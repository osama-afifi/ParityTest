import async
import requests
import csv

#urls = ['http://github.com/osama-afifi']

# A simple task to do to each response object
def do_something(response):
	with open('output1.csv', 'wb') as csvout:
    	print response.url, response.text
		csvout = csv.writer(csvout)
		#csvout.writerows([row[0,22] for _ in xrange(count)])



# A list to hold our things to do via async

def make_get_requests(urls):
	async_list = []

	headers = {
    'content-type': "application/json",
    }

	for u in urls:
	    action_item = async.get(u, headers=headers, hooks = {'response' : do_something})
	
	    # Add the task to our list of things to do via async
	    async_list.append(action_item)
	
	# Do our list of things to do via async
	async.map(async_list)


def populateHeader():
	pass

def populateUrls():
	urls1
	limit = 10
	with open('sample.tsv','rb') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		
		line_count = 0
		for row in tsvin:

			line_count += 1

			if line_count == 1:
				continue

			if line_count > limit:
				break

			bookingId = row[0]
			bookingUUID = row[22]
			client_id = row[3]
			print client_id, bookingId, bookingUUID
			#print row






def prepare_urls():
	urls1 = []

	populateUrls()


	#make_get_requests(urls)

def main():
    prepare_urls()

if __name__ == "__main__":
    main()