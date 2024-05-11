

#ex 6
print("Exercise - 6")



def getScore():
    num_students = int(input("Enter the number of students : "))
    scores = []
    for i in range(num_students):
        while True:
            score = int(input(f"Enter the score for the student {i + 1}:"))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Score must be between 0 & 100")
    return scores

def total(scores):
    Total = 0
    for score in scores:
        Total += score
    return Total

def Average(scores):
    Total = total(scores)
    return Total / len(scores)

def max(scores):
    maxScore = scores[0]
    for score in scores[1:]:
        if score > maxScore:
            maxScore = score
    return maxScore

def min(scores):
    minScore = scores[0]
    for score in scores[1:]:
        if score < minScore:
            minScore = score
    return minScore

def passed(scores):
    passCount = 0
    
    for score in scores:
        if score >= 50:
            passCount += 1
    return passCount

def failed(scores):
    return len(scores) - passed(scores)

def number_of_students(scores):
    return len(scores)

 #Main Program   
scores = []
while True:
    print("\n----------Student Management System--------------")
    print("\n Selection Menu : ")
    print("\n Firstly Choose 1")
    print("1. Input students number : ")
    print("2. Display the number of students : ")
    print("3. Display Total Score : ")
    print("4. Display Average Score : ")
    print("5. Display Maxinum Score : ")
    print("6. Display Minumum Score : ")
    print("7. Number of Student Pass : ")
    print("8. Number of Student Fail : ")
    print("9. Exit Program")
    
    
    choice = int(input("Enter your choice (1-9)"))
    
    if choice == 1:
        scores = getScore()
    elif choice == 2:
        print("Number of students : ", len(scores))
    elif choice == 3:
        print("Total Score : ", total(scores))
    elif choice == 4:
        print("Average Score : ", Average(scores))
    elif choice == 5:
        print("Maximum Score : ", max(scores))
    elif choice == 6:        
        print("Minumum Score  : ", min(scores))
    elif choice == 7:
        print("Student Passed : ", passed(scores))
    elif choice == 8:
        print("Students Failed : ", failed(scores))
    elif choice == 9:
        print("Have A nice Day.")
        break
    else:
        print("No menu available")
        break
    
        
        
            
        
    

    





