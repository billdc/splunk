#!/bin/sh
SPLUNK=/opt/splunk/bin/splunk
while true;do
    TIME=`date +%H%M%S`
    LOG_DIR='/home/applog/test'
    if [ $TIME -le 170000 ];then
        if [ "`ls -A $LOG_DIR`" = "" ];then
            echo "stop splunk"
            date +%H%M%S
            #splunk stop
            #splunk clean all
            break
        fi
    else
        break
    fi
    sleep 5
done

while true;do
    if [ $DATE -gt 140000 ];then
        echo "start splunk"
        exit
    fi
    sleep 10
done
