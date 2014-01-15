#!/bin/sh
DIRECTORY='/home/applog/test'
if [ "`ls -A $DIRECTORY`" = "" ];then
    echo "no file"



else 
    echo "not empty"
fi
