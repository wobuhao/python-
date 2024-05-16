
import os
from pyspark import SparkConf, SparkContext
#os.environ['SPARK_HOME'] = "E:/python/python-learn/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = "E:/python/pythonProject/.venv/Scripts/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

def hah(i):
    return i * 10
rdd2 = rdd.map(lambda i: i * 10)

print(sc.version)
print(rdd2.collect())

sc.stop()
