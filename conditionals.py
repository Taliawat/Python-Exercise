#Asks for an input from the user as a mark.
#If the mark is greater that 85 print "Distinction"
#if the mark is between 65 and 85 print "Pass"
#anything else print "Fail"
mark = float(input("What is you exam score: "))

if mark >= 65:
    if mark >= 85:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")