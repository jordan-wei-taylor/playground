#!/bin/bash

rm -rf directory
rm -rf __pycache__

for file in requirements.txt script.py
do
    if [ -f $file ]
    then 
        rm $file
    fi
done


echo "removed demo directory and files"