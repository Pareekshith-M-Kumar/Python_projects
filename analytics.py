
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round as spark_round

# 1. Start Spark
spark = (
    SparkSession.builder
    .appName("KaratePerformanceAnalytics")
    .master("local[*]")
    .getOrCreate()
)

# 2. Load the karate dataset
df = spark.read.csv(
    "karateAnalytics.csv",
    header=True,
    inferSchema=True
)

# 3. Calculate each student's win rate
df = df.withColumn(
    "WinRate",
    spark_round(
        col("Wins") / (col("Wins") + col("Losses")) * 100,
        2
    )
)

# 4. Display the results
df.select(
    "Student",
    "Wins",
    "Losses",
    "WinRate"
).show()

# 5. Display basic skill statistics
df.select(
    "Punches",
    "Kicks",
    "Stamina",
    "Defense"
).describe().show()

# 6. Stop Spark
spark.stop()
