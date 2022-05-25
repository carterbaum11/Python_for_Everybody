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
