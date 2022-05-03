if [ ! -d directory ]
then
    echo -e 'please first execute the "directory.sh" file by executing the following line\n\n./directory.sh\n\nthen re-run\n\n./directory-demo.sh\n'
    exit 0
fi
    
function wait {
    echo ""
    read -n 1 -s -r -p "[Press any key to continue]"
    echo -ne "\033[2K\r"
}

echo -e "lets print the current working directory with the following command:\n\n$ pwd"

wait

pwd

wait

echo -e "lets print all files and folders in the current directory with:\n\n$ ls"

wait 

ls

wait

echo -e "lets change our directory to $(pwd)/directory with:\n\n$ cd directory"

wait

cd directory

echo -e "lets verify our working directory followed by it's contents with \"pwd\" followed by \"tree -a\""

wait

echo "$ pwd"

wait

pwd

wait

echo "$ tree -a"

wait 

tree -a

wait 