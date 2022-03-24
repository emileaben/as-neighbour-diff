#!/usr/bin/env python
import re
import requests
import subprocess
from collections import Counter
import sys

'''
"data": {
        "resource": "400280",
        "query_starttime": "2022-03-11T16:00:00",
        "query_endtime": "2022-03-11T16:00:00",
'''

asn = sys.argv[1]
d1 = sys.argv[2]
d2 = sys.argv[3]

urld1 = f"https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn}&starttime={d1}"
urld2 = f"https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn}&starttime={d2}"

def asn_lookup_cymru( asn ):
    cmd = f"dig +short AS{asn}.asn.cymru.com TXT"
    rv = str( subprocess.check_output( cmd, shell=True,  ) )
    fields = list( map( lambda x: re.sub('[ \n]','', x), rv.split('|') ) )
    return fields

def extract_n( url ):
    r = requests.get( url )
    d = r.json()
    out = set()
    for n in d['data']['neighbours']:
        out.add( n['asn'] )
    return out

n1set = extract_n( urld1 )
n2set = extract_n( urld2 )

print("nr. neighbours date1: ", len( n1set ) )
print("nr. neighbours date2: ", len( n2set ) )

same = n1set & n2set
print("nr. neighbours same", len( same ) )

added = n2set - n1set
removed = n1set - n2set

print("nr. neighbours added", len( added ) )
print("nr. neighbours removed", len( removed ) )

print("#ADDED: ")
ccadd = Counter()
for asn in sorted( list( added ) ):
    f = asn_lookup_cymru( asn )
    ccadd[ f[1] ] += 1
    print( f )


print("#REMOVED: ") 
ccrem = Counter()
for asn in sorted( list( removed ) ):
    f = asn_lookup_cymru( asn )
    if( len( f ) > 1 ):
        ccrem[ f[1] ] += 1
        print( f )
    else:
        print( asn )

print("#most added countries")
for cc in ccadd.most_common():
    print( cc )
print("#most removed countries")
for cc in ccrem.most_common():
    print( cc )



