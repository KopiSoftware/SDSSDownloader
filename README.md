# SDSSDownloader  
##Instructions  
**SSDS Downloader** can download processed images from SSDS Dataset Release 12 or 14.  
1. First,you must download csv form SSDS SQL database.    
2. Keep dec and ra only,**DO NOT keep column or row name**  
3. Run this command you will get help.Learn how to setup arguments and run:  
'python ./scrapy.py --help'

###**NOTICE** If this program without any arguments,the program will download a set of demo in Download directory.  

##Example  
'python ./scrapy.py -c download.csv -v 12 -W 960 -H 720 --scale 0.5'
