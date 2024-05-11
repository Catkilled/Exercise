

#ex 5
print("Exercise - 5")



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


 #Main Program   
scores = getScore()
print("Scores : ",scores)
print("Total score : ", total(scores))
print("Average Score : ", Average(scores))
print("Max Score :",max(scores))
print("Min Scores : ", min(scores))
print("Number of student pass : ", passed(scores))
print("Number of student fail : ", failed(scores))

    





