#!/bin/bash

#检测次数
count=0

while true

do

count=$(($count+1))
now=$(date "+%Y%m%d %H:%M:%S")
echo "-------第 $count 次（5分钟/次）检测($now)-------"  >> run.log

#取相关进程ID号
list="$(ps -ef | grep "进程关键字" | grep -v grep | awk '{print $2}')"
#echo $list

#循环取时间，并kill运行时间超过10分钟的进程
for pid in $list
do

time="$(ps -p $pid -o etimes | awk 'NR!=1 {print}')"

#echo $time

if [ $time -ge '600'  ];then

ps -eo pid,etime,cmd | grep $pid | grep -v grep >> kill_beian_thread.log
kill -9 $pid

fi

done

#暂停5分钟
sleep 300

done
