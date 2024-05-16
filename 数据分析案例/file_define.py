from data_define import Record
import json


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileeReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(date=data_list[0], order_id=data_list[1], money=int(data_list[2]), province=data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(date=data_dict["date"], order_id=data_dict["order_id"], money=int(data_dict["money"]),
                            province=data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileeReader('F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt')
    list1 = text_file_reader.read_data()
    for z in list1:
        print(f"{z}")
    print('陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省陕西省')
    json_file_reader = JsonFileReader('F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt')
    list2 = json_file_reader.read_data()
    for z in list2:
        print(f"{z}")
