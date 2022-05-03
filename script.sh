#!/bin/bash

if [ -f requirements.txt ]
then
    echo "demo files already exist"
    exit 0
fi

echo -e "numpy==1.22.3\n" >> requirements.txt
echo -e "def main(n, t, v):\n\tfrom time import sleep\n\n\ttry:\n\t\timport numpy\n\texcept:\n\t\traise ImportError('could not import numpy!')\n\n\tfor i in range(1, n + 1):\n\t\tsleep(t)" >> script.py
echo -en "\t\t" >> script.py
echo "print(f'\\riteration {i}', end = ['\\n',''][i % v > 0])" >> script.py
echo -e "\n\t\nif __name__ == '__main__':\n\n\timport argparse\n\t\n\timport json\n\timport os\n\n\tif 'env' not in os.listdir():\n\t\tfor line in ['virtual python environment not detected!', '', 'try the following command:', '\tpython3 -m venv env', '', \n\t\t\t\t\t 'then activate with', '\tsource env/bin/activate']:\n\t\t\tprint(line)\n\t\texit()\n\n\tpy\t = os.path.basename(__file__)\n\tparser = argparse.ArgumentParser('example script')\n\n\tparser.add_argument('n' , type = int  , help = 'number of iterations')\n\tparser.add_argument('-t', type = float, help = 'time in seconds', default = 0.5)\n\tparser.add_argument('-v', type = int  , help = 'verbosity'\t  , default = 10)\n\n\targs = parser.parse_args()\n\t\n\tprint(f'executing {py} with parameters:')\n\tprint(json.dumps(dict(args._get_kwargs()), indent = 4))\n\n\tmain(args.n, args.t, args.v)\n\n\tprint(f'executed {py}')\n" >> script.py

echo "created demo files"
