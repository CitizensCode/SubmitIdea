# Code courtesy of Stuart Langridge at
# http://www.kryogenix.org/days/2014/01/16/posting-to-discourse-via-the-discourse-rest-api-from-python/

import requests
import logging
import httplib
import json

# Log everything to see what's going on
httplib.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Set the API key
APIKEY = ""
APIUSERNAME = "Brideau"
QSPARAMS = {"api_key": APIKEY, "api_username": APIUSERNAME}
FORUM = "http://ideas.citizenscode.org/"

r = requests.get(FORUM, params=QSPARAMS)
SESSION_COOKIE = r.cookies["_forum_session"]

post_details = {
    "title": "Test title for API submission",
    "raw": """The body of the test post, and it must be
    more than 40 characters long to be valid.""",
    "category": "ideas",
    "archetype": "regular",
    "reply_to_post_number": 0
}

r = requests.post(FORUM + "posts",
                  params=QSPARAMS,
                  data=post_details,
                  cookies={"_forum_session": SESSION_COOKIE})

print "Various details of the response from discourse"
print r.text, r.headers, r.status_code
disc_data = json.loads(r.text)
disc_data["FORUM"] = FORUM
print "The link to your new post is: "
print "%(FORUM)st/%(topic_slug)s/%(topic_id)s" % disc_data
