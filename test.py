import urllib2
import json
from StringIO import StringIO
import base64

username = "aadityadeowanshi@hotmail.com"
password = "somethingyoushouldnotsee"

token = base64.urlsafe_b64encode("%s:%s" % (username, password))
print token
# req = urllib2.Request("https://api.github.com/repos/user/repo")
# req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
# req.add_header("Content-Type", "application/json")
# req.add_header("Accept", "application/json")
# res = urllib2.urlopen(req)

# data = res.read()
# repository = json.load(StringIO(data))