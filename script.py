import time

def main(n, t, v):
	
	if 'env' not in os.listdir():
		print(msg2)
		exit()

	if sys.executable.startswith('/usr'):
		print(msg3)
		exit()

	try:
		import numpy
	except:
		print(msg1)
		exit()

	for i in range(1, n + 1):
		time.sleep(t)
		print(f'\riteration {i}', end = ['\n',''][i % v > 0])

msg1 = '''Most GitHub repositories will have a "requirements.txt" which lists all the python dependencies. For this simple demo, our only requirement is numpy. We can either install it manually with

	pip install numpy

or install every package listed in "requirements.txt" with

	pip install -r requirements.txt

After installing required package(s), try running this script again'''

msg2 = '''Virtual python environment not detected!

Try the following command:

	python3 -m venv env

then activate with

	source env/bin/activate

and try running this script again
'''

msg3 = '''Virtual python environment not activated!

Try the following command:

	source env/bin/activate

and try running this script again
'''

description = r'''Example script

Given number of iterations, n, time in seconds, t, and verbosity, v, performs n iterations of sleep(t) with verbose updates.
If the current iteration is divisible by v, prints a new line, otherwise, prints inplace.

Usage
=======

python -m script n [-t T] [-v V]

where n, T, and V are of type integer, float and integer respectively. T and V are optional parameters and have default values of 0.5 and 10.

Example
=======

python -m script 20 -t 0.5 -v 10
'''

if __name__ == '__main__':

	import argparse
	
	import json
	import sys
	import os


	py	   = os.path.basename(__file__)
	parser = argparse.ArgumentParser(description, formatter_class = argparse.RawTextHelpFormatter)

	parser.add_argument('n' , type = int  , help = 'number of iterations')
	parser.add_argument('-t', type = float, help = 'time in seconds', default = 0.5)
	parser.add_argument('-v', type = int  , help = 'verbosity', default = 10)

	args   = parser.parse_args()
	
	print(f'executing {py} with parameters:')
	print(json.dumps(dict(args._get_kwargs()), indent = 4))

	main(args.n, args.t, args.v)

	print(f'executed {py}')

