#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    将特定位置的 Logo 替换为 InnoTree 的 Logo
    指定位置：
            以 距离下40 距离右110 为原点，进行替换。
"""
import cv2
import os
import shutil
# mask = cv2.imread('/Users/wuweigong/Downloads/org/mask.jpeg')
mask = cv2.imread('/home/weigong.wu/python_script/wash_logo/mask.jpeg')


def getFiles(path):
    result = []
    [result.append(path+x) for x in os.listdir(path) if os.path.join(path, x) and (os.path.splitext(x)[1] == '.jpg'
                                                                                   or os.path.splitext(x)[1] == '.png')]
    return result


def processing(files):
    global mask  # 获得InnoTree Logo
    for src_file in files:
        src_img = cv2.imread(src_file)

        try:
            x, y, z = src_img.shape
            if x >= 40 and y > 110:
                start = x - 40
                end = y - 110
                for i in range(30):
                    for j in range(100):
                        src_img[start+i, end+j] = mask[i, j]
                str_file = str(src_file).split('/')
                str_file[4] = 'logo_new'
                str_file.remove('')
                str_result = ''
                for z in str_file:
                    str_result += '/'+z
                cv2.imwrite(str_result, src_img)
                os.remove(src_file)
            elif x > 10 and y > 110:
                start = 0
                end = y - 110
                for i in range(x - 10):
                    for j in range(100):
                        src_img[start+i, end+j] = mask[i, j]
                str_file = str(src_file).split('/')
                str_file[4] = 'logo_new'
                str_file.remove('')
                str_result = ''
                for z in str_file:
                    str_result += '/' + z
                cv2.imwrite(str_result, src_img)
                os.remove(src_file)
            else:
                no_process = '/home/etl_user/etl/logo_new/'+os.path.basename(src_file)
                # no_process = '/Users/wuweigong/Downloads/result/' + os.path.basename(src_file)
                shutil.copyfile(src_file, no_process)
                os.remove(src_file)
        except AttributeError:
            print(src_file)


if __name__ == '__main__':
    # src_path = '/Users/wuweigong/Downloads/org/'
    src_path = '/home/etl_user/etl/logo/'
    org = getFiles(src_path)  # 获取所有文件合法
    processing(org)
