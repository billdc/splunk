#!/usr/bin/python
import sys
import os
import csv
import datetime


if len(sys.argv) > 0:
    now = str(datetime.datetime.now())
    path = "/tmp/" + sys.argv[4] + "_results.csv"
    cmd = "gunzip -c " + sys.argv[8] + " > " + path
    f = open("/tmp/console", "a")
    os.system(cmd)
    level = sys.argv[4].split("_")[-1]
    field = sys.argv[4].split("_")[-2]
    sys_name = sys.argv[4].split("_")[2]
    uri = sys.argv[6]
    c_reader = csv.reader(open(path))
    oid_2 = "1.3.6.1.4.1.27389.1."
    oid = oid_2 + "1."
    csv_head = c_reader.next()
    i=csv_head.index(field)
    j=csv_head.index("host")
    for line in c_reader:
        error_msg = sys_name + "," + str(line[i])
        host_ip = str(line[j])
        #snmp = '''/usr/bin/snmptrap -v 2c -c public 10.20.22.49:162 '' \
        # %s2 %s1 s "%s" %s2 s "%s" %s3 s "%s" %s4 s "%s" %s5 s "%s"''' \
        #% (oid_2,oid,now,oid,level,oid,host_ip,oid,error_msg,oid,uri)
        #os.system(snmp)
        #f.write(snmp)
        f.write("message:"+error_msg+"\n")
        f.write("ip:"+host_ip+"\n")
    f.write("\n\n\n\n")
    f.close()
