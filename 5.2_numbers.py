"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""

large = None
small = None


while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    #print(num)
    if small is None:
        small = fnum
    if fnum < small:
        small = fnum

    if large is None:
        large = fnum
    if fnum > large:
        large = fnum


print('Maximum is', int(large))
print('Minimum is', int(small))
