# AS Neighbour Diff tools

This repo contains 2 scripts to make it easy to look at AS Adjacencies.

## ndiff.py

usage:
```
ndiff.py <asn> <date1> <date2>
```
Dates are in YYYY-MM-DD format.

This will show a short summary for the number of adjacencies for both dates, and will do some set calculation (how many are added, deleted between the dates)

## nexists.py

usage:
```
nexists.py <asn1> <asn2> <date>
```

This will show if an AS adjacency exists between asn1 and asn2 on a particular date


