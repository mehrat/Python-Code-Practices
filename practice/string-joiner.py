import sys

a = unicode(sys.stdin.readline())

print a
b = a.split(" ")

c = ""
for x in b:
    c += x
    if not x==b[len(b)-1]:
        c +="-"

print("%s"% c[:-1])