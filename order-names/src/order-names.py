#!/usr/bin/python3 

def order_names(n):
	namelist = n.split("\n")
	namelist.sort()
	return "\n".join(namelist)




names = "turing\ndjikstra\nknuth"
print(order_names(names))
