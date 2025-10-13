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
    "show files": "ls",
    "display files": "ls",
    "list directory": "ls",
    "list contents": "ls",
    "show folder contents": "ls",
    "current directory": "pwd",
    "show current directory": "pwd",
    "where am i": "pwd",
    "show location": "pwd",
    "create folder": "mkdir",
    "new folder": "mkdir",
    "create directory": "mkdir",
    "new directory": "mkdir",
    "make directory": "mkdir",
    "build folder": "mkdir",
    "delete folder": "rmdir",
    "delete directory": "rmdir",
    "remove folder": "rmdir",
    "remove directory": "rmdir",
    "clean folder": "rmdir",
    "erase directory": "rmdir",
    "delete empty folder": "rmdir",
    "remove file": "rm",
    "delete file": "rm",
    "erase file": "rm",
    "delete item": "rm",
    "remove item": "rm",
    "clean file": "rm",
    "trash file": "rm",
    "create file": "touch",
    "make file": "touch",
    "new file": "touch",
    "read file": "cat",
    "open file": "cat",
    "view file": "cat",
    "print file": "cat",
    "show file": "cat",
    "inspect file": "cat",
    "file contents": "cat",
    "file preview": "head",
    "show first lines": "head",
    "first few lines": "head",
    "read beginning of file": "head",
    "lines from file": "head",
    "read lines": "head",
    "show last lines": "tail",
    "last few lines": "tail",
    "read end of file": "tail",
    "show date": "date",
    "what's the date": "date",
    "today's date": "date",
    "show time": "time",
    "current time": "time",
    "what time is it": "time",
    "system time": "time",
    "change directory": "cd",
    "go to": "cd",
    "navigate to": "cd",
    "enter folder": "cd",
    "change folder": "cd",
    "move to folder": "cd",
    "switch directory": "cd",
    "jump to": "cd",
    "how do i list files": "ls",
    "how to create folder": "mkdir",
    "how to delete file": "rm",
    "how to read file": "cat",
    "how to change directory": "cd"
}
    for task, cmd in task_map.items():
        if task in query:
            return f"Try: {cmd} <args>"
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
