#!/bin/bash

if [ -d directory ]
then
    echo "demo directory already exist"
    exit 0
fi

mkdir directory

for folder in a b .c
do
    mkdir directory/$folder
done

for file in a/1 b/1 b/2 .c/1
do
    echo -e "$file\n" >> directory/$file.txt
    base64 /dev/urandom | head -c 500 >> directory/$file.txt
    echo "" >> directory/$file.txt
done

echo "created demo directory"