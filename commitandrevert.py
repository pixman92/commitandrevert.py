#!/usr/bin/python

import sys
import subprocess
import pdb
import re

def main():
	# run the GIT LOG command
	subprocess.run(["git", "log", "--max-count=4"])

	while True:
		addingNewCommit = input("Please Commit now: ")
		if(len(addingNewCommit)>0):
			subprocess.run(['git', 'add', '.'])
			subprocess.run(['git', 'commit', '-m', str(addingNewCommit)])
			print ("Commit - done")
			break
		else:
			print("Try again")




	splitString = subprocess.check_output(["git", "log"])
	# to save the commit string into the variable
	pulledCommit = str(splitString)
	savedCommit = pulledCommit.split(" ")
	# print (savedCommit)


	rangeIndexBetween = pulledCommit.split(' ')[1]
	# print (rangeIndexBetween)

	# pdb.set_trace()

	# indexMe = savedCommit[1].index('\\')

	# indexMe = str(indexMe)
	# rangeIndexBetween = savedCommit[[0], [indexMe]]
	# indexArray = [[0], [40]]
	# rangeIndexBetween = indexMe[str(0),str(24)]

	lastIndex = rangeIndexBetween.index('A')
	# pdb.set_trace()
	rangeIndexBetween = rangeIndexBetween[0:lastIndex-2]
	# print(rangeIndexBetween)


	# pulling All Logs
	pattern = r"commit (\w+)"

	matches = re.findall(pattern, pulledCommit)
	# print("matches", matches)


	# print("\n\nRevert to this Previous Commit:?")
	# print(matches[1])



	# commitText = pulledCommit[1]
	# split the string an array
	# myString = "commit a20a73e6656fb6be6d912f5131d978f1596309e9 Author: Christian <gotrustd@verizon.net> Date:   Mon Apr 24 20:57:16 2023 -0700"

	# save system variable, get Commit Strin
	run = True
	while (run):
		numOfMatch = input("What Commit to Revert back to?")
		numOfMatch2 = int(numOfMatch)
		print (numOfMatch, str(numOfMatch2).isdigit())
		# try:	
		# print(matches)
		# pdb.set_trace()
		# print(numOfMatch)
		if(str(numOfMatch2).isdigit()):
			# pdb.set_trace()
			subprocess.run(["git", "revert", matches[int(numOfMatch)]])
			run = False 
		else:		
			print("Choose again")
		# except:
		# 	print("Incorrect answer")
# 
	# print (commitText)
	# print ('======================')
	# commitTextArg = input("Would you like to Revert?: ")
	# if (commitTextArg == "yes" or commitTextArg == "y"):
	# 	subprocess.run(["git", "revert", matches[1]])

	# 	print ("\nAll done!")

	# else:
	# 	print ("\nNothin Changed.")

	# # print (splitString[1])
	# # subprocess.run("git", "revert", splitString[1])

# ======================
if __name__ == '__main__':
  main()

 # ======================
