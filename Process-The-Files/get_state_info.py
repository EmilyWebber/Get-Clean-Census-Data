import csv
import sys

'''
This file can be called for a single state.
	It reads in all of the data for that state
	And returns some print statement confirming it read these into memory.
'''

def crunch(alabama):
	all_years = {}

	for year in year_directory:
		one_year = {}

		for table in table_files:

			one_table = {}

			headers = get_headers(table)

			state_row = get_state_row(table, alabama)

			for idx, entry in state_row:

				h = headers[idx]
				one_table[h] = entry

			one_year[table] = one_table

		all_years[year] = one_year

	return all_years




if __name__ == "__main__":
	crunch(sys.argv[1])