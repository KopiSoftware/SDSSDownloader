# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:15:21 2019

@author: MECHREV
"""

import os
import requests
import csv
import argparse

        


file_help = "select csv file(指定csv文件),请不要在路径中包含空格。"


abs_path = os.path.split(os.path.abspath("__file__"))[0]

parser = argparse.ArgumentParser()
parser.add_argument("--csv", '-c', dest='filename', help=file_help)


csv_arg = parser.parse_args()
csv_file = csv_arg.filename
if csv_file == None:
    print('No file input or input failed, default file has been added in.')
    csv_file = os.path.join(abs_path,'starlist.csv')
    
scale = 1


i = 0
with open(csv_file, 'r') as file_in:
    
    f_csv = csv.reader(file_in)
    for obj in f_csv:
        ra, dec = obj[0],obj[1]
        
        print(str(i)+"    ra: "+ra+"   dec: "+dec)
        width, height = 500, 300
        url = "http://skyserver.sdss.org/dr12/SkyserverWS/ImgCutout/getjpeg?"+ \
                "ra="+str(ra)+ \
                "&dec="+str(dec)+ \
                "&width="+str(width)+ \
                "&height="+str(height)+ \
                "&scale="+str(scale)
                
        response = requests.get(url)
        
        
        filename = os.path.join(abs_path, "Download","{:0>6}.jpg".format(str(i)) )
        with open(filename,"wb") as img:
            img.write(response.content)
        i = i + 1
        
        
        
        
        
        
        

        
        