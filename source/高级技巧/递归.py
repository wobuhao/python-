import os


def test_os():
    print(os.listdir('D:/test'))  # 列出路径下的内容
    print(os.path.isdir('D:/test/a'))  # 判断指定路径是不是文件夹
    print(os.path.exists('D:/test'))  # 判断指定路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list 包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path},不存在")
        return []

    return file_list


if __name__ == "__main__":
    get_files_recursion_from_dir('D:/test')
