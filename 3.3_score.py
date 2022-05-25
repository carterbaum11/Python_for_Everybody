# The try except statement does not work

s = input('Enter Score: ')
score = float(s)

try:
    score < 1
except:
    print("Please Try Again")
    quit()

try:
    score >0
except:
    print("Please Try Again")
    quit()

if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else :
    print('F')
