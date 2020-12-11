#!/usr/bin/env python

########################################
## Author: Parag Thakur (aka Virag)
## Follow: @_virag007
## Licence: MIT
## Copyright: Copyright 2020, PETracker
## Title: Performance Enhancer & Tracker
## About: CLI Tool
########################################

import os
from colorama import Fore, Style
import sys
import argparse

OS_NAME = sys.platform
PATH = None

if 'win' in OS_NAME:
	if not os.path.exists('Activity'):
		os.makedirs('Activity')
	PATH = os.getcwd() + '\\Activity\\'

else:
	if not os.path.exists('Activity'):
		os.makedirs('Activity')
	PATH = os.getcwd() + '/Activity/'

def banner():
	print(Fore.RED)
	os.system('figlet -f smslant PE-Tracker')
	print(Style.RESET_ALL)
	print('\033[1m' + '┌──────────────────────────────────────┐' + '\033[0m')
	print('\033[1m' + '│++++ You are your own rule maker. ++++│' + '\033[0m')
	print('\033[1m' + '└──────────────────────────────────────┘' + '\033[0m')
	print('\033[1m' + '\n[*] Starting Performance Enhancer modules...\n' + '\033[0m')

def usage():
	parser = argparse.ArgumentParser(description = """Title: Performance Enhancer and Tracker
		\nAuthor: Parag Thakur (aka Virag)
		\nTwitter Handle: @_virag007
		\nDescription: It is a self-competitive CLI tool written in python that will enhance your performance by keeping track of the threshold you set. You can also add your competitor with whom you want to compete. It will generate weekly and monthly leaderboards as well. You can take a challenge of (say 30 days), set your threshold, and start tracking your daily progress. By the end of your resolution, you\'ll see a better you (mark it).This is the help window""", formatter_class = argparse.RawTextHelpFormatter, usage = 'use "%(prog)s --help" for more information')

	parser.add_argument('--version', action = 'version', version = '%(prog)s v1.0 (Beta)', help = 'Shows the version information and exit')
	args = parser.parse_args()

def create_template(attrib):
	attrib_dict = {}
	participants_dict = {}
	print(attrib)

	for attributes in range(1, len(attrib)):
		attrib_dict[attrib[attributes]] = 0

	for participants in attrib[0]:
		participants_dict[participants] = attrib_dict

	print(participants_dict)



def menu():
	if not os.path.exists(PATH + 'template.json'):
		print('1. Compete with yourself')
		print('2. Compete with your friend')
		print('3. Exit')

		print(Fore.GREEN)
		choice = int(input('Enter your choice: '))
		print(Style.RESET_ALL)

		while(choice != 3):
			if(choice == 1):
				participants = []
				your_name = input('What\'s your name: ')
				participants.append(your_name)
				participants.append('Threshold')
				print('Create your template\n')
				print('Name your attributes--')
				attrib = []
				attrib.append(participants)

				termination = ''
				while(termination.lower() != 'exit'):
					termination = input()
					attrib.append(termination)

				attrib.pop()
				create_template(attrib)
				break

			elif(choice == 2):
				participants = []
				your_name = input('What\'s your name: ')
				participants.append(your_name)
				friend_name = input('What\'s your friend name: ')
				participants.append(friend_name)
				participants.append('Threshold')
				print('Create your template\n')
				print('Name your attributes--')
				attrib = []
				attrib.append(participants)

				termination = ''
				while(termination.lower() != 'exit'):
					termination = input()
					attrib.append(termination)

				attrib.pop()
				create_template(attrib)
				break

			elif(choice == 3):
				print('Exitting...')
				break

			else:
				print('Enter right choice...')
				break

	else:
		print("Adding existing")
	

def main():
	usage()
	banner()
	menu()

if __name__ == '__main__':
	main()