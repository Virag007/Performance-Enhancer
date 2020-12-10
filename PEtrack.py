import os
from colorama import Fore, Style

def banner():
	print(Fore.RED)
	os.system('figlet -f smslant PE-Tracker')
	print(Style.RESET_ALL)
	print('\033[1m' + '[*] Starting Performance Enhancer modules...' + '\033[0m')
	print()

def menu():
	choice = int(input('Enter your choice: '))
	print('1. Compete with yourself')
	print('2. Compete with your friend')
	print('3. Exit')
	
	while(choice != 3):
		if(choice == 1):
			print('Com')
			break
		elif(choice == 2):
			print('com1')
			break
		elif(choice == 3):
			print('Exitting...')
			break
		else:
			print('Enter right choice...')
			break
	

def main():
	banner()
	menu()

if __name__ == '__main__':
	main()