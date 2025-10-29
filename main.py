import os
from executor import execute_command
from history import Command_History
history=Command_History()

def main():
    print("Welcome to Axon Core...")
    while True:
        try:
            command = input("\033[1;31mAxon Core>> \033[0m") #Red, bold text
            history.add(command)
            if command.lower() in ["exit", "quit", "stop"]:
                print("Exiting Axon Core...")
                break
            elif command.lower()=="about":
                print("Axon Core was created as a part of the OS project in 2025.\nIt is a custom shell that was created for the ease of the user.")
                continue
            elif len(command)==0:
                continue
            elif command.lower()=="help":
                print("Available commands:")
                print("help                 Show this help message")
                print("exit/quit/stop       Exit the shell")
                print("about                Learn about Axon Core")
                print("clear                Clear the screen")
                print("cd <dir>             Change directory")
                print("pwd                  Show current directory")
                print("ls [dir]             List files in directory")
                print("mkdir <name>         Create a new directory")
                print("rm <file>            Remove file")
                print("rmdir <dir>          Remove empty directory")
                print("touch <file>         Create an empty file")
                print("cat <file>           Display file contents")
                print("head <file> [n]      Show first n lines (default 10)")
                print("tail <file> [n]      Show last n lines (default 10)")
                print("date                 Show current date")
                print("time                 Show current time")
                print("echo <message>       Print messages")
                print("<command>            Run external commands")
            elif command.lower() == "history":
                history.show()
            elif command.lower() == "history clear" or command.lower() == "clear history":
                history.clear()
            elif "echo" in command:
                print(command[5:])
            elif command.lower()=="pwd":
                print(os.getcwd())
            elif command.lower()=="clear":
                for i in range(40):
                    print("\n")
            elif command.lower()== "date and time" or command.lower()=="time and date":
                from datetime import datetime
                now = datetime.now()
                print("Date:", now.strftime("%Y-%m-%d"))
                print("Time:", now.strftime("%H:%M:%S"))
            else:
                execute_command(command)
        except KeyboardInterrupt:
            print("Exiting Axon Core...")
            break
        except Exception:
            print("An error occurred. Please try again.")

main()