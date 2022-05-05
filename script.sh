#!/bin/bash

if [[ -f requirements.txt && -f script.py ]]
then
    echo "demo files already exist"
    exit 0
fi

for file in requirements.txt script.py
do
    if [ -f $file ]
    then
        echo "detected \"$file\" so removed it!"
        rm $file
    fi
done

echo -e "numpy==1.22.3\n" >> requirements.txt
echo -en "def main(n, t, v):\n\t\n\ttry:\n\t\timport numpy\n\texcept:\n\t\tprint(msg1)\n\t\texit()\n\n\tfor i in range(1, n + 1):\n\t\ttime.sleep(t)\n\t\t" >> script.py
echo "print(f'\\riteration {i}', end = ['\\n',''][i % v > 0])" >> script.py
echo -e "\nmsg1 = '''Most GitHub repositories will have a \"requirements.txt\" which lists all the python dependencies. For this simple demo, our only requirement is numpy. We can either install it manually with\n\n\tpip install numpy\n\nor install every package listed in \"requirements.txt\" with\n\n\tpip install -r requirements.txt\n\nAfter installing required package(s), try running this script again'''\n\nmsg2 = '''Virtual python environment not detected!\n\nTry the following command:\n\n\tpython3 -m venv env\n\nthen activate with\n\n\tsource env/bin/activate\n\nand try running this script again\n'''\n\nmsg3 = '''Virtual python environment not activated!\n\nTry the following command:\n\n\tsource env/bin/activate\n\nand try running this script again\n'''\n\nif __name__ == '__main__':\n\n\timport argparse\n\t\n\timport time\n\timport json\n\timport sys\n\timport os\n\n\tif 'env' not in os.listdir():\n\t\tprint(msg2)\n\t\texit()\n\n\tif 'env/lib' not in sys.path[-1]:\n\t\tprint(msg3)\n\t\texit()\n\t\n\tdescription = r'''Example script\n\n\tGiven number of iterations, n, time in seconds, t, and verbosity, v, performs n iterations of sleep(t) with verbose updates.\n\tIf the current iteration is divisible by v, prints a new line, otherwise, prints inplace.\n\n\tUsage\n\t=======\n\n\tpython -m script n [-t T] [-v V]\n\n\twhere n, T, and V are of type integer, float and integer respectively. T and V are optional parameters and have default values of 0.5 and 10.\n\n\tExample\n\t=======\n\n\tpython -m script 20 -t 0.5 -v 4\n\t'''\n\n\tpy\t   = os.path.basename(__file__)\n\tparser = argparse.ArgumentParser(description, formatter_class = argparse.RawTextHelpFormatter)\n\n\tparser.add_argument('n' , type = int  , help = 'number of iterations')\n\tparser.add_argument('-t', type = float, help = 'time in seconds', default = 0.5)\n\tparser.add_argument('-v', type = int  , help = 'verbosity', default = 10)\n\n\targs   = parser.parse_args()\n\t\n\tprint(f'executing {py} with parameters:')\n\tprint(json.dumps(dict(args._get_kwargs()), indent = 4))\n\n\tmain(args.n, args.t, args.v)\n\n\tprint(f'executed {py}')\n" >> script.py

echo "created demo files"
