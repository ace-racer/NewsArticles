import requests
import json


def perform_get_request(complete_url, success_handler):
    """Perform the GET request on the specified URL and let the success handler do the success handling"""
    try:
        print "URL: " + complete_url
        r = requests.get(complete_url)
        if r.status_code == requests.codes.ok:
            json_response_data = json.loads(r.text)
            success_handler(json_response_data)
        else:
            r.raise_for_status()
    except requests.exceptions.RequestException as ex:
           print 'An exception occurred while performing the HTTP request: ' + str(ex)
