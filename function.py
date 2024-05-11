



#ex 1
print("Exercise 1")

def triangleArea():
    triangle = 0.5 *H * W
    print("Triangle Area : ", triangle)
    
H = int(input("Enter Height value : "))
W = int(input("Enter Width Vvalue : "))
    
triangleArea()

#ex 2
print("Exercise 2")

def circleArea():
    radius = int(input("Enter radius Value ; "))
    area = 3.14 * radius**2
    return area

print("Area of Circle : ", circleArea())

#ex 3
print("Exercise 3")

def getScore(Scores):
    total = 0
    for score in Scores:
        total += score
        return total
    
Scores = [56, 75, 64, 82, 77, 68]
total = getScore(Scores)
average = total / len(Scores)

print("Total : ", total, "Average : ", average)


#ex 4
print("Exercise 4")

def scoreList():
    list = []
    for x in range(5):
        list = int(input("Enter Score = "))
        return list

def totalScore(Scores):
    total = 0
    for score in total:
        total += score
        return total
    
print("Total Score = ", totalScore(256))

        



    
    





