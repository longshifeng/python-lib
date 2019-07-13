def deal_with_file(src_file_dir,file_name,dst_file_dir):
    with open(src_file_dir+file_name,"r+",encoding="utf-8") as f:
        lines = f.readlines()
    #print(lines)
    with open(dst_file_dir+file_name+"_deal.edges","w+",encoding="utf-8") as f_w:
        for line in lines:
            if "#" in line:#去除包含#的头信息行
                continue
            if "|" in line:
                temp=line.split("|",2)# src|dst|weight->src\tdst
                # print(temp[0],temp[1])
                node_pair=temp[0]+"\t"+temp[1]+"\r"
                # print(node_pair)
                f_w.write(node_pair)
        print(filename+" finish")
        f_w.close()

import os
# import pandas as pd
src_file_dir= 'I:/2019.7/2016.1-12/'
dst_file_dir='I:/2019.7/2016.1-12_deal.edges/'
for root, dirs, files in os.walk(src_file_dir):  #root 根目录，dirs 子目录
    files.sort(reverse=False)  # files是路径下包含所有文件的遍历列表(乱序)
    for filename in files:
        if ".bz2" not in filename:
            print(src_file_dir,filename)
            deal_with_file(src_file_dir,filename,dst_file_dir)

