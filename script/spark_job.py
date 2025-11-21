from pyspark.sql import SparkSession
def main():
    spark = SparkSession.builder \
    .appName("YourAppName") \
        .config("spark.some.config.option", "some-value") \
            .getOrCreate()
    
print("hello Spark")
spark.stop()

if __name__ == "__main__":
    main()

