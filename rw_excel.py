import openpyxl
import xlrd
import xlwt


def read_excel_sheet(filename,sheetname):
    '''
    读取excel文件的指定sheet数据
    :param filename: 文件路径
    :param sheetname: sheet名称
    :return: [[‘第一行数据’],[‘第二行数据’],...]
    '''
    wb = openpyxl.load_workbook(filename)
    sheet=wb[sheetname]
    new_sheet=list()
    for row in sheet.rows:
        new_row=list()
        for cell in row:
            new_row.append(cell.value)
        new_sheet.append(new_row)
    return new_sheet


def read_excel_xlrd(file,sheets_name):
    '''
    读excel表格的首列数据
    :param file: 文件路径
    :param sheets_name: 表格名称
    :return: 每一行的第一个单元格（列表）
    '''
    workbook = xlrd.open_workbook(file)  # 打开工作簿
    worksheet = workbook.sheet_by_name(sheets_name)  # 获取工作簿中指定表格
    datas=list()
    for i in range(0, worksheet.nrows):
        datas.append(worksheet.cell_value(i, 0))   #读每行首列数据
    return datas


def write_excel_xlwt(file,sheet_name,value):
    '''
    将数据写入excel表格
    :param file: 文件路径
    :param sheet_name: 表格名称
    :param value: 待写入的数据(每一行为列表，列表套列表)
    :return: 无
    '''
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 向表格中写入数据（对应的行和列）
    workbook.save(file)  # 保存工作簿





