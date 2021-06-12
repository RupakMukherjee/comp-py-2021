stuff = dict()
print stuff.get('candy',-1)

x = ('Glenn', 'Sally', 'Joseph')
print x[2]
y = (1,9,2)
print y
print max(y)

for iter in y:
 print iter

x = [9,8,7]  #  -- this is a list 
x[2] = 6
print x # -- hence it is mutable..

# x = (9,8,7)  -- this is a touple
#x[2] = 6
#print x  --  it is NOT mutable.
 
# y = 'ABC'
# y[2] = "D"
# it will give a traceback...

x = (3,2,1)
# x.sort()
# x.append(5)
# x.reverse()
x.index(3)
# x.pop()


l = list()
dir(l)

t = tuple()
dir(t)

(x,y) = (4, 'fred')
print y

(a,b) = (99,98)
print a

a,b = (99,98)
print a

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
 print k,v

tups = d.items()
print tups

print (0, 1, 2) < (5, 1, 2)
print (0, 1, 2000000) < (0, 3, 4)
print ('Jones', 'Sally') < ("Jones", 'Fred')
print ('Jones', "Sally") < ("Jones", "Sam")

d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t

t.sort()
print t

d = {'a':10, 'b':1, 'c':22}
print d.items()
t = sorted(d.items())
print t

for k,v in sorted(d.items()):
 print k,v

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
 tmp.append( (v,k) )
print tmp
tmp.sort(reverse = True)
print tmp

tmp.sort(reverse = False)
print tmp

fhand = open('A-8-2-data')
counts = dict()
for line in fhand:
 words = line.split()
 for word in words:
  counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
 lst.append (  (val, key)  )
 
lst.sort(reverse = True)

for val, key in lst[:10]:
 print key, val

c = {'a':10, 'b':1, 'c':22}
print sorted ( [ (v,k) for k,v in c.items() ] )
