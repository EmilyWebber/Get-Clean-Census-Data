# Explaining the File Processing Logic

Every year has about 75 tables. Every table has three files:
```
	- tablename.txt
	- tablename_metadata.csv
	- tablename_with_ann.csv
```

1. The  ``` tablename.txt ``` file specifies symbols, missing values, and describes some of the sampling techniques.

2. The ``` tablename_metadata.csv ``` file lists each column code along with its substantive description. It is useful for looking at all of the columns in the file in one place, but the next csv has both the column code and its descriptive name, so this file is not strictly necessary.

3. The ``` tablename_with_ann.csv ``` almost always have just over 50 rows and over 400 columns. Each row is a state, and each column is a measurement from the ACS survery for that state, in that year. 