
def Grades(Percentage):
    if Percentage>=65:
        print ('First Division')
    elif Percentage>=50 and Percentage <65:
        print('Second Division')
    elif Percentage>=35 and Percentage <50:
        print('Third Division')
    elif Percentage <35:
        print('Fail')
    else:
        print ('Enter Correct Pecentage ')


Percentage =int(input('Enter the percentage to know your grade'))
Grades(Percentage)
