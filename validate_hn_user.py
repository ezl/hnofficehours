from BeautifulSoup import BeautifulSoup
import urllib2

hn_username = "lachyg"
hn_profile_url = "http://news.ycombinator.com/user?id=%s" % hn_username
hnoh_profile = "http://hnofficehours.com/user/%s/" % hn_username

hnoh_profile = "marketer"

request = urllib2.Request(hn_profile_url)
response = urllib2.urlopen(request)
page = response.read()
soup = BeautifulSoup(page)

fields = soup.findAll("td", attrs={'valign': 'top'})

user_data = dict()

for f in fields:
    field_key = f.string.replace(":", "") 
    user_data[field_key] = f.findNextSibling().string

print "^ " * 10
print hnoh_profile in user_data['about']

