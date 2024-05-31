# 练习案例
import os
import json
from pyspark import SparkConf, SparkContext
if __name__ == "__main__":
    #os.environ['SPARK_HOME'] = "E:/python/python-learn/.venv/Lib/site-packages/pyspark"
    os.environ['PYSPARK_PYTHON'] = "E:/python/pythonProject/.venv/Scripts/python.exe"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    rdd_orders = sc.textFile("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第15章资料/资料/orders.txt")
    rdd_datas = rdd_orders.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x))
    #rdd_datas = rdd_datas.sortBy(lambda x: float(x['money']), ascending=False, numPartitions=1)
    # 按销售额排序
    print(rdd_datas.map(lambda x: (x['areaName'], float(x['money']))).reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], ascending=False, numPartitions=1).collect())
    # 取出所有在售的商品类别
    print(rdd_datas.map(lambda x: x['category']).distinct().collect())
    # 取出北京的数据
    beijing_rdd = rdd_datas.filter(lambda x: x['areaName'] == '北京')
    result_rdd = beijing_rdd.map(lambda x: f"{x['areaName']}_{x['category']}")
    print(result_rdd.collect())

    sc.stop()