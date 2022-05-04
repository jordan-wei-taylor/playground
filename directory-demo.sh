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

left="\e[1m\e[92muser@device\e[0m"

function set_dir {

    if [ $# -eq 0 ]
    then
        right="\e[1m\e[34m~\e[0m"
    else
        right="\e[1m\e[34m~/$1\e[0m"
    fi

    dir="$left:$right$"

}

set_dir

echo -e "lets print the current working directory with the following command:\n\n$dir pwd"

wait

pwd

wait

echo -e "lets print all files and folders in the current directory with:\n\n$dir ls"

wait 

ls

wait

echo -e "lets change our directory to $(pwd)/directory with:\n\n$dir cd directory"

wait

cd directory

echo -e "lets verify our working directory followed by it's contents with \"pwd\" followed by \"tree -a\""

wait

set_dir directory

echo -e "$dir pwd"

wait

pwd

wait

echo -e "$dir tree -a"

wait 

tree -a

wait

echo -e "we know there are three folders in our current directory from the previous executing of \"tree -a\""
echo -e "lets verify this by using the \"ls\" command:\n\n$dir ls"

wait

ls

wait

echo "notice how the \".c\" folder is missing?"
echo "this is because files and folders that start with a \".\" are hidden in linux"
echo -e "we can tell \"ls\" to show hidden objects by the following command:\n\n$dir ls -all"

wait

ls -all

wait

echo -e "we can print text files to the terminal using the command \"cat\", for example\n\n$dir cat a/1.txt"

wait

cat a/1.txt

wait

echo -e "we can make a directory \"d\" as well as the subdirectory \"d/e\" using the \"mkdir\" command\n\n$dir mkdir d\n$dir mkdir d/e"

wait

mkdir d
mkdir d/e

echo -e "we can create a blank txt file in the subdirectory with \n\n$dir touch d/e/1.txt"

wait

touch d/e/1.txt

echo -e "and verify the current tree of our directory with \"tree -a\"\n\n$dir tree -a"

wait

tree -a

wait

echo -e "we can delete a file with the \"rm\" command, for example\n\n$dir rm d/e/1.txt"

wait

rm d/e/1.txt

echo -e "lets check the tree\n\n$dir$ tree -a"

wait

tree -a

wait

echo -e "note that \"rm\" attempts to remove files and not directories as default - we can append the \"-rf\" flag to remove directories, for example \n\n$dir rm -rf d"

rm -rf d

wait

echo -e "lets check the tree\n\n$dir tree -a"

wait

tree -a

wait

exit 0