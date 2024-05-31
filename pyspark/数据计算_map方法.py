
import os
from pyspark import SparkConf, SparkContext
if __name__ == "__main__":
    #os.environ['SPARK_HOME'] = "E:/python/python-learn/.venv/Lib/site-packages/pyspark"
    os.environ['PYSPARK_PYTHON'] = "E:/python/pythonProject/.venv/Scripts/python.exe"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)

    # map(func) 算子
    rdd = sc.parallelize([1, 2, 3, 4, 5])
    rdd2 = rdd.map(lambda i: i * 10)

    print(rdd2.collect())

    # flatMap(func) 算子 对rdd执行map操作，然后进行解除嵌套操作
    lists = [[1, 2, 3], [4, 5, 6,]]
    lists2 = ["a b c", "e f g"]
    rdd2 = sc.parallelize(lists2)
    print(rdd2.flatMap(lambda x: x.split(' ')).collect())

    # reduceByKey(func) 算子
    rdd3 = sc.parallelize([('a', 1), ('a', 1), ('b', 2), ('b', 3), ('b', 4)])
    print(rdd3.reduceByKey(lambda a, b: a + b).collect())

    # 练习案例
    rdd_file = sc.textFile("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
    words = rdd_file.map(lambda x: (x.split(",")[3], 1))
    word_one = words.reduceByKey(lambda a, b: a + b)
    print(word_one.collect())

    # filter(func) 算子 过滤想要的数据进行保留
    rdd_filter = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8])
    print(rdd_filter.filter(lambda num: num % 2 == 0).collect())

    # distinct() 算子 对rdd进行去重
    rdd_distinct = sc.parallelize([1, 2, 2, 3, 'hah', 'hah', 'haha'])
    print(rdd_distinct.distinct().collect())

    # sortBy(func, ascending=False, numPartitions) 算子 对rdd数据进行排序，基于你指定的排序依据
    # func：排序方法，告知根据哪个数据排序 ascending：True升序，False降序 numPartitions：用多少分区排序
    final_rdd = word_one.sortBy(keyfunc=lambda x: x[1], ascending=False, numPartitions=1)
    print(final_rdd.collect())

    sc.stop()
