from BeautifulSoup import BeautifulSoup
import urllib2
from datetime import date, timedelta
import re

def retrieve_hn_user_data(hn_username):
    hn_profile_url = "http://news.ycombinator.com/user?id=%s" % hn_username
    page = urllib2.urlopen(hn_profile_url).read()
    soup = BeautifulSoup(page)
    fields = soup.findAll("td", attrs={'valign': 'top'})
    user_data = dict()
    for f in fields:
        field_key = f.string.replace(":", "") 
        contents = f.findNextSibling().contents
        user_data[field_key] = " ".join(str(c) for c in contents)

    # convert the "created X days ago" to a python datetime
    if not "day" in user_data["created"]:
        days = 0
    else:
        days = int(re.match("\d+", user_data["created"]).group())
    user_data["created"] = date.today() - timedelta(days=days)
    return user_data

if __name__ == "__main__":
    loser = "ezl"
    user_data = retrieve_hn_user_data(loser)

