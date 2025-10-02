import os
from executor import execute_command

def main():
    print("Welcome to Axon Core")
    while True:
        try:
            command = input("\033[1;31mAxon Core>> \033[0m") #Red, bold text
            if command.lower() in ["exit", "quit", "stop"]:
                print("Exiting Axon Core...")
                break
            elif command.lower()=="about":
                print("Axon Core was created as a part of the OS project in 2025.\nIt is a custom shell that created for the ease of the user.")
                continue
            elif len(command)==0:
                continue
            elif command.lower()=="help":
                print("Available commands:")
                print("help                 Show this help message")
                print("exit/quit/stop       Exit the shell")
                print("about                Learn about Axon Core")
                print("clear                Clear the screen")
                print("cd                   Change directory")
                print("pwd                  Show current directory")
                print("echo                 Print messages")
                print("<command>            Run external commands")
            elif "echo" in command:
                print(command[5:])
            elif command=="pwd":
                print(os.getcwd())
            elif command=="clear":
                for i in range(40):
                    print("\n")
            else:
                execute_command(command)
        except KeyboardInterrupt:
            print("Exiting Axon Core...")
            break
        except Exception:
            print("An error occurred. Please try again.")

main()