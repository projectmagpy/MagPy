import MySQLdb
import pafy
import argparse
import sys
import requests

# Open database connection
db = MySQLdb.connect("localhost","root","","myvault" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
username = raw_input("Enter the username : ")
password = raw_input("Enter the password : ")



sql = 'select * from login where username='+"'"+username+"'"+' AND password='+"'"+password+"'"

try:
   # Execute the SQL command
	cursor.execute(sql)
	result=cursor.fetchone()
	number_of_rows=result[0]
	if (number_of_rows==0):
		print "empty"
	else:
		try:
			def invoker():
				try:
					r=requests.get("http://127.0.0.1/tiny/"+username+"/links.txt")
					url=r.content

					fo=open("temp.txt","r+");
					temp=fo.read();
					fo.close();
					if (temp != url):
						fw=open("temp.txt","wb");
						fw.write(url);
						fw.close();
						downloadVideo(url)
					else:
						invoker()
						#exit()
				except:
					print "waiting !!"
					invoker()

			def downloadVideo(url, ptype='mp4', audio=False, silent=False):
				video = pafy.new(url)
				if audio:
					best = video.getbestaudio()
				else:
					best = video.getbest(preftype=ptype)
				print ("Downloading", video.title)
				best.download(quiet=silent)
				print ("Completed", video.title)
				invoker()

			def downloadPlaylist(url, start, end, ptype='mp4',silent=False, audio=False):
				plist = pafy.get_playlist(url)
				videos = [ item['pafy']for item in plist['items'] ]
				if start is None:
					start = 0
				else:
					start = start - 1
				if end is None:
					end = len(videos)

				for video in videos[start:end]:
					try:
						if audio:
							best = video.getbestaudio()
						else:
							best = video.getbest(preftype=ptype)
						print ("Downloading ", video.title)
						best.download(quiet=silent)
						print ("Completed", video.title)
					except:
						print ("Error:skipping")
			invoker()
		except:
			print "function error !"
except:
   print "Invalid username or password !!"

# disconnect from server
db.close()