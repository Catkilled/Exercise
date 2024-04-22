



#ex 1
print("Exercise - 1")

i = 1

while  i < 6:
    print (i)
    i+=1
    
#ex 2
print("Exercise - 2")

i = 1
while i < 6 :
    if i == 3:
        break
    i+=1
    print(i)

#ex 3
print("Exercise - 3")

i = 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#ex 4
print("Exercise - 4")

i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#ex 5
print("Exercise - 5")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
#ex 6
print("Exercise - 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
#ex 7
print("Exercise - 7")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
#ex 8
print("Exercise - 8")

for x in range(10):
    print(x)                        

#ex 9
print("Exercise - 9")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#ex 10
print("Exercise - 10")

num_terms = int(input("PLease enter how many number of Terms you want : "))
fib_terms = [0,1]
for i in range(2,num_terms):
    next_term = fib_terms[-1] + fib_terms[-2]

    fib_terms.append(next_term)

print(num_terms, "Your Fibonacci series : ", fib_terms)

