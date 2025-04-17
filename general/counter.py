from collections import Counter

arr1 = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']

counter = Counter(arr1)


print(counter)
print(type(counter))

for item, count in counter.items():
    print(item, count)
print()
b = counter['banana']
print(b)