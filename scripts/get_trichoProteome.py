import urllib,urllib2
import sys

url = "https://www.uniprot.org/uniprot/"

columns = ["id",
           "entry_name",
           "protein names",
           "genes(OLN)",
           "genes(PREFERRED)",
           "length",
           "encodedon",
           "go",
           "go-id"]
col_names=",".join(columns)

params = {
'format':'tab',
'query':'proteome:UP000008878',
'columns':col_names,
'compress':'no'
}

data = urllib.urlencode(params)
request = urllib2.Request(url, data)
contact = "a.j.baylay@soton.ac.uk" # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
request.add_header('User-Agent', 'Python %s' % contact)
response = urllib2.urlopen(request)
page = response.read(200000)

sys.stdout.write(page)
