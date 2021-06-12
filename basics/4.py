def hello():
 print "Hello"
 print 'Fun'

hello()
print 'Zip'
hello()

big = max("Hello world")
print big
tiny = min('Hello world')
print tiny

def greet(lang):
 if lang == 'es':
  print "Hola"
 elif lang =='fr':
  print 'Bonjour'
 else:
  print "Hello"

greet("en")
greet("es")
greet('fr')

def greet():
 return "Hello"

print greet(), "Glenn"
print greet(), 'Sally'

def greet(lang):
 if lang == 'es':
  return "Hola"
 elif lang =='fr':
  return 'Bonjour'
 else:
  return "Hello"

print greet("en"), "Glenn"
print greet("es"), "Sally"
print greet('fr'), "Michael"

def addtwo(a,b):
 added = a+b
 return a

x = addtwo(3,5)
print x

def addtwo(a,b):
 added = a+b
 return added
x = addtwo (3,5)
print x
