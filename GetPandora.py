import requests

eve = "http://eve.gameloft.com"

#2148:58919:3.9.0g:android:googleplay

clientID = raw_input('Enter your ClientID:  ')
urlEve = eve +  "/config/" + clientID + "/datacenters"

# sending get request
def readURL(URL):
	return requests.get(URL) 

# extracting data in json format 
configEve = readURL(urlEve).json()
for nameDatacenters in configEve:
	urlPandora = urlEve + "/"+ nameDatacenters['name'] + "/urls"
	dataPandora = readURL(urlPandora).json()
	print(nameDatacenters['name'].upper() + "-" + dataPandora['pandora'])
