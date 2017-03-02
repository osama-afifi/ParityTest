from requests import async


#urls = ['http://github.com/osama-afifi']

# A simple task to do to each response object
def do_something(response):
    print response.url, response.text

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


def prepare_urls():
	urls = []
	make_get_requests(urls)

def start():
	pass