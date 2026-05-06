# String indexing

example = '0123456789'

example2 = 'abcdefghij'

print(example[0:5])
print(example2[0:5])

print(example[5:-1])
print(example2[5:-1])

print(len(example))
print(len(example2))

# Splitting a string

fruits = "banana, apple, orange"
a = fruits.split()
b = fruits.split(',')
c = fruits.split(', ')
d = fruits.split('a')

print(a)
print(b)
print(c)
print(d)

print(fruits.replace('apple', 'pear'))
print(fruits)

print(float('$1,200'.replace(',', '').replace('$','')))

print(range(0,5))

for i in range(0,5):
    print(i)

for peanutbutter in range(100,105):
    print(peanutbutter)

for x in fruits:
    if x == 'o':
        break
    else:
        print(x)


for i, z in enumerate(c, start = 1):
    print(f'{i}. {z}')

ice_cream_sales = [
 ('cone-single', 'chocolate', 4.00),
 ('cone-double', 'mint', 6.00),
 ('dish-single', 'cherry chip', 4.00),
]

for item, flavor, price in ice_cream_sales:
    print(f'{item} in {flavor} for ${price:.2f}')