import os

if __name__ == '__main__':

    from   base   import execute, simulate, wait, activate, deactivate

    simulate('# for this tutorial, the typing is simulated for you so only press ENTER when prompted')
    print()
    wait()

    simulate('# this tutorial aims to show you how to set up a virtual python environment')
    simulate('# a good GitHub repository will contain the desired package you wish to use as well as a "requirements.txt" file')
    simulate('# it is good practice to create a virtual python environment for each of your (GitHub) projects')
    simulate('# where each project specifies package dependencies in the "requirements.txt" file')
    
    print()

    simulate('# lets consider our "script.py"')
    simulate('# similar to bash commands, we can use the "--help" flag to print some form of documentation')

    print()
    simulate('python3 -m script --help')
    print()
    wait()
    
    execute('python3 -m script --help')

    simulate('# our example script requires 1 input "n" and 2 optional inputs "T" and "V" which require the flags "-t" and "-v"', pause = 2)
    simulate('# lets try executing script.py with "n=20"')
    print()
    simulate('python3 -m script 20')
    execute('python3 -m script 20')

    simulate('# there seems to be an error!')
    print()
    wait()
    simulate('# this script seems to require an (activated) virtual python environment')
    simulate('# lets create one with "python3 -m venv env')
    print()
    simulate('python3 -m venv env')
    wait()
    execute('python3 -m venv env')
    print()
    wait()
    print()
    simulate('# we should now have the subdirectory "env" within our current directory.')
    simulate('ls')
    wait()
    execute('ls')
    print()
    wait()
    simulate('# lets try running the script again with "n=20"')

    simulate('python3 -m script 20')
    print()
    wait()
    execute('python3 -m script 20')
    print()
    wait()

    simulate('# we seem to have forgotten to activate our function!')
    simulate('# this just means we use this python3 instead of the system\'s python3')

    simulate('source env/bin/activate')
    activate('env')

    wait()

    simulate('# note that we now have "(env)" at the start of the line', pause = 2)
    simulate('# this is to indicate that we are now using "env"\'s python3')
    simulate('# finally, lets re-run the script')

    print()
    simulate('python3 -m script 20')
    print()
    wait()
    execute('env/bin/python -m script 20')

    wait()

    simulate('# we seem to be missing the package "numpy"!', pause = 2)
    simulate('# what we have done so far is to create a blank version of python3 and use it', pause = 0.5)
    simulate('# we have not installed any package dependencies yet', pause = 0.5)
    simulate('# for this example, we only need to install numpy so we could do execute', pause = 0.5)
    simulate('# "pip3 install numpy"')

    wait()

    simulate('# but for larger packages with more dependencies it is easier to install using')
    simulate('# the "requirements.txt" file directly with "pip3 install -r requirements.txt"')

    wait()

    simulate('pip3 install -r requirements.txt')
    print()
    wait()
    execute('env/bin/pip install -r requirements.txt')
    print()
    wait()
    simulate('# finally lets try executing the script again with "n=20"')
    simulate('python3 -m script 20')
    print()
    wait()
    execute('env/bin/python -m script 20')

    wait()

    simulate('# great, we have managed to:', pause = 1)
    simulate('#    create a virtual python environment', pause = 1)
    simulate('#    activate it', pause = 1)
    simulate('#    install required dependencies')
    print()
    simulate('finally, we can deactivate the virtual python environment by executing')
    simulate('deactivate')
