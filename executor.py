from parsers import parse_command
import subprocess
from builtin import handle_builtin

def execute_command(command):
    tokens = parse_command(command)
    if handle_builtin(tokens):
        return
    try:
        subprocess.run(tokens)
    except FileNotFoundError:
        print(f"Command not found: {tokens[0]}")