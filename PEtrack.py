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
import json

OS_NAME = sys.platform
PATH = None

#Checking the platform and create the required folder correspondigly if not exist
if 'win' in OS_NAME:
	if not os.path.exists('Activity'):
		os.makedirs('Activity')
	PATH = os.getcwd() + '\\Activity\\'

else:
	if not os.path.exists('Activity'):
		os.makedirs('Activity')
	PATH = os.getcwd() + '/Activity/'


#Defining the banner
def banner():
	print(Fore.RED)
	os.system('figlet -f smslant PE-Tracker')
	print(Style.RESET_ALL)
	print('\033[1m' + '┌──────────────────────────────────────┐' + '\033[0m')
	print('\033[1m' + '│++++ You are your own rule maker. ++++│' + '\033[0m')
	print('\033[1m' + '└──────────────────────────────────────┘' + '\033[0m')
	print('\033[1m' + '\n[*] Starting Performance Enhancer modules...\n' + '\033[0m')


#Defining the usage help
def usage():
	parser = argparse.ArgumentParser(description = """Title: Performance Enhancer and Tracker
		\nAuthor: Parag Thakur (aka Virag)
		\nTwitter Handle: @_virag007
		\nDescription: It is a self-competitive CLI tool written in python that will enhance your performance by keeping track of the threshold you set. You can also add your competitor with whom you want to compete. It will generate weekly and monthly leaderboards as well. You can take a challenge of (say 30 days), set your threshold, and start tracking your daily progress. By the end of your resolution, you\'ll see a better you (mark it)""", formatter_class = argparse.RawTextHelpFormatter, usage = 'use "%(prog)s --help" for more information')

	parser.add_argument('--version', action = 'version', version = '%(prog)s v1.0 (Beta)', help = 'Shows the version information and exit')
	args = parser.parse_args()


#Creating the template of attributes
def create_template(attrib):
	attrib_dict = {}
	participants_dict = {}

	#Converting the list into dictionary data structure
	for attributes in range(1, len(attrib)):
		attrib_dict[attrib[attributes]] = 0

	for participants in attrib[0]:
		participants_dict[participants] = attrib_dict

	#Write it to JSON file
	with open(PATH + 'template.json', 'w') as outfile:
		json.dump(participants_dict, outfile)

	set_threshold()


#Setting the threshold
def set_threshold():
	json_file = open(PATH + 'template.json', 'r')
	json_data = json.load(json_file)
	json_file.close()

	keys = list(json_data)
	print('Enter the thresholds: ')

	attrib_dict = {}
	threshold_dict = {}
	for attributes in json_data[keys[-1]]:
		print(attributes + ': ', end = '')
		attrib_dict[attributes] = int(input())

	threshold_dict['Threshold'] = attrib_dict
	
	with open(PATH + 'threshold.json', 'w') as outfile:
		json.dump(threshold_dict, outfile)

	set_tracks()


#Set your tracks
def set_tracks():
	template_file = open(PATH + 'template.json', 'r')
	template_data = json.load(template_file)
	template_file.close()

	threshold_file = open(PATH + 'threshold.json', 'r')
	threshold_data = json.load(threshold_file)
	threshold_file.close()

	keys = list(template_data)
	keys.pop()

	track_dict = {}
	for participants in keys:
		attrib_dict = {}
		print(f'Enter your today track {participants}: ')
		for attributes in template_data[participants]:
			if(attributes == 'NumberOfDays'):
				attrib_dict[attributes] = threshold_data['Threshold']['NumberOfDays']
				continue
			print(attributes + ': ', end = '')
			attrib_dict[attributes] = int(input())

		track_dict[participants] = attrib_dict

	with open(PATH + 'activity.json', 'a+') as outfile:
		json.dump(track_dict, outfile)


	option = 'Y'
	print('Do you want to see entered stats (Y/N): ', end = '')
	option = input()

	if(option.lower() == 'y'):
		display(track_dict, threshold_data)


#Display stats to terminal
def display(track_dict, threshold_data):
	threshold_list = list(threshold_data)
	track_list = list(track_dict)
	dash = '─' * 28

	print('┌' + dash + '┐')
	print('\033[1m' + '{:^30}'.format(threshold_list[0]) + '\033[0m')
	print('├' + dash + '┤')

	for attributes in threshold_data[threshold_list[0]]:
		print('{:^30}'.format(attributes + ': ' + str(threshold_data[threshold_list[0]][attributes])))

	print('└' + dash + '┘')


	for participants in track_list:
		print('┌' + dash + '┐')
		print('\033[1m' + '{:^30}'.format(participants) + '\033[0m')
		print('├' + dash + '┤')

		for attributes in track_dict[participants]:
			print('{:^30}'.format(attributes + ': ' + str(track_dict[participants][attributes])))

		print('└' + dash + '┘')


#Menu-Driven program
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
				attrib.append('NumberOfDays')

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
				attrib.append('NumberOfDays')

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
		set_tracks()
	

#Main function
def main():
	usage()
	banner()
	menu()

if __name__ == '__main__':
	main()