


#ex 1
print ("Exercise - 1")

a = 50
b= 10

if a > b:
    print("Hello World")
    
#ex 2
print ("Exercise - 2")

a= 50
b = 10

if a != b:
    print("Hello World")    

#ex 3
print("Exercise - 3")

a = 50
b = 10

if a == b:
    print("Tes")
else:
    print("No")
    
#ex 4
print("Exercise - 4")

a = 50
b = 10

if a == b:
    print("1")
if a > b:
    print("2")
else:
    print("3")

#ex 5
print("Exercise - 5")

a = 10
b = 10
c = 50
d = 50

if a == b and c == d:          
    print("Hello")

a = 20
b = 10
c = 23
d = 23

if a == b or c == d:    
    print("Hello")

#ex 6
print("Exercise - 6")

if 5 > 2:
   print("YES") 
   
a = 2
b = 5
print("YES") if a == b else print("NO")

#ex 7
print("Exercise - 7")

a = 2
b = 50
c = 2

if a == c or b == c:
    print("YES")

#ex 8
print("Exercise - 8")

print("Please input any number")
num = int(input())

if num % 2 == 0:
    print("The number is EVEN")
else:
    print("THe number is ODD")
    
#ex 9
print("Exercise - 9")        

print("Please note that the first letter should be Upper case")
country = input("Please Enter your country :")

if country == "Myanmar":
    print("You are eligable to vote in Myanmar")
else:
    print("You are not eligable to vote in Myanmar")
    
#ex 10
print("Exercise - 10")

base = int(input("Enter triangle base value : "))
height = int(input("Enter triangle height value : "))

a = 1/2*base*height

print("This is the area of Triangle : ", a)

#ex 11
print("Exercise - 11")

a = 10
b = 20
c = 30

largest_number = max(a,b,c)

print("This is the largest number : ", largest_number)

#ex 12
print("Exercise - 12")

tickets = 20 #price per one ticket

num_tickets = int(input("Enter ticket amount : "))

total_price = num_tickets * tickets #total price without discount
discount_ten_percent = total_price * 0.1
discount1 = total_price-discount_ten_percent #ticket pice 10% discount
discount_twenty_percent = total_price * 0.2
discount2 = total_price - discount_twenty_percent
    
if num_tickets < 20:
    print("Total ticket price : ",total_price)
    
    if num_tickets == 10:
        print("Total ticket price with 10% discount : ", discount1)
        
elif num_tickets == 20:
    print("Total ticket price with 20% dicount : ", discount2)
    
if num_tickets >20:
     print("You can purchase only 20 tickes per single transaction.")
else:
    print("Thank you for your time!!!")        
#ex 13
print("Exercise - 13")

score = int(input("Please enter your Score : ",))

if score <= 100 and score >= 80:
    print("A")
if score <= 79 and score >= 70:
    print("B")
if score <= 69 and score >= 60:
    print("C")
if score >= 50 and score <= 59:
    print("D")
if score >=0 and score <=49:
    print("F")
                    
#ex 14
print("Exercise - 14")

boat_capacity = int(input("Please enter the Boat Capacity value as u like : "))
num_passenger = int(input("Please enter number of passengers as u like : "))

num_across_river = num_passenger // boat_capacity
print("Number of times the boat has to cross the river :", num_across_river)

#ex 15
print("Exercise - 15")

mark = int(input("Enter your mark : "))

if mark >= 90:
    print("You score A")
if mark >= 85 and mark <= 89:
    print("You score A-")        
if mark >= 80 and mark <= 84:
    print("You score B+")
if mark >= 75 and mark <= 79:
    print("You Score B")
if mark >= 70 and mark <= 74:
    print("You Score B-")                   
if mark >= 65 and mark <= 69:
    print("You Score C+")        
if mark >= 60 and mark <= 64:
    print("You Score C")    
if mark >= 55 and mark <= 59:
    print("You Score C-")
if mark >= 50 and mark <= 54:
    print("you Score D")    
if mark >= 0 and mark <= 49:
    print("You Score F")
    
            
   


