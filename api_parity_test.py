import difflib
import json
import grequests
import requests
import csv

PARITY_TEST_LIMIT = 15
FILE_NAME = 'YOUR_FILE_TO_POPULATE_URLS.txt'


# A simple task to do to each response object
def do_something(response, **kwargs):
	print response.url, response.text

def exception_handler(request, exception, **kwargs):
		print "Request failed"

# A list to hold our things to do via async
def make_get_requests(urls):
	headers = {
    'content-type': "application/json",
    }

	rs = (grequests.get(u, headers=headers) for u in urls)

	responses = grequests.map(rs)
	print responses
	for t in responses:
		if t is not None:
			print t.text
	return responses

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except:
    return False
  return True

def populateUrls1():
	urls = []
	base_url = 'http://localhost1/$'

	with open(FILE_NAME,'rb') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		
		line_count = 0
		for row in tsvin:

			line_count += 1

			if line_count == 0:
				line_count += 1
				continue

			if line_count > PARITY_TEST_LIMIT:
				break

			SOME_RANDOM_FIELD = row[0] # REPLACE THIS WITH YOUR OWN SHIT!
			urls.append(base_url.replace('$', SOME_RANDOM_FIELD))

	return urls

def populateUrls2():
	urls = []
	base_url = 'http://localhost1/$'

	with open(FILE_NAME,'rb') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		
		line_count = 0
		for row in tsvin:

			line_count += 1

			if line_count == 0:
				line_count += 1
				continue

			if line_count > PARITY_TEST_LIMIT:
				break

			SOME_RANDOM_FIELD = row[0] # REPLACE THIS WITH YOUR OWN SHIT!
			urls.append(base_url.replace('$', SOME_RANDOM_FIELD))

	return urls


def normalize1(response_list):
	print response_list
	lines = []
	# NORMALIZE THE RESPONSE 1 TO SOME COMMON FORMAT
	return lines

def normalize2(response_list):
	print response_list
	lines = []
	# NORMALIZE THE RESPONSE 2 TO SOME COMMON FORMAT
	return lines

def save_normalized_response(normalized_response, fileDir):
	f = open(fileDir,"w")
	#f.write(str(normalized_response))
	for line in normalized_response:
			print line
			f.write(line + '\n')
	f.close()

def diff_responses(normalized_response1, normalized_response2):
	pass
	# TODO: implement file within the python script, currently I use unix diff file1.txr file2.txt
	# for line in difflib.unified_diff(lines1, lines2, fromfile='file1', tofile='file2', lineterm=''):
 	#    	print line

def main():

	# For first api
	urls1 = populateUrls1()
	print 'Generated urls for api 1 (My api): '#, urls1
	print 'Sending Requests to api 1: \n'
	response_list1 = make_get_requests(urls1)
	print 'Normalize the response of api 1: \n'
	normalized_response1 =  normalize1(response_list1)
	print 'Save the normalized response of api 2: \n'
	save_normalized_response(normalized_response1, "test1.txt")

	# For second api
	urls2 = populateUrls2()
	print 'Generated urls for api 2 (Old Api): '#, urls2
	print 'Sending Requests to second api 2: \n'
	response_list2 = make_get_requests(urls2)
	print 'Normalize the response of api 2: \n'
	normalized_response2 = normalize2(response_list2)
	print 'Save the normalized response of api 2: \n'
	save_normalized_response(normalized_response2, "test2.txt")

	#diff_responses(normalized_response1, normalized_response2)

if __name__ == "__main__":
    main()