
numberofclasses = ''
grade = ''
average_grade = ''

def algorithim(numberofclasses):
    totalgrade = 0
    for amount in numberofclasses:
        totalgrade += (int(input('What is the grade for this class?: ')))      
    return (totalgrade)


numberofclasses = (input('What is the number of classes?: '))

totalgrade = algorithim(numberofclasses)

numberofclasses = int(numberofclasses)

average_grade = totalgrade / numberofclasses

print("The average grade is:", average_grade)


