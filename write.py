#!/usr/bin/python
import psycopg2
import psycopg2
from config import config

class Main:

	def write_data():
		sql = "select code as ID, count(*), MIN(timestamp), MAX(timestamp), MAX(timestamp) - MIN(timestamp) as DIFF  from intrusion_data    				where code = code group by code"
		file = open('DoS_attack_dataset.txt','r')
		params = config()
		# connect to the PostgreSQL database
		conn = psycopg2.connect(**params)
		# create a new cursor
		cur = conn.cursor()
		# execute the SELECT statement
		cur.execute(sql)
		# retrive data from the database
		row = cur.fetchone()
		file = open("testfile.txt","w") 
		while row is not None:
			print(str(row[0])+', '+str(row[1])+', '+str(row[2])+', '+str(row[3]))
			file.write("\n")
			file.write(str(row[0])+', '+str(row[1])+', '+str(row[2])+', '+str(row[3])) 

		cur.close()
		file.close()
		return "Records have been successfully written to the file"


if __name__ == "__main__":
	Main.write_data()
