#! /bin/bash

rm -rf "电视剧"
mkdir  "电视剧"

rm -rf "电影"
mkdir "电影"

rm -rf "动漫"
mkdir  "动漫"

rm -rf "综艺"
mkdir  "综艺"

rm -rf "韩剧"
mkdir  "韩剧"

rm -rf "日剧"
mkdir  "日剧"

rm -rf "其他"
mkdir "其他"

#jpython=`which python3`
python3 format.py movie.txt
#python3.7 weixin_gonggao.py movie.txt
echo "finish `date +"%Y%m%d"`"
