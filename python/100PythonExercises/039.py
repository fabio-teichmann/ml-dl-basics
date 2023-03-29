# Write a program to generate and print another tuple whose values are even 
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

data = range(1,11)
even = tuple(filter(lambda i: i%2==0, data))
odd = ()
# for i in data:
#     if i % 2 == 0:
#         even = even + (i,)
#     else:
#         odd = odd + (i,)

print(even)
print(odd)