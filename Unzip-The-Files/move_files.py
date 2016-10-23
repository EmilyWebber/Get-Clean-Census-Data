import csv
import os
import glob



def move_the_files():
	os.chdir("../Zip-File-Downloads")
	for f in glob.glob("*.csv"):
		if "with_ann" in f:
			splits = f.split("_")
			year = "20" + splits[1]
			table = splits[3]
			# print splits

			newname = table + " " + year + ".csv"
			print newname


if __name__ == "__main__":
	move_the_files()