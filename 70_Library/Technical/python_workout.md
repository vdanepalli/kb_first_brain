## Python Workout - Second Edition -- Reuven M Lerner

### Numbers 

Numeric Types -- int, float, complex. 

```py
random.randint(a, b) # including a, b
input(prompt) # returns empty string if user does not enter anything. 

# assignment in python is not an expression; does not return anything. 

# walrus operator or assignment expression operator ":="

while s:= input('Enter number'):
    print(f"number = {s}")

str.isdigit(value) # checks if string contains all numbers

'Hello, {0}'.format('world')

name = 'world'
first = 'Reuven'
last = 'Lerner'
f'Hello, {first:#<10} {last:#>10}' # 'Hello, Reuven#### ####Lerner'

# splat operator * ; captures all arguments as tuple; if none, empty tuple

def mysum(*numbers):
    output = 0
    for number in numbers:
            output += number
    return output

sum([1,2,3], 4) # 10

s = 0.1 + 0.7 
print(f"{s:.2f}") # two digits after decimal and its a float
```

```py
def run_timing():
    """Asks the user repeatedly for numeric input.
    Prints the average time and number of runs."""

    number_of_runs = 0
    total_time = 0

    while True:     #1
         one_run = input('Enter 10 km run time: ')

        if not one_run:    #2
             break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')

run_timing()
```

floats in python are not exact. so use with caution
decimal can be used where you need exact. 

```py
hex(80) # '0x50'
reversed(array) # consumes less memory, returns iterator
array[::-1] # returns a new string

def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):  #1
         decnum += int(digit, 16) * (16 ** power)   #2
    print(decnum)

hex_output()

int(str, base) = int('A', 16) => 10
```

### Strings

```py
def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'


print(pig_latin('python'))

# Strings are immutable; Easy implementation; Allows to be used as keys in Dict. 
# Constant permanently connects a name to a variable; Python doesn't have it. 
# Constants and Immutables are different. 

str.split(' ') # splits by exactly one whitespace
str.split() # splits by any number of whitespaces. 

def pl_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)

print(pl_sentence('this is a test'))
```

```py
def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')  #1
        else:
            output.append(letter)

    return ''.join(output)

print(ubbi_dubbi('python'))
```

```py
sorted('vinay') # [a, i, n, v, y] returns list; sorts by unicode order

# Unicode UTF-8 -- variable length encoding. Code point = Unicode char number
# ASCII characters are encoded using 1 byte
# French, Spanish, Greek, Russian etc 2 bytes
# Chinese and Emojies etc 3 bytes

def strsort(a_string):
    return ''.join(sorted(a_string))

print(strsort('cbjeaf'))
```

### Lists and Tuples

- When retrieving single index, one can't go beyond bounds. 
- When using slicing, python is forgiving. 
- Lists are arrays of pointers to objects. 

```py
import sys
mylist = []
for i in range(25):
    l = len(mylist)
    s = sys.getsizeof(mylist)
    print(f'len = {l}, size = {s}')
    mylist.append(i)

def mysum(*items):
    if not items:     #1
        return items
    output = items[0]
    for item in items[1:]:
        output += item     #2
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))
```

None, False, 0, Empty collections -- False

```py
mylist = ['abcd', 'efg', 'hi', 'j']
mylist = sorted(mylist, key=len)

def by_country_name(d):
    return d['name']

print(sorted(people, key=by_country_name))

for p in sorted(COUNTRIES, key=lambda d: d['name']):
    print(f'{c["name"]}, {c["size"]}, {c["population"]}')


```

### Dictionaries and Sets


### Files


### Functions


### Functional Programming with Comprehensions


### Modules and Packages


### Objects


### Iterators and Generators

