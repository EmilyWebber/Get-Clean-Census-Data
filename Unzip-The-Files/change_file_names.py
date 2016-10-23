import os
import glob



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
		1. Reads the file into memory 
		2. Replaces the code with the table name
		3. Re-writes the file with the new name
	'''
	print "About to change {} files names".format(len(file_names))


if __name__ == "__main__":
	codes = read_tables("Tables.txt")
	print "Read {} codes".format(len(codes))
	
	file_names = get_file_names()
	print "Read {} file names".format(len(file_names))

	change_file_names(codes, file_names)