#Skylar Thompson
#M02 - If Else and While.py
#This app will test students GPAs and see if they qualify for either the Dean's List or the Honor Roll



LName = input("Please Enter Student's Lastname or 'ZZZ' to quit: ")
while(LName != 'ZZZ'): 
    FName = input("Please Enter Student's Firstname: ")
    GPA = float(input("What is the Student's GPA?: "))
    if(GPA >= 3.25):
        if(GPA >= 3.5): 
            print(FName, LName, "has made the Honor Roll and the Dean's List!")
        else:
            print(FName, LName, "has made the Honor Roll!")
    else:
        (print(FName, LName, "has unfortunatly not made either Honor Roll or Dean's List"))
    
    LName = input("Please Enter Student's Lastname or 'ZZZ' to quit: ")

print("Thank you for using this App! GoodBye")