# -*- coding: utf-8 -*-
# @Time : 2020/3/25 20:49
# @Author : NamakoNeko
# @Version : 
# @Function :

import jsonpath
import json
import os


def all_path(dirname):
    result = []  # 所有的文件
    filter = [".json"]
    for maindir, subdir, file_name_list in os.walk(dirname):

        # maindir 当前主目录
        # subdir 当前主目录下的所有目录
        # file_name_list 当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            filename_withoutext = os.path.splitext(apath)[0]
            if ext in filter:
                result.append(filename_withoutext)

    return result


def recurr_print_descs(desc, valid, choice, filepath):
    listrange = len(desc)
    count = 0
    with open(filepath, 'w',encoding='utf-8') as fp:
        while count < listrange:
            fp.write(str(count + 1) + str(desc[count]) + '\n' + str(valid[count]) + '\n' + str(choice[count]) + '\n\n')
            count = count + 1


filepath = all_path(".\\")
count = 0
while count < len(filepath):
    with open(filepath[count] + ".json", 'r', encoding='utf-8') as loadfile:
        loaddata = json.load(loadfile)
    item_desc = jsonpath.jsonpath(loaddata, '$..item_desc')
    item_valid = jsonpath.jsonpath(loaddata, '$..item_valid')
    item_choice = jsonpath.jsonpath(loaddata, '$..item_choice')
    recurr_print_descs(item_desc, item_valid, item_choice, filepath[count] + ".txt")
    count = count + 1