import csv


# DictReader
def read_csv_col(file_path, label):
    '''
    读取csv文件的某一列数据，csv文件的第一行为列名
    :param file_path: 文件路径
    :param label: 某一列的列名（第一行）
    :return: 指定列的所有数据（列表形式）
    '''
    col = list()
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cell = row[label]
            col.append(cell)
    return col

def read_csv_dict(file_path):
    '''
    读取csv文件的所有，csv文件的第一行为列标题
    :param file_path: 文件路径
    :return: 所有行的数据（每一行为字典，字典的key为列标题）
    '''
    rows = list()
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            new_row = dict()
            for label in row:
                new_row[label] = row[label]
            rows.append(new_row)
    return rows


# DictWriter
def write_csv_dict(file_path, labels, rows):
    '''
    将字典形式的数据写入csv文件
    :param file_path: 输出的文件路径
    :param labels: 列名（第一行）,字典的键值[key1,key2,key3...]
    :param rows :写入的字典，[{key1:value1,key2:value2,key3:value3...},{key1:value1,key2:value2...}]
    :return:
    '''
    out = open(file_path, 'a', newline='', encoding='utf-8')
    csv_writer = csv.DictWriter(out, fieldnames=labels)
    csv_writer.writeheader()  # 列标题写入第一行
    for row in rows:
        csv_writer.writerow(row)  # 每一行是字典
    out.close()


# reader
def read_csv_all(file_path, read_head_row=True):
    '''
    读取csv文件的所有行列数据
    :param file_path: 文件路径
    :param read_head_row: 是否读取第一行，默认是
    :return: 所有行所有列数据（每一行为单独的列表）
    '''
    rows = list()
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        if not (read_head_row):
            next(reader)
        for row in reader:
            rows.append(row)
    return rows


# writer
def write_csv_row(file_path, row):
    '''
    追加写入csv文件
    :param file_path: 文件路径
    :param row: 待写入的行（列表）
    :return: 无
    '''
    with open(file_path, "a", newline='', encoding="utf-8") as out:
        csv_write = csv.writer(out, dialect='excel')
        csv_write.writerow(row)
