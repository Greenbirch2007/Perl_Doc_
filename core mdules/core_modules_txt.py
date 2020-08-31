






# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本


import csv
import datetime

import os
import re
import time
import sys

type = sys.getfilesystemencoding()
import pymysql
import xlrd
import requests
from requests.exceptions import RequestException
from lxml import etree


def call_page(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  #
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def removeDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items





def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile






def getOneText(url):
    html = call_page(url)
    selector = etree.HTML(str(html))
    title = selector.xpath('//*[@id="content"]/div/div[2]/article/div/ul/li/a/text()')
    content = selector.xpath('//*[@id="content"]/div/div[2]/article/div/ul/text()')
    f_content = []
    for item in content:
        f_content.append(" ".join(item.split()))


    half_url = selector.xpath('//*[@id="content"]/div/div[2]/article/div/ul/li/a/@href')
    f_url = []
    for item in half_url:
        f_url.append("https://perldoc.perl.org/5.32.0/"+item)
    for i1,i2,i3 in zip(title,f_content[1:],f_url):
        print(i1)
        big_l.append((i1, i2,i3))






def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('core_m.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)
        print("保存完成")

if __name__ == '__main__':
    big_l =[]


    for item in range(64,91):
        url = 'https://perldoc.perl.org/5.32.0/index-modules-{0}.html'.format(chr(item))

        getOneText(str(url))

    for sname in big_l:
        for one_c in sname:
            try:# 保存必须是str的类型
                with open('k_module.txt', 'a') as file_handle:
                    # .txt可以不自己新建,代码会自动新建

                    file_handle.write(one_c + ",")  # 写入
                    file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
                    print("{0} 整理完毕".format("k_module"))
            except:
                pass
