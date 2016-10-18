
import json
import requests
import numpy as np
import datetime
from datetime import timedelta
import dateutil.parser

#Connect to the registration endpoint 
def levelOne(token, github, postRequest, header):
	requestData = {'token': token, 'github': github}
	r = requests.post(postRequest, data = json.dumps(requestData), headers = header)
	print(r.status_code, r.reason)
	print r.text

#reverse the string returned from the first request
def levelTwo(token, postRequest, postValidate, header):
	#send request for the string
	requestData = {'token': token}
	r = requests.post(postRequest, data = json.dumps(requestData), headers = header)
	print(r.status_code, r.reason)

	#get string that will be reversed
	stringToReverse = r.text

	#reverse string 
	reversedString = stringToReverse[::-1]

	#post the solution 
	validateData = {'token': token, 'string': reversedString}
	r2 = requests.post(postValidate, data=json.dumps(validateData), headers = header)
	print(r2.status_code, r2.reason)
	print r2.text

#Get the index of the "needle" in the array called "haystack"
def levelThree(token, postRequest, postValidate, header):
	#send request for the needle and haystack
	requestData = {'token': token}
	r = requests.post(postRequest, data = json.dumps(requestData), headers = header)

	#unpack the data and retrieve the string needle and array hatstack
	needleResponse = r.content
	needleAndHaystack = json.loads(needleResponse)
	needle = needleAndHaystack["needle"]
	haystack = needleAndHaystack["haystack"]

	#finds index of needle
	index = haystack.index(needle)

	#post the solution 
	validateData = {'token': token, 'needle': index}
	r2 = requests.post(postValidate, data=json.dumps(validateData), headers = header)
	print(r2.status_code, r2.reason)
	print r2.text


#Given a prefix and an array, creates an array containing only the strings in the original array that do not start with that prefix.
def levelFour(token, postRequest, postValidate, header):
	#Send request for array and prefix
	requestData = {'token': token}
	r = requests.post(postRequest, data = json.dumps(requestData), headers = header)

	#unpack the data and retrieve the prefix and array
	prefixString = r.content
	prefixDict = json.loads(prefixString) 
	prefix = prefixDict['prefix']
	pArr = prefixDict['array']

	#create array consisting of only words that don't start with prefix
	resultArr = [str(x).encode('ascii') for x in pArr if not x.startswith(prefix)]

	#post the solution 
	validateData = {'token': token, 'array': resultArr}
	r2 = requests.post(postValidate, data=json.dumps(validateData), headers = header)
	print(r2.status_code, r2.reason)
	print r2.text

#Given a datestamp and an int representing an increment of seconds, adds the increment to the date
def levelFive(token, postRequest, postValidate, header):
	#Send  request for datestamp and increment value
	requestData = {'token': token}
	r = requests.post(postRequest, data = json.dumps(requestData), headers = header)
	requestRecieved = r.content

	#unpack the data and retrieve the datestamp and increment
	dateDict = json.loads(requestRecieved)
	dateStampString = dateDict['datestamp']
	interval = dateDict['interval']

	#parse datestamp into a datetime
	inputDate = dateutil.parser.parse(dateStampString, ignoretz=True)

	#turn increment into a timedelta
	intervalTime = timedelta(seconds = interval)

	#add the increment to the datestamp
	updatedDate = inputDate + intervalTime

	#insure that the resulting datestamp is formatted correctly
	updatedDateFormated = updatedDate.isoformat()
	updatedDateFormated = updatedDateFormated + 'Z'

	#post the solution 
	validateData = {'token': token, 'datestamp': updatedDateFormated}
	r2 = requests.post(postValidate, data=json.dumps(validateData), headers = header)
	print(r2.status_code, r2.reason)
	print r2.text


	

#All of the locations to retrieve and send data for each problem along with some other constants

token = '805bb8d34a229bd94e4e730cf014c5ca'
headers = {'content-type': 'application/json'}

github = 'https://github.com/JulianMartinez14/Code2040'
requestOne = 'http://challenge.code2040.org/api/register'	

requestTwo = 'http://challenge.code2040.org/api/reverse'
validateTwo = 'http://challenge.code2040.org/api/reverse/validate'

requestThree = 'http://challenge.code2040.org/api/haystack'
validateThree = 'http://challenge.code2040.org/api/haystack/validate'

requestFour = 'http://challenge.code2040.org/api/prefix'
validateFour = 'http://challenge.code2040.org/api/prefix/validate'

requestFive = 'http://challenge.code2040.org/api/dating'
validateFive = 'http://challenge.code2040.org/api/dating/validate'


#Calls for each method to complete each level 
levelOne(token, github, requestOne, headers)
levelTwo(token, requestTwo, validateTwo, headers)
levelThree(token, requestThree, validateThree, headers)
levelFour(token, requestFour, validateFour, headers)
levelFive(token, requestFive, validateFive, headers)
