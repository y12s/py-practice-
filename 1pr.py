a = 8

# 1. if-elif-else ladder in Python
# if(a<3): 
#     print("The value of a is greater than 3")
# elif(a>13):
#     print("The value of a is greater than 13")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>17):
#     print("The value of a is greater than 17")
# else:
#     print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")
a = 45 
print(a)
print(2+5)
print('yatharth')
print('singh')
print('rajput')
age = 18
if age >= 18:
    print('eligible')
else:
    print('not eligible')
ys = 'yatharh singh'
ysr = 'Yatharth singh Rajput'

def greet(name='Stranger'):
    print('good day ' + name)

greet('yatharth')

def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]) / 300) * 100
    return p

m1 = [98, 96, 97]
percentage1 = percent(m1)
print(percentage1)