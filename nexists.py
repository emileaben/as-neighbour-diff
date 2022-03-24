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

asn1 = sys.argv[1]
asn2 = sys.argv[2]
d1 = sys.argv[3]

url = f"https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn1}&starttime={d1}"

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
        out.add( str( n['asn'] ) )
    return out

nset = extract_n( url )

if asn2 in nset:
    print("NEIGBORS ", asn1, asn2)
else:
    print("DISCONNECTED", asn1, asn2)
