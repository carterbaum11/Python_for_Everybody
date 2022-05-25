
def computepay(h, r):
    if h < 41:
        p = (h * r)
    else :
        p = ((h-40)*(r*0.5)+(h*r))
    return p

hours = input("Enter Hours:")
h = float(hours)
rate = input('Enter Rate: ')
r = float(rate)

p = computepay(h, r)
print("Pay",p)
