percent_grade = int(input("what is your grade percentage?: "))
while True:
    if percent_grade > 95:
        print("Your letter grade is A")
        break
    elif percent_grade > 90:
        print("Your letter grade is A-")
        break
    elif percent_grade > 85:
        print("Your letter grade is B+")
        break
    elif percent_grade > 80:
        print("Your letter grade is B")
        break
    elif percent_grade > 75:
        print("Your letter grade is B-")
        break
    elif percent_grade > 70:
        print("Your letter grade is C+")
        break
    elif percent_grade > 65:
        print("Your letter grade is C")
        break
    elif percent_grade > 60:
        print("Your letter grade is C-")
        break
    elif percent_grade > 55:
        print("Your letter grade is D+")
        break
    elif percent_grade > 50:
        print("Your letter grade is D")
        break
    elif percent_grade > 45:
        print("Your letter grade is D-")
        break
    else: 
        print("Your letter grade is F")
        break

        
