#recap from last class
Amount = input("What USD amount do you want to convert to NRS : ")
TotalConversion = float(Amount)*144
#print("The total amount in NRS would be " + str(TotalConversion) )
print(f"The total amount in NRS would be {TotalConversion}" )

#NEW MATERIAL START DAY 2
#Len function in python (Counts how many characters in a string)
welcome = "Hope you are enjoying our tutorial!"
print("The length of the string is :", len(welcome))

vegetables = ["cabbage", "spinach", "potato"]
print(len(vegetables))

#.upper function
course = 'Python for Beginners'
print(course.upper()) #presenting string in upper case
#output will be: PYTHON FOR BEGINNERS

#.lower function
course = 'Python for Beginners'
print(course.lower()) #presenting string in lower case
#output will be: python for beginners

#.find function (B is at 11th character)
course = 'Python for Beginners'
print(course.find('B')) #finding index/location of character; is case-sensitive; gives -1 if
#the character isn't found
#output will be: 11

#format string function
name = "Alex"
age = 25
print(f"My name is {name} and I am {age} years old")

#IF function, elif, and else function
a = 30
b = 200
if b > a:
    print("b is greater than a")

#a loan application:
#if income is high give loan
#or give loan if the person has a high creditscore or a guarantor
high_income = False
has_guarantor = True
has_highCreditScore = False

if high_income:
    print("Eligible for loan because of high income")

elif has_guarantor or has_highCreditScore:
    print("Eligible for loan because of guarantor or high credit score")

else:
    print("Not eligible for loan")

#weight conversion app
# 1lbs. is .45 kg.
weight = input("What is your weight?")
unit = input("Was the weight you typed in Lbs or Kgs?")
if unit.lower() == "lbs": #if unit.upper() == "LBS"
    ConvertedWeight = float(weight) * 0.45
    print("Your weight in Kgs " + str(ConvertedWeight))

else:
    ConvertedWeight = float(weight) / 0.45
    print("Your weight in lbs " + str(ConvertedWeight))

#SAT Score
# if someone's SAT score is 500 and less, we give a statement called your score is low
# if 501 to 1200, your score is okay
#if 1201 and above, your score is good

name = input("What is your name?")
score = input("What is your SAT score?")

if int(score)<0 or int(score)>1600:
    print("Invalid SAT score")
elif int(score)<=500:
    print(name +", your score is low")
elif int(score)<=1200: #elif score>=501 and score<1200:
    print(name + ", your score is okay")
else:
    print(name + ", your score is good")

#We are now learning about library.
#we are creating a QR code
#Install two Libraries Pillow and QRCode

import qrcode
from PIL import Image
data = "https://youtu.be/wvd9ZuA1lvg"
horse = qrcode.make(data)
horse.save("MyQRCode.jpg") #save it as img file
horse.show() #can you open the file?

