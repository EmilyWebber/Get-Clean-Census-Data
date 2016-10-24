# Explaining the Unzip Logic

1. Each year zip folder has roughly 75 files. You'll need to cd into that directory, and then use some bash scripting to unzip them programatically. This will make your folder explode with files.

	```
	$ cd Zip-File-Downloads
	$ for d in *; do unzip $d; done
	```

2. Each file name has a digit/letter code that corresponds to a substantive description of the information the data conveys. Replace the codes in the file names with:

	```
	$ cd ../Unzip-The-Files
	$ python change_file_names.py
	```

3. This next script will select only the useful files, make their names even more simple, and move them into the cleaned directory.

	```
	$ python move_files.py
	```