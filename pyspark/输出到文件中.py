import os
from pyspark import SparkConf, SparkContext
if __name__ == "__main__":
    #os.environ['SPARK_HOME'] = "E:/python/python-learn/.venv/Lib/site-packages/pyspark"
    os.environ['PYSPARK_PYTHON'] = "E:/python/pythonProject/.venv/Scripts/python.exe"
    os.environ['HADOOP_HOME'] = 'D:/hadoop-3.0.0'
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    # 修改rdd分区为1个，两种方式
    # 方式1：SparkConf对象设置属性全局并行为1
    conf.set('spark.default.parallelism', "1")
    sc = SparkContext(conf=conf)
    # 方式2：创建rdd的时候设置parallelize方法传入numSlices参数为1
    rdd = sc.parallelize([1, 2, 3, 4, 5])
    # rdd.saveAsTextFile('E:/data')
    print(rdd.collect())
    sc.stop()
