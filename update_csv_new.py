#!/usr/bin/python
#coding:utf-8
import sys
import os
import csv
import datetime

if(len(sys.argv)>0):
    bank_dist = {
        "310001":"浦东",
        "310002":"虹口",
        "310003":"闵行"
    }
    now = str(datetime.datetime.now())
    path = "/tmp/"+sys.argv[4]+"_results.csv"
    cmd = "gunzip -c "+sys.argv[8]+" > "+ path
    f = open("/tmp/console","a")
    f.write(cmd)
    f.write("\n")
    f.close()
    os.system(cmd)
    uri = sys.argv[6]
    c_file = file(path,'rb')
    c_reader = csv.reader(c_file)
    f = open("/home/neo/splunk/etc/system/lookups/test_splunk.csv","a")
    f.write("test,test")
    for row in c_reader:
        if bank_dist.has_key(row[2]):
            f.write(row[0])
            f.write(row[1]+"\n")
            f.write(row[2]+"\n")
            f.write(row[3]+"\n")
            f.write(row[0],bank_dist[row[2]])
            f.write("\n")
          
    f.close()
    c_file.close()
            
