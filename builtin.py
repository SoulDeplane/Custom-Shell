import os
import shutil
import datetime

def cmd_cd(args):
    try:
        os.chdir(args[0])
    except Exception as e:
        print(f"cd error: {e}")

def cmd_mkdir(args):
    try:
        os.mkdir(args[0])
    except Exception as e:
        print(f"mkdir error: {e}")

def cmd_rm(args):
    try:
        if os.path.isdir(args[0]):
            shutil.rmtree(args[0])
        else:
            os.remove(args[0])
    except Exception as e:
        print(f"rm error: {e}")

def cmd_touch(args):
    try:
        open(args[0], 'a').close()
    except Exception as e:
        print(f"touch error: {e}")

def cmd_ls(args):
    try:
        path = args[0] if args else '.'
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"ls error: {e}")

def cmd_pwd(args):
    print(os.getcwd())

def cmd_rmdir(args):
    try:
        os.rmdir(args[0])
    except Exception as e:
        print(f"rmdir error: {e}")

def cmd_cat(args):
    try:
        with open(args[0], 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"cat error: {e}")

def cmd_date(args):
    print(datetime.datetime.now().strftime("%Y-%m-%d"))
    
def cmd_time(args):
    print(datetime.datetime.now().strftime("%H:%M:%S"))

def cmd_head(args):
    try:
        filename = args[0]
        n = int(args[1]) if len(args) > 1 else 10
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= n:
                    break
                print(line.rstrip())
    except Exception as e:
        print(f"head error: {e}")

def cmd_tail(args):
    try:
        filename = args[0]
        n = int(args[1]) if len(args) > 1 else 10
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line.rstrip())
    except Exception as e:
        print(f"tail error: {e}")

def handle_builtin(tokens):
    if not tokens:
        return True
    cmd = tokens[0]
    args = tokens[1:]

    builtins = {
        "cd": cmd_cd,
        "mkdir": cmd_mkdir,
        "rm": cmd_rm,
        "touch": cmd_touch,
        "ls": cmd_ls,
        "pwd": cmd_pwd,
        "rmdir": cmd_rmdir,
        "cat": cmd_cat,
        "date": cmd_date,
        "time": cmd_time,
        "head": cmd_head,
        "tail": cmd_tail
    }

    if cmd in builtins:
        builtins[cmd](args)
        return True
    return False