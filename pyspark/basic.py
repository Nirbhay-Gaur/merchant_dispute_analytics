from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DisputeAnalytics")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv('data\disputes.csv')
)

df.show(5)

summary = (
    df.groupBy("merchant_segment")
    .count()
    .orderBy("count", ascending=False)
)

summary.show()

spark.stop()