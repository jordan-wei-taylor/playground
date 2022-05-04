#!/bin/bash

for folder in directory __pycache__ env
do
    rm -rf $folder
done

for file in requirements.txt script.py
do
    if [ -f $file ]
    then 
        rm $file
    fi
done

echo "removed demo directory and files"
