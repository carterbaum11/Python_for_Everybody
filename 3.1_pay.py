hours = input('Enter Hours: ')
h = float(hours)

rate = input('Enter Rate: ')
r = float(rate)

if h < 41:
    print(h * r)
else :
    print((h-40)*(r*0.5)+(h*r))
