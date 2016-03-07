#from cgi import parse_qs, escape
from urlparse import parse_qs
def app(environ, start_response):
	#response = ['%s: %s' % (key, value) for key, value in environ.items()]
	#response = parse_qs(environ['QUERY_STRING'])
	#response = ['%s=%s'% (key, value[0]) for key, value in response.items()]
	#response = '\n'.join(response)
	response = environ['QUERY_STRING']
	response = response.replace('&', '\n')
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [response]
