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

dir=$(pwd)

echo -e "lets print the current working directory with the following command:\n\n$dir$ pwd"

wait

pwd

wait

echo -e "lets print all files and folders in the current directory with:\n\n$dir$ ls"

wait 

ls

wait

echo -e "lets change our directory to $(pwd)/directory with:\n\n$dir$ cd directory"

wait

cd directory

echo -e "lets verify our working directory followed by it's contents with \"pwd\" followed by \"tree -a\""

wait

dir=$(pwd)

echo "$dir$ pwd"

wait

pwd

wait

echo "$dir$ tree -a"

wait 

tree -a

wait

echo -e "we know there are three folders in our current directory from the previous executing of \"tree -a\""
echo -e "lets verify this by using the \"ls\" command:\n\n$dir$ ls"

wait

ls

wait

echo "notice how the \".c\" folder is missing?"
echo "this is because files and folders that start with a \".\" are hidden in linux"
echo -e "we can tell \"ls\" to show hidden objects by the following command:\n\n$dir$ ls -all"

wait

ls -all

wait

echo -e "lets try making a directory \"d\" as well as the subdirectory \"d/e\"\n\n$dir$ mkdir d\n$dir$ mkdir d/e"

wait

mkdir d
mkdir d/e

wait

echo -e "we can create a blank txt file in the subdirectory with \n\n$dir$ touch d/e/1.txt"

wait

touch d/e/1.txt

echo -e "and verify the current tree of our directory with \"tree -a\"\n\n$dir$ tree -a"

wait

tree -a

exit 0

