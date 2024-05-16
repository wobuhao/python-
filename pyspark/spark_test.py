from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"name": "hymn", "age": 30})

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 通过textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd_file = sc.textFile("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")

print(rdd_file.collect())


# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()
