import subprocess
from builtin import handle_builtin
from parsers import parse_command

def is_ai_query(command):
    return command.strip().startswith("@axon")

def extract_ai_query(command):
    return command.strip()[6:].strip()

def ai_suggest_command(query):
    query = query.lower()
    task_map = {
        "list files": "ls",
        "show current directory": "pwd",
        "create folder": "mkdir",
        "remove file": "rm",
        "delete folder": "rm -r",
        "create file": "touch",
        "read file": "cat",
        "show date": "date",
        "change directory": "cd"
    }
    for task, cmd in task_map.items():
        if task in query:
            return f"Try: {cmd} [args]"
    return "Sorry, I couldn't find a matching command."

def handle_ai_query(command):
    query = extract_ai_query(command)
    response = ai_suggest_command(query)
    print(response)

def execute_command(command):
    if is_ai_query(command):
        handle_ai_query(command)
        return

    tokens = parse_command(command)
    if handle_builtin(tokens):
        return

    try:
        subprocess.run(tokens)
    except FileNotFoundError:
        print(f"Command not found: {tokens[0]}")
