import os

def handle_builtin(tokens):
    cmd = tokens[0]
    if cmd == "cd":
        try:
            os.chdir(tokens[1])
        except IndexError:
            print("Usage: cd <directory>")
        except FileNotFoundError:
            print(f"No such directory: {tokens[1]}")
        return True
    elif cmd == "exit":
        return True
    return False
