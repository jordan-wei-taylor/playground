# Playground

<br>

This repository is designed for my students under CM50175 providing a simple tutorial in directory manipulation and virtual python environments.

To run through this tutorial open a bash terminal and first execute the following

```console
user@device:~$ git clone https://github.com/jordan-wei-taylor/playground.git; cd playground
```

and ensure the bash script files (.sh) have been given the rights to be executable by executing

```console
user@device:~$ chmod 777 *.sh
```

To execute the bash files, please first ensure the commands `tree` and `python3` work. If both do not work install them using the command

```console
user@device:~$ sudo apt install tree python3.x python3.x-venv
```

or to install only `tree`

```console
user@device:~$ sudo apt install tree
```

or to install only python3 with virtual environment

```console
user@device:~$ sudo apt install python3.x python3.x-venv
```

where `x` should be an integer. For example, on Ubuntu 20.04, python3.8 is the supported version of python3 and on Ubuntu 22.04, python3.10 is the supported version.

The user should execute `directory.sh` by

```console
user@device:~$ ./directory.sh
```

then go through the directory demo

```console
user@device:~$ ./directory-demo.sh
```

Once the user has completed it, they are recommended to practice some of the commands. Upon feeling more comfortable the user should execute

```console
user@device:~$ ./script.sh
```

and attempt to show the help documentation of the newly generated `script.py`

```console
user@device:~$ python3 -m script --help
```

and follow the debugging text until it can successfully run.

<br>

We will go through how to use the University of Bath's hex cluster in our next meeting but please do ensure you can all sign in with

```console
user@device:~$ ssh <username>@ogg.cs.bath.ac.uk
```

for example, I would execute

```console
user@device:~$ ssh jt2006@ogg.cs.bath.ac.uk
```

and enter your password (note it does not show). If you cannot successfully sign in, please email Tom Haines requesting access.