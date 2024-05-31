import os
from pyspark import SparkConf, SparkContext
if __name__ == "__main__":
    #os.environ['SPARK_HOME'] = "E:/python/python-learn/.venv/Lib/site-packages/pyspark"
    os.environ['PYSPARK_PYTHON'] = "E:/python/pythonProject/.venv/Scripts/python.exe"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    rdd = sc.parallelize([1, 2, 3, 4, 5])

    # collect 输出算子 把rdd转为Python list
    rdd_list = rdd.collect()
    print(rdd_list)
    print(type(rdd_list))

    # reduce 对rdd数据集按照传入的逻辑进行聚合
    num = rdd.reduce(lambda a, b: a+b)
    print(num)

    # take 算子 取出rdd的前N个元素，组合成list返回给你
    nums = rdd.take(3)
    print(nums)

    # count 算子 统计rdd内有多少条数据，返回值为数字
    print(rdd.count())
    sc.stop()
