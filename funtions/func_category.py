






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
    with open('func_category.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)
        print("保存完成")

if __name__ == '__main__':
    big_l =[]
    lpath = os.getcwd()
    excelFile = '{0}\\tc.xlsx'.format(lpath)
    full_items = read_xlrd(excelFile=excelFile)
    for i1,i2 in zip(full_items,range(1,21)):

        one_url ='https://perldoc.perl.org/5.32.0/index-functions-by-cat.html#'+i1[0]
        f_OneUrl = "-".join(one_url.split())
        the1_num = i2
        the2_num = i2+1
        print(f_OneUrl,the1_num,the2_num)
        html = call_page(one_url)
        selector = etree.HTML(str(html))
        the1 = '//*[@id="content"]/div/div[2]/article/div/h2[{0}]/text()'.format(the1_num)
        the2_title = '//*[@id="content"]/div/div[2]/article/div/ul[{0}]/li/a/text()'.format(the2_num)
        the2_url = '//*[@id="content"]/div/div[2]/article/div/ul[{0}]/li/a/@href'.format(the2_num)
        the2_cotent = '//*[@id="content"]/div/div[2]/article/div/ul[{0}]/text()'.format(the2_num)


        the1_xp = selector.xpath(the1)
        the2_title_xp = selector.xpath(the2_title)
        the2_url_xp = selector.xpath(the2_url)
        the2_cotent_xp = selector.xpath(the2_cotent)
        f_the1 = len(the2_title_xp) * the1_xp
        for i1, i2, i3, i4 in zip(f_the1, the2_title_xp, the2_url_xp, the2_cotent_xp[1:]):
            big_l.append((i1, i2, 'https://perldoc.perl.org/5.32.0/' + i3, "-".join(i4.split())))
    headers =["tc","title","url","content"]
    writerDt_csv(headers,big_l)


    # big_l =[]
    # url = 'https://perldoc.perl.org/5.32.0/index-functions-by-cat.html'
    # getOneText(url)
    #




    # headers =["title","content","url"]
    # writerDt_csv(headers,big_l)



