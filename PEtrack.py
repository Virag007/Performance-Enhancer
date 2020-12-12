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
import datetime

OS_NAME = sys.platform
PATH = None
DATE = datetime.datetime.now()

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

	parser.add_argument('-f', '--flush', action = 'store_true', help = 'Wipe out the previous activities and exit')
	parser.add_argument('--version', action = 'version', version = '%(prog)s v1.0 (Beta)', help = 'Shows the version information and exit')
	args = parser.parse_args()
	return args


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
		json.dump(participants_dict, outfile, indent = 2)

	set_threshold()


#Setting the threshold
def set_threshold():
	template_data = fetch_template()

	#Storing the participants into list
	keys = list(template_data)
	print('\nEnter the thresholds: ')

	attrib_dict = {}
	threshold_dict = {}

	#Setting the threshold values
	for attributes in template_data[keys[-1]]:
		if(attributes == 'Date'):
			attrib_dict[attributes] = DATE.strftime("%a, %d-%b-%Y")
			continue

		elif(attributes == 'Time'):
			attrib_dict[attributes] = DATE.strftime("%X %P")
			continue

		else:
			print(attributes + ': ', end = '')
			attrib_dict[attributes] = int(input())

	threshold_dict['Threshold'] = attrib_dict
	
	#Writing the threshold key value pairs into json object file
	with open(PATH + 'threshold.json', 'w') as outfile:
		json.dump(threshold_dict, outfile, indent = 2)

	set_tracks(threshold_dict['Threshold']['NumberOfDays'] - 1)


#Set your tracks
def set_tracks(NOD):
	template_data = fetch_template()
	threshold_data = fetch_threshold()

	#Storing the participants into list and deleting the last value i.e., Threshold
	keys = list(template_data)
	keys.pop()

	track_dict = {}

	#Setting the daily stats
	for participants in keys:
		attrib_dict = {}
		print('\nEnter your Day-' + str(threshold_data['Threshold']['NumberOfDays'] - NOD) + ' track ' + participants + ': ')
		for attributes in template_data[participants]:
			if(attributes == 'NumberOfDays'):
				attrib_dict[attributes] = NOD
				continue

			elif(attributes == 'Date'):
				attrib_dict[attributes] = DATE.strftime("%a, %d-%b-%Y")
				continue

			elif(attributes == 'Time'):
				attrib_dict[attributes] = DATE.strftime("%X %P")
				continue

			else:
				print(attributes + ': ', end = '')
				attrib_dict[attributes] = int(input())

		track_dict[participants] = attrib_dict

	#Writing the activity data to the Json file
	with open(PATH + 'activity.json', 'a+') as outfile:
		json.dump(track_dict, outfile)
		outfile.write('\n')


	print('\nDo you want to see entered stats (Y/N): ', end = '')
	option = input()

	#Displaying the stats to the terminal
	if(option.lower() == 'y'):
		display(track_dict, threshold_data)


#Fetch Templete Data
def fetch_template():
	template_file = open(PATH + 'template.json', 'r')
	template_data = json.load(template_file)
	template_file.close()
	return template_data

#Fetch Threshold Data
def fetch_threshold():
	threshold_file = open(PATH + 'threshold.json', 'r')
	threshold_data = json.load(threshold_file)
	threshold_file.close()
	return threshold_data

#Fetch Activity Data
def fetch_activity():
	activityList = []

	#Activity file contains multiple Json data object
	for jsonObj in open(PATH + 'activity.json', 'r'):
		activityDict = json.loads(jsonObj)
		activityList.append(activityDict)
	
	return activityList

#Display stats to terminal
def display(track_dict, threshold_data):
	threshold_list = list(threshold_data)
	track_list = list(track_dict)
	dash = '─' * 28

	#Displaying the Threshold table to the terminal
	print('\n┌' + dash + '┐')
	print('\033[1m' + '{:^30}'.format(threshold_list[0]) + '\033[0m')
	print('├' + dash + '┤')

	for attributes in threshold_data[threshold_list[0]]:
		print('{:^30}'.format(attributes + ': ' + str(threshold_data[threshold_list[0]][attributes])))

	print('└' + dash + '┘')

	#Displaying the participants table to the terminal
	for participants in track_list:
		print('┌' + dash + '┐')
		print('\033[1m' + '{:^30}'.format(participants) + '\033[0m')
		print('├' + dash + '┤')

		for attributes in track_dict[participants]:
			print('{:^30}'.format(attributes + ': ' + str(track_dict[participants][attributes])))

		print('└' + dash + '┘')


#End day statistics build and display to the terminal
def stats_build():
	print('Nice Job')
	#display()


#Menu-Driven program
def menu():
	if not os.path.exists(PATH + 'template.json'):
		print('1. Compete with yourself')
		print('2. Compete with your friend')
		print('3. Exit')

		try:
			print(Fore.GREEN)
			choice = int(input('Enter your choice: '))

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
					attrib.append('Date')
					attrib.append('Time')

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
					attrib.append('Date')
					attrib.append('Time')

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

		except:
			print(Style.RESET_ALL)
			print('Enter only integer value')

	else:
		threshold_data = fetch_threshold()
		activity_data = fetch_activity()
		activity_list = list(activity_data[0])
		NOD = activity_data[len(activity_data) - 1][activity_list[0]]['NumberOfDays']
		print('Do you want to see last day stats (Y/N): ', end = '')
		option = input()
		
		if(option.lower() == 'y'):			
			display(activity_data[len(activity_data) - 1], threshold_data)

			print('Do you want to enter your todays stat (Y/N): ', end = '')
			today_stat = input()

			if(today_stat.lower() == 'y'):

				if(NOD == 0):
					print('\n\033[1m' + 'Congratulations, You\'ve completed your resolution successfully' + '\033[0m')
					print('Now you can view your progress')
					stats_build()

				else:
					if(activity_data[len(activity_data) - 1][activity_list[0]]['Date'] != DATE.strftime("%a, %d-%b-%Y")):
						set_tracks(NOD - 1)
					else:
						print('\n\033[1m' + 'You have set the stats already for the day.' + '\033[0m')

			elif(today_stat.lower() == 'n'):
				print('Good Day')

			else:
				print('Choose among Y-(Yes) or N-(No) only')

		elif(option.lower() == 'n'):
			print('Do you want to enter your todays stat (Y/N): ', end = '')
			today_stat = input()

			if(today_stat.lower() == 'y'):

				if(NOD == 0):
					print('\n\033[1m' + 'Congratulations, You\'ve completed your resolution successfully' + '\033[0m')
					print('Now you can view your progress')
					stats_build()

				else:
					if(activity_data[0][activity_list[0]]['Date'] != DATE.strftime("%a, %d-%b-%Y")):
						set_tracks(NOD - 1)
					else:
						print('\n\033[1m' + 'You have set the stats already for the day.' + '\033[0m')

			elif(today_stat.lower() == 'n'):
				print('Good Day')

			else:
				print('Choose among Y-(Yes) or N-(No) only')

		else:
			print('Choose among Y-(Yes) or N-(No) only')
	

#Main function
def main():
	args = usage()
	if args.flush:
		os.system('rm -r ' + PATH + '*')
		print('All activity files flushed.\n')
		return

	banner()
	menu()

if __name__ == '__main__':
	main()