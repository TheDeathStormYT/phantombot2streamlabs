#!/usr/bin/env python

import csv
import sqlite3
import pathlib


def run(database):
	conn = sqlite3.connect(database)
	conn.row_factory = dict_factory
	cursor = conn.cursor()

	pointsCursor = cursor.execute('SELECT variable, value FROM phantombot_points')
	points_rows = pointsCursor.fetchall()

	# Write the CSV
	with open('points-export.csv', 'w+') as csvfile:
		points_writer = csv.writer(csvfile, delimiter = ',')

		points_writer.writerow(['', '', ''])

		for points in points_rows:
			points_writer.writerow([str(points['variable']), str(points['variable']), str(points['value'])])


	conn.close()

	print('[+] Success! You can upload the points-export.csv file to streamlabs (https://streamlabs.com/dashboard#/accountsettings)!')


# Shamelessly stolen from https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query/3300514#3300514
def dict_factory(cursor, row):
	d = {}

	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]

	return d


if __name__ == '__main__':
	db = pathlib.Path('./phantombot.db')

	if not db.exists():
		print('[-] Could not find Phantombot database.')
		print('[-] If you use MySQL for phantombot, please comment on https://github.com/h4ckninja/phantombot2streamlabs/issues/1')

	else:
		db = str(db)
		run(db)
