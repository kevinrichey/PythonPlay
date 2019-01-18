import string
import sys
import fileinput
import binascii

# Process command line args
inFileName = sys.argv[1]

width = 20

with open(inFileName, 'rb') as binfile:
    bindata = binfile.read()
    binrows = [ bindata[i:i+width] for i in range(0, len(bindata), width) ]
    for row in binrows:
        #hexrow = binascii.hexlify(row)
        txtrow = binascii.b2a_uu(row)
        print(row)

