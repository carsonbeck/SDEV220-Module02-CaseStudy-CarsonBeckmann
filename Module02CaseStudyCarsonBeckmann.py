#Name: Carson Beckmann
#File Name: Module02CaseStudyCarsonBeckmann.py
#App description: My app will prompt the user for a student last and first name, 
#then their GPA, then the app will tell the user whether the GPA has met the requirement for the Dean's List, Honor Role, or neither.
lastName = ""
while lastName != "ZZZ":
    lastName = input("Input student's last name (Enter ZZZ to end the program): ")
    if lastName == "ZZZ": 
        print("The program has ended.")
        break
    firstName = input("Input student's first name: ")
    gpa = float(input ("Input student's GPA: "))
    if gpa >= 3.5:
        print(firstName + " " +lastName + " has made the Deans's List")
    elif gpa >= 3.25:
        print(firstName + " " +lastName + " has made the Honor Roll")
    else:
        print(firstName + " " +lastName + " did not make the Dean's List or Honor Roll")