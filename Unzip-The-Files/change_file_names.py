



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






if __name__ == "__main__":
	codes = read_tables("Tables.txt")
	print codes