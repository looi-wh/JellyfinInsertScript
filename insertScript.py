# !/usr/bin/python3
import platform
import os
import fileinput
import sys
from shutil import copyfile

# insertScript
# designed to insert links into jellyfin thanks to https://www.reddit.com/r/jellyfin/comments/mkudb0/tutorial_how_to_insert_a_custom_link_into/

# run script with sudo python3 insertScript.py -i /usr/share/jellyfin/web/main.*.bundle.js
text_to_search = '+m.ZP.translate("Home")+"</span></a>",' # edit if it changes in future

# extract arg into variable
for arg in sys.argv:
	filename = str(arg)

# theres a chance the user might not specify path
if ".py" in filename:
	print("you did not specify target file location")
	print("run the command below next time")
	print("")
	print("sudo python3 insertScript.py -i /usr/share/jellyfin/web/main.*.bundle.js")
	exit()

# check for correct path
if not os.path.exists(filename):
	print("please ensure the correct file path")
	exit()
else:
	print("target:", filename)

# restore function
if ".js_backup" in filename:
	print("you have linked to a backup file, trying to restore..")
	try:
		dst = filename.replace(".js_backup", ".js")
		os.remove(dst) # remove .js file first
		copyfile(filename, dst) # copy .js_backup to .js
		os.remove(filename) # delete .js_backup
		print("backup restored successfully")
	except:
		print("something went wrong. please review", filename, "and", dst, "for any changes made by this script")
		print("or else, please check if script is running with sudo")
	exit()

# import replacement_text
with open('additional_text.txt') as f:
    additional_text = str(f.read())


# create backup of target
# access the file with /usr/share/jellyfin/web/main.*.bundle.js_backup
dst = filename.replace(".js", ".js_backup")
if os.path.exists(dst):
	print("an existing backup file was found")
	print("please restore the file first before applying new changes by linking to", dst)
	print()
	print("if you still think this is a mistake, run the following command into a terminal with sudo rights")
	print("sudo rm", dst)
	exit()
else:
	copyfile(filename, dst)
	print("a backup file is created at", dst)


replacement_text = text_to_search + additional_text
try:
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
		for line in file:
			print(line.replace(text_to_search, replacement_text), end='')
except:
	print("something went wrong. please review", filename, "for any changes made by this script")
	print("or else, please check if script is running with sudo")
	exit()

print("changes has been applied successfully")
print("job done")