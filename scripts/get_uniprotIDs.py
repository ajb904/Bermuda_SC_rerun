import urllib,urllib2
import sys
from Bio import SeqIO

url = "https://www.uniprot.org/uploadlists/"

fasta = SeqIO.parse(sys.argv[1], 'fasta')

query = " ".join([s.id for s in fasta])

params = {
'from':'EMBL',
'to':'ID',
'format':'tab',
'query':query
}

data = urllib.urlencode(params)
request = urllib2.Request(url, data)
contact = "a.j.baylay@soton.ac.uk" # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
request.add_header('User-Agent', 'Python %s' % contact)
response = urllib2.urlopen(request)
page = response.read()

sys.stdout.write(page)
