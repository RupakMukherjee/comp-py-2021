fruit = "banana"
letter = fruit [1]
print letter

n=3
w = fruit [n-1]
print w

fruit = 'banana'
print len(fruit)

fruit = 'banana'
index = 0
while index < len(fruit):
 letter = fruit[index]
 print index, letter
 index = index + 1

fruit = 'banana'
for letter in fruit:
 print letter

word = 'banana'
count = 0
for letter in word:
 if letter == 'a':
  count = count +1
print count

s = "Monty Python"
print s[0:4]
print s[6:7]
print s[6:20]
print s[:2]
print s[8:]
print s[:]

fruit = "banana"
'n' in 'banana'
'm' in 'banana'
"nan" in 'banana'
if "a" in fruit:
 print "Found it!"

if word == 'banana':
 print 'All right, banana'

word = 'apple'
print "All right, Bananas"
if word < 'banana':
 print 'your word,' + word + ',comes before banana'
elif word > 'banana':
 print 'your word,' + word + ',comes after banana'
else:
 print 'All right, bananas'

greet = "Hello Bob"
zap = greet.lower()
print zap
print greet
zap = greet.upper()
print zap
nstr = greet.replace("Bob","Jane")
print nstr
nstr = greet.replace("o","X")
print nstr

print "Hi There".lower()

stuff = "Hello World"
dir(stuff)

fruit = 'banana'
pos = fruit.find('na')
print pos
aa = fruit.find('z')
print aa

greet = " Hello Bob "
print greet.lstrip()
print greet.rstrip()
print greet.strip()

line = 'Please have a nice day'
print line.startswith("Please")
print line.startswith("P")
print line.startswith("p")

data = "From Stephen Marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print atpos
sppos = data.find (" ",atpos)
print sppos
host = data[atpos + 1: sppos]
print host

