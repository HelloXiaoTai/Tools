import csv


def read_csv_col(filename, col_name):
    '''
    读取csv文件的某一列数据，csv文件的第一行为列名
    :param filename: 文件路径
    :param col_name: 列名（第一行）
    :return: 指定列的所有数据（列表形式）
    '''
    col = list()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            cell = row[col_name]
            col.append(cell)
    return col


def read_csv_all(filename, read_head_row=True):
    '''
    读取csv文件的所有行列数据
    :param filename: 文件路径
    :param read_head_row: 是否读取第一行，默认是
    :return: 所有行所有列数据（每一行为单独的列表）
    '''
    rows = list()
    with open(filename) as f:
        reader = csv.reader(f)
        if not (read_head_row):
            next(reader)
        for row in reader:
            rows.append(row)
    return rows


def write_csv_row(filename, row):
    '''
    追加写入csv文件
    :param filename: 文件路径
    :param row: 待写入的行（列表）
    :return: 无
    '''
    with open(filename, "a", newline='', encoding="utf-8") as out:
        csv_write = csv.writer(out, dialect='excel')
        csv_write.writerow(row)


if __name__ == '__main__':
    domains = read_csv_all(r'E:\pythonProjects\domian_info\second_data\demo.csv', read_head_row=False)
    print(domains)
