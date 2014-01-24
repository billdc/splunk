#coding:utf-8
#!/usr/bin/python
import csv

#path = '/home/neo/Desktop/dist.csv'
path = './original.csv'
c_file = file(path,'rb')
c_reader = csv.reader(c_file)
bank_dist = {
    "310001":"浦东",
    "310002":"虹口",
    "310003":"闵行"
}


for row in c_reader:
    if bank_dist.has_key(row[1]):
        print row[0],bank_dist[row[1]]


c_file.close()
