import os
if os.path.isfile('.apikey') == False:
	print("\n === Tweet Purge Setup === ")
	consumerKey = input("Consumer Key: ")
	consumerSecret = input("Consumer Secret: ")
	accessToken = input("Access Token: ")
	accessTokenSecret = input("Access Token Secret: ")
	printArray = [consumerKey,consumerSecret,accessToken,accessTokenSecret]
	with open(".apikey",'w') as apiinfo:
		for item in printArray:
			print(item,file=apiinfo)
os.system("rm .ignoreIDs")
os.system("touch .ignoreIDs")
print("Setup complete")
runOr = input("Run purge.py now? (y/n): ")
if runOr == 'y':
	os.system("python ./purge.py")
