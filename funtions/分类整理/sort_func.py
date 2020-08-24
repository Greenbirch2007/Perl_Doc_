  # coding=utf-8
import os
import csv
import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile

def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('sort_func.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)
        print("保存完成")
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == '__main__':
    lpath = os.getcwd()
    big_l= []

    excelFile = '{0}\\func_category.xlsx'.format(lpath)
    names_list = set()
    for item in read_xlrd(excelFile=excelFile):
        names_list.add(item[0])
    full_items = read_xlrd(excelFile=excelFile)
    for single_name  in names_list:
        one_list = []
        one_list.append(single_name)
        for item in full_items:
            if single_name == item[0]:
                one_list.append(item[1])
            else:
                pass
        big_l.append(one_list)
    headers =["tc","title"]
    writerDt_csv(headers,big_l)
