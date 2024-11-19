
'''ListA=['Rakesh','Ramesh','Lokesh','Ram']
ListB=['Ram','Rakesh','Lokesh','Dev','Madhav']
ListC=[]

def commonValues(ListA,ListB):
    for i in ListA:
        if i in ListB:
          ListC.append(i)
    return ListC

print(commonValues(ListA,ListB))'''


def findCommonElement(set1, set2):
    # Find the common elements using intersection
    set3 = set1 & set2
    return set3

# Get input from the user, splitting by commas and converting to sets
set1 = set(input("Enter elements for Set 1 (comma-separated): ").split(','))
set2 = set(input("Enter elements for Set 2 (comma-separated): ").split(','))

# Call the function and print the result
result = findCommonElement(set1, set2)
print("Common elements:", result)







