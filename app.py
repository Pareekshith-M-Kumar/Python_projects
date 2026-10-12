
import streamlit as st
import plotly.express as px
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round as spark_round

# Page configuration
st.set_page_config(
    page_title="Karate Performance Analytics",
    page_icon="🥋",
    layout="wide"
)

st.title("🥋 Karate Performance Analytics")
st.write("Analyze karate students' skills and competition results.")

# Start Spark
@st.cache_resource
def create_spark():
    return (
        SparkSession.builder
        .appName("KarateDashboard")
        .master("local[*]")
        .getOrCreate()
    )

spark = create_spark()

# Load data
df = spark.read.csv(
    "KarateAnalytics.csv",
    header=True,
    inferSchema=True
)

# Calculate win rate
df = df.withColumn(
    "WinRate",
    spark_round(
        col("Wins") / (col("Wins") + col("Losses")) * 100,
        2
    )
)

# Convert results for dashboard display
data = df.toPandas()

# Sidebar filter
st.sidebar.header("Student Filter")
student = st.sidebar.selectbox(
    "Select a student",
    ["All Students"] + data["Student"].tolist()
)

if student != "All Students":
    data = data[data["Student"] == student]

# Summary metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", len(data))
col2.metric("Total Wins", int(data["Wins"].sum()))
col3.metric("Total Losses", int(data["Losses"].sum()))

average_win_rate = data["WinRate"].mean()
col4.metric("Average Win Rate", f"{average_win_rate:.1f}%")

# Competition performance
st.subheader("Competition Performance")

fig = px.bar(
    data,
    x="Student",
    y=["Wins", "Losses"],
    barmode="group",
    title="Wins vs Losses"
)

st.plotly_chart(fig, use_container_width=True)

# Skill analysis
st.subheader("Skill Comparison")

skills = ["Punches", "Kicks", "Stamina", "Defense"]

skill_data = data.melt(
    id_vars=["Student"],
    value_vars=skills,
    var_name="Skill",
    value_name="Score"
)

fig2 = px.bar(
    skill_data,
    x="Student",
    y="Score",
    color="Skill",
    barmode="group",
    title="Karate Skill Scores (out of 100)",
    range_y=[0, 100]
)

st.plotly_chart(fig2, use_container_width=True)

# Student records
st.subheader("Student Records")
st.dataframe(data, use_container_width=True)

# Basic improvement suggestions
st.subheader("Training Focus")

for _, row in data.iterrows():
    weakest_skill = min(skills, key=lambda skill: row[skill])
    st.write(
        f"**{row['Student']}**: Focus on improving "
        f"**{weakest_skill}** (score: {row[weakest_skill]}/100)."
    )
