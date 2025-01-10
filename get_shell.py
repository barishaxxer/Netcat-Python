import select
import argparse
import os
import NOP
import subprocess
import sys

def init_argparse():

	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
				description='Simple Bind Shell in python',
				epilog='''https://github.com/barishaxxer
usage:\n 
bind shell: 
bind -l -p 1337''')
	parser.add_argument('-l', '--listen', action='store_true', required=False)
	parser.add_argument('-e', '--exec', required=False)
	parser.add_argument('-p', '--port', type=int)
	parser.add_argument('-i', '--ip')
	return parser.parse_args()

def is_windows():
	return hasattr(sys, 'getwindowsversion')
def execute(command):
	output = "\n"
	shell_type = ['/bin/bash', '-i']
	if is_windows():
		shell_type = [r'C:\Windows\System32\cmd.exe']
	interactive_shell = subprocess.Popen(shell_type, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	if command:
		output = interactive_shell.communicate(input=command.encode())[0]
	return output
		
			

def main():

	

	args = init_argparse()
	
	nc = NOP.NOP(args)
	nc.run()
if __name__ == '__main__':
	main()
