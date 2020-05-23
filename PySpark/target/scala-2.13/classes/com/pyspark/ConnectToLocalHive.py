from logging import *
from pyspark.sql import SparkSession
from os.path import abspath
# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')
sparkSessionObj = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

log =getLogger("jobLogger")
log.info("Info message")
log.error("Error message")

#sparkSessionObj.sql("create database if not exists rakesh")
#sparkSessionObj.sql("drop database if exists demo")
sparkSessionObj.sql("show databases").show()
#sparkSessionObj.sql("use demo")
#sparkSessionObj.sql("show databases").show()
#sparkSessionObj.sql("CREATE TABLE IF NOT EXISTS employee(id INT, name STRING, age INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
#sparkSessionObj .sql("CREATE TABLE src(key INT, value STRING) USING hive")
#sparkSessionObj .sql("show tables").show()
#spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")