'''
Author : Keerthi
Id : N151119
Scraping the images of the students from the local web site (SMS)
'''
import requests
file = open("users.txt","r+")
for line in file:
	k = line.split(':')[0]
	with open(k+'.jpg', 'wb') as handle:
		response = requests.get("http://intranet.rguktn.ac.in/SMS/usrphotos/user/"+str(k)+".jpg", stream=True)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)
file.close()
