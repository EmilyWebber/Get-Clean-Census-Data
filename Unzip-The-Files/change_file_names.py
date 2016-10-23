import os
import glob
import re

def read_tables(path):
	codes = {}
	with open(path, "r") as f:
		for row in f.readlines():
			row = row.strip("\n").split("-")
			key =  row[0]
			value = row[-1]

			# add the key and value pair to the dictionary
			codes[key] = value

	return codes

def get_file_names():
	files = []
	os.chdir("../Zip-File-Downloads")
	for f in glob.glob("*"):
		if "zip" not in f:
			files.append(f)
	return files

def change_file_names(codes, file_names):
	'''
	Takes a dictionary matching codes to table names and a list of filenames.
	Walks through the list of filenames: 
		1. Grabs the code from the file name
		2. Grabs the replacement from the code dictionary
		3. Subs in the replacement
		4. Saves the new filename
	'''
	for f in file_names:
		code = f.split("_")[3] 
		
		if ".txt" in code:
			code = code.split(".txt")[0]

		# skip the readme
		if "readme" in f:
			continue

		# get the replacement name
		replace = codes[code]

		# sub out the replacement with regular expressions
		new_file = re.sub(code, replace, f)

		# rename the file
		os.rename(f, new_file)

	print "Congratualations, you just renamed all of the files!!"

if __name__ == "__main__":
	codes = read_tables("Tables.txt")
	print "Read {} codes".format(len(codes))
	
	file_names = get_file_names()
	print "Read {} file names".format(len(file_names))

	change_file_names(codes, file_names)