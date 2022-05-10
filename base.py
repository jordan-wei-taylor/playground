import os, sys, time

_activated = False

def activate(name):
    global _activated
    _activated = name

def deactivate():
    global _activated
    _activated = False

def activated():
    global _activated
    if _activated:
        return f'({_activated}) '
    interpreter = sys.executable
    if interpreter.startswith('/usr'):
        return ''
    return f"({interpreter.split('/')[-3]}) "

def pwd(path = ''):
    home  = os.path.expanduser('~')
    full  = os.path.join(os.path.abspath('.'), path).replace(home, '~')

    if full.endswith('/'):
        full = full[:-1]

    return full

def user(path = ''):
    left  = f"{activated()}\033[1m\033[92m{os.getlogin()}@{os.uname().nodename}\033[0m"
    right = f"\033[1m\033[34m{pwd(path)}\033[0m"
    return f'{left}:{right}$ '

def write(text, delay = 0.03):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)

def simulate(text, path = '', newline = True, backspace = False, pause = 0, delay = 0.03):

    if backspace:
        newline = False
        
    write(user(path), 0)

    for tex in text:
        write(tex, delay)
        
    time.sleep(pause)

    if backspace:

        for tex in text:
            write('\b \b', delay)

    if newline:
        print()
    
def execute(command):
    os.system(command)

def wait():
    input("[Press ENTER to continue]")
    print('\033[F\033[K\r', end = '')
