xfile = open('file.txt','r')
for cheese in xfile:
 print 'cheese'

fhand = open("file.txt","r")
count = 0
for cheese in fhand:
 count = count+1
print 'count', count

fname = raw_input('enter the file name')
try:
 fhand = open(fname)
except:
 print 'file can not be opened', fname
 exit()
count = 0
for cheese in fhand:
 count = count+1
print 'count', count

fhand = open('file.txt',"r")
inp = fhand.read()
print len(inp)
print inp[:20]

stuff = 'Hello\nWorld!'
stuff
print stuff

stuff = 'X\nY'
print stuff

print len(stuff)

fhand = open('file.txt')
for line in fhand:
 if line.startswith('cheese'):
  print line

fhand = open('file.txt')
for line in fhand:
 line = line.rstrip()
 if line.startswith('cheese'):
  print line

fhand = open('file.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('123'):
  continue
 print line

fhand = open('file.txt')
for line in fhand:
 line = line.rstrip()
 if not 'happy' in line:
  continue
 print line
