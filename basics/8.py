print [1,24,76]
print ["red",'yellow',"blue"]
print['red',24,98.6]
print[1,[5,6],7]
print[]

for i in [5,4,3,2,1]:
 print i
print 'Blastoff!'

friends = ['Joseph','Glenn',' Sally']
for i in friends:
 print i
print friends [1]

fruit = "Banana"
# fruit[0] = b  -- it will give error. Strings are immutable but lists are mutable.
x = fruit.lower()
print x
lotto = [2,14,26,41,63]
print lotto
lotto[2] = 28
print lotto

greet = 'Hello Bob'
print len(greet)
x = [ 1,2,"joe", 99]
print len(x)

print range(4)
friends = ['Joseph', 'Glenn', 'Sally']
print len(friends)
print range(len(friends))

friends = ['Joseph','Glenn','Sally']
for friend in friends:
 print "Happy New Year:", friend

for i in range(len(friends)):
 friend = friends[i]
 print 'Happy New Year:', friend

a = [1,2,3]
b = [4,5,6]
c = a+b
print c

t = [9,41,12,3,74,15]
print t[1:3]
print t[:4]
print t[3:]
print t[:]

x = list()
print type(x)
print dir(x)

stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff

some = [1,9,21,10,16]
print 9 in some
print 15 in some
print 20 not in some

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print friends
print friends[1]

nums = [3,41,12,9,74,15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

total = 0
count = 0
while True:
 inp = raw_input('Enter a number:')
 if inp =='done':break
 value = float(inp)
 total = total +value
 count = count+1
average = total/count
print 'Average:', average

numlist = list()
while True:
 inp = raw_input('Enter a number:')
 if inp =='done':break
 value = float(inp)
 numlist.append(value)
average = sum(numlist)/len(numlist)
print 'Average', average

abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
for w in stuff:
 print w

line = "a lot                   of spaces"
etc = line.split()
print etc
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)

fhand = open('mbox.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('From'): continue
 words = line.split()
 print words[2]

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print words
email = words[1]
print email
pieces = email.split('@')
print pieces [1]



