import shlex
import argparse
import sys
import subprocess
def init_argparse():

	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
				description='Simple implementation of netcat in python',
				epilog='''https://github.com/barishaxxer
usage:\n 
connect to somewhere:
nc [options] hostname port\n
reverse shell: 
nc hostname port -e [shell]''')
	parser.add_argument('-l', '--listen', action='store_true', required=False)
	parser.add_argument('-e', '--exec', required=False)
	return parser.parse_args()

def is_windows():
	return hasattr(sys, 'getwindowsversion')
def execute(command):
	shell_type = ['/bin/bash', '-i']
	if is_windows():
		shell_type = [r'C:\Windows\System32\cmd.exe']
		
	interactive_shell = subprocess.Popen(shell_type, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	if command == "exit":
		sys.exit("Bye")
	if command:
		output = interactive_shell.communicate(input=command.encode())
		print(output[0])
			

def main():

	args = init_argparse()
	execute("cd ~/Documents/python_networking")
	execute("pwd")
if __name__ == '__main__':
	main()
