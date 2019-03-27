#!/usr/bin/python
import psycopg2
import psycopg2
from config import config

class Main:

	def get_data():
		sql = "INSERT INTO intrusion_data(code,timestamp) VALUES(%s, %s)"
		conn = None
		file = open('DoS_attack_dataset.txt','r')
		my_data={}
		for line in file:
			if line:
				s = line.split()
				my_data["ID"]=s[3]
				my_data["Timestamp"]=float(s[1])
				params = config()
				# connect to the PostgreSQL database
				conn = psycopg2.connect(**params)
				# create a new cursor
				cur = conn.cursor()
				# execute the INSERT statement
				cur.execute(sql,(s[3], float(s[1])))
				# commit the changes to the database
				conn.commit()
				# close communication with the database
				cur.close()
			if conn is not None:
				conn.close()
		return "Okay"


if __name__ == "__main__":
	Main.get_data()
