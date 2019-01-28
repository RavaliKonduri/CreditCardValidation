import re
for x in range(int(raw_input())):
    RI = raw_input().strip()
    inip = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',RI)
    if inip:
        pdip = "".join(inip.group(0).split('-'))
        fnip = re.search(r'(\d)\1{3,}',pdip) 
		if fnip:
		   print 'Invalid'
		else:
		   print 'Valid'
    else:
        print 'Invalid'