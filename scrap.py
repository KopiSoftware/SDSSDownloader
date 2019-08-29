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
scale_info = "set image scale  sec per pix,指定尺寸 角秒/像素"
width_info = "width,宽度"
height_info = "height,高度"


abs_path = os.path.split(os.path.abspath("__file__"))[0]

parser = argparse.ArgumentParser()
parser.add_argument('-c', "--csv", dest='filename',default=os.path.join(abs_path,'starlist.csv'),
                    help=file_help)
parser.add_argument('-s', "--scale", dest='scale',default=0.4,help=scale_info)
parser.add_argument('-W', "--width", dest='width',default=500, help=width_info)
parser.add_argument('-H', "--height", dest='height',default=400, help=height_info)

csv_arg = parser.parse_args()
csv_file = csv_arg.filename
scale = csv_arg.scale
width = csv_arg.width
height = csv_arg.height
    

i = 0
with open(csv_file, 'r') as file_in:
    
    f_csv = csv.reader(file_in)
    for obj in f_csv:
        ra, dec = obj[0],obj[1]
        
        print(str(i)+"    ra: "+ra+"   dec: "+dec)
        url = "http://skyserver.sdss.org/dr14/SkyserverWS/ImgCutout/getjpeg?"+ \
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
        
        
        
        
        
        
        

        
        