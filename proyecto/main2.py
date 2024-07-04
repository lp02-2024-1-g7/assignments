import subprocess

# Example with xterm
command = ['xterm', '-e', 'bash', '-c', 'source ../venv/bin/activate && python main.py input01.txt; exec bash']
subprocess.run(command)

# Example with gnome-terminal
# command = ['gnome-terminal', '--', 'bash', '-c', 'source /path/to/venv/bin/activate && echo "Hello, World!"; exec bash']
# subprocess.run(command)
