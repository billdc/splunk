#!/usr/bin/python
import sys
import os
import csv
import datetime


if(len(sys.argv)>0):
    now = str(datetime.datetime.now())
    path = "/tmp/"+sys.argv[4]+"_results.csv"
    cmd = "gunzip -c "+sys.argv[8]+" > "+ path
    f = open("/tmp/console","a")
    f.write(cmd)
    f.write("\n")
    os.system(cmd)
    level = sys.argv[4].split("_")[-1]
    sys_name = sys.argv[4].split("_")[1]
    #sys_name="test_system"
    uri = sys.argv[6]
    c_reader = csv.reader(open(path))
    c_reader.next()
    oid_2 = "1.3.6.1.4.1.27389.1."
    oid  = oid_2 + "1."
    for line in c_reader:
        error_msg = line[0]
        host_ip = line[1]
        snmp = '''/usr/bin/snmptrap -v 2c -c public 10.20.22.49:162 '' %s2 %s1 s "%s" %s2 s "%s" %s3 s "%s" %s4 s "%s" %s5 s "%s" %s6 s "%s"''' \
        % (oid_2,oid,sys_name,oid,level,oid,host_ip,oid,now,oid,error_msg,oid,uri) 
        os.system(snmp)
        f.write(snmp)
        f.write("\n")
    f.close()
