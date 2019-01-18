import os
import sys

rootDir = sys.argv[1]

print("Directory\tFile\tSize (b)")

grandtotal = 0

for dirname, subdirs, files in os.walk(rootDir):
    dirsize = 0
    for fname in files:
        filepath = os.path.join(dirname, fname)
        filesize = os.path.getsize(filepath)
        print("%s\t%s\t%d" % (dirname, fname, filesize))
        dirsize += filesize
    print("%s\tTotal Directory Size\t%d" % (dirname, dirsize))
    grandtotal += dirsize

print("\tGrand Total\t%d" % grandtotal)


