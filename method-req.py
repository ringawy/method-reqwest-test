from requests import request
method_list = ['get', 'post', 'trace', 'put']
for method in method_list:
	req = request(method, 'http://view.email.tesla.com')
	print(method, req.status_code, req.reason)
