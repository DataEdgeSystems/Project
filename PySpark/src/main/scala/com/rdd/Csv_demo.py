from pyspark.sql import SparkSession


class Csv_demo:
    @staticmethod
    def csv_test():
        try:
            spark = SparkSession.builder.appName("test").getOrCreate()
            data_df = spark.read.csv('C:\\Project\\Files\\Input\\csv\\Sample.csv', inferSchema=True, header=True)
            print(type(data_df))
            # print(dataDF.show())
            print(data_df.printSchema())

            # Creating a Temp View from the data_frame
            data_df.createOrReplaceTempView("records")

            sql_df = spark.sql("select * from records where Units > 50")
            print(sql_df.show())
            print(type(data_df))
            print(type(sql_df))

        except ValueError:
            print("Not able to read the csv file")


if __name__ == "__main__":
    Csv_demo.csv_test()


