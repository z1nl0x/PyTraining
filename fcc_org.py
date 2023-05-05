# Fee Code Camp - Code Examples

# print('Hello World!')

# Math Expresions

#x = 1 + 2 ** 3 / 4 * 5
#print(x)

#print(float(99) + 100)

#i = 42

#type(i)

#f = float(i)
#print(f)
#print(type(f))

# Integer division produces a floating point result

#print(9 / 2)

#print(99 / 100)

#print(10.0 / 2.0)


# String conversions

#sval = '123'

#print(type(sval))

#print(int(sval) + 1)

# User Input

#nam = input('Who are you? ')
#print('Welcome', nam)

#x = 20

#if x < 2:
#    print('Small')
#elif x < 10:
#    print('Medium')
#else:
#    print('Large')
#print('All Done!')


#astr = 'Hello Kreft'
#try:
#    istr = int(astr)
#except:
#    istr = -1
#print('First', istr)
#
#astr = '123'
#
#try:
#    istr = int(astr)
#except:
#    istr = -1
#print('Second', istr)


# Testando git command

#def greet(lang):
#    if lang == 'es':
#        return 'Hola'
#    elif lang == 'fr':
#        return 'Bonjour'
#    else:
#        return 'Hello'
#
#print(greet('en'), 'Paulo')


#n = 5
#while n > 0:
#    print(n)
#    n = n - 1
#
#print('Blastoff!')
#print(n)



#for i in [5, 4, 3, 2, 1]:
#    print(i)
#print('Blastoff!')


#friends = ['Joseph', 'Glenn', 'Sally']
#for friend in friends:
#    print('Happy New Year:', friend)
#print('Done!')


#largest_so_far = -1
#print('Before', largest_so_far)
#for the_num in [9, 41, 12, 3, 74, 15]:
#    if the_num > largest_so_far:
#        largest_so_far = the_num
#    print(largest_so_far, the_num)
#
#print('After', largest_so_far)


#zork = 0

#print('Before', zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + 1
#    print(zork, thing)
#print('After', zork) 


#found = False
#print('Before', found)
#for value in [9, 41, 12, 3, 74, 15]:
#    if value == 3:
#        found = True
#    print(found, value)
#print('After', found)


#smallest = None
#print('Before')
#for value in [9, 41, 12, 3, 74, 15]:
#    if smallest is None:
#        smallest = value
#    elif value < smallest:
#        smallest = value
#    print(smallest, value)
#print('After', smallest)

          
#fruit = 'orange'
#index = 0
#while index < len(fruit):
#    letter = fruit[index]
#    print(index, letter)
#    index = index + 1


#for letter in fruit:
#    print(letter)


#word = 'testando'
#count = 0
#for letter in word:
#    if letter == 't':
#        count = count + 1
#print(count)


#stuff = 'Hello World'
#type(stuff)
#dir(stuff)

# FILE PROCESSING


#fhand = open('mbox.txt')
#print(fhand)

#count = 0
#for line in fhand:
#    count = count + 1
#print('Line Count:', count)


#fhand = open('mbox.txt')
#inp = fhand.read()
#print(len(inp))
#print(inp[:20])


fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Test'):
        print(line)








