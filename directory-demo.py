def directory():
    
    if 'directory' in os.listdir():
        rmtree('directory')

    os.mkdir('directory')
    os.chdir('directory')

    for folder in ['a', 'b', '.c']:
        os.mkdir(folder)

    folder_files = {'a' : range(1, 4), 'b' : range(1, 3), '.c' : [2]}

    for folder, files in folder_files.items():
        for file in files:
            with open(f'{folder}/{file}.txt', 'w') as f:
                f.write(f'contents of file "{file}" in folder "{folder}"\n')
    
    os.chdir('..')

def _continue(command):
    commands = 'cd', 'mkdir', 'touch', 'rm'
    if 'cd' in command:
        os.chdir(command.split()[1])
    if 'rm' in command:
        print()
    return any(s in command for s in commands)


if __name__ == '__main__':

    from   base   import execute, pwd, simulate, wait

    from   shutil import rmtree
    import os

    directory()

    simulate('# for this tutorial, the typing is simulated for you so only press ENTER when prompted')
    print()
    wait()

    simulate('# the main commands we will look at in this tutorial are')

    commands = ['pwd', 'ls', 'cd', 'tree', 'rm']
    descs    = ['prints the current working directory',
                'prints the directories and files within a given directory (default is the current directory)',
                'changes the directory relative to the current one (absolute paths start with a "/")',
                'prints the directory tree',
                'removes objects (files only by default)']

    for command, desc in zip(commands, descs):
        simulate(f'# {command}')
        simulate(f'#     {desc}', pause = 1.5)
        print()

    print()

    commands = ['pwd', 'ls', 'cd directory', 'pwd', 'tree -a', 'ls', 'ls -all', 'cat a/1.txt', 'mkdir d', 'mkdir d/e', 'touch d/e/1.txt', 'tree -a', 
                'rm d/e/1.txt', 'tree -a', 'rm d', 'rm -rf d', 'tree -a']

    echoes   = ['lets print the current working directory with the command "pwd"',
                'lets print all files and folders in the current directory with "ls"',
                f'lets change our directory to {pwd("directory")}',
                'lets verify we have changed directory using "pwd"',
                'we can examine the directory tree by using the command "tree -a"',
                [
                    'we know there are three folders in our current directory from the previous execution of "tree -a"',
                    'lets verify this by using the command "ls"'
                ],
                [
                    'notice how the ".c" folder is missing?',
                    'this is because files and folders that start with a "." are hidden',
                    'we can tell "ls" to show hidden objects by the following command "ls -all"'
                ],
                'we can print text files to the terminal using the command "cat"',
                'we can create a directory using the command "mkdir"',
                'we can also create a subdirectory using the command "mkdir"',
                'to create a blank text file we use the command "touch"',
                'lets verify the creation of our directories "d" and "d/e" as well as the new file "d/e/1.txt" using "tree -a"',
                'we can delete a file with the "rm" command',
                'lets verify "d/e/1.txt" has been deleted with the "tree -a" command',
                'lets try deleting the directory "d"',
                [
                    'we see that we cannot delete a directory by default',
                    'to do so we need to execute "rm -rf"'
                ],
                'lets verify the directory "d" has been deleted with "tree -a"',
                [
                    'if you do not know how to use a command we can flag "--help" at the end of any command',
                    'for example lets see the help documentation for "rm"'
                ]
               ]

    for command, echo in zip(commands, echoes):
        
        if isinstance(echo, list):
            for e in echo:
                simulate(f'# {e}', pause = 0.5)
        else:
            simulate(f'# {echo}')

        simulate(command)
        print()
        wait()
        execute(command)

        if _continue(command):
            continue

        print()
        wait()
