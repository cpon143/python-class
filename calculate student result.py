'''ACTIVITIES_WEIGHTAGE=30.0
    SPORTS_WEIGHTAGE=20.0
    EXAMS_WEIGHTAGE=50.0
    
    
    EXAMS_TOTAL=200.0
    ACTIVITIES_TOTAL=60.0
    SPORTS_TOTAL=50.0
    
    exam_score1=int(input("Enter marks in first examinations out of 100"))
    exam_score2=int(input("Enter marks in second examinations out of 100"))
    
    
    sports_score=int(input("Enter marks in sports out of 50"))
    
    activities_score1=int(input("Enter marks in first activity out of 20"))
    activities_score2=int(input("Enter marks in second activity out of 20"))
    activities_score3=int(input("Enter marks in third activity out of 20"))
    
    
    exam_total=exam_score1+exam_score2
    
    activities_total=activities_score1+activities_score2+activities_score3
    
    
    exam_percent=float(exam_total*EXAMS_WEIGHTAGE/EXAMS_TOTAL)
    
    sports_percent=float(sports_score*SPORTS_WEIGHTAGE/SPORTS_TOTAL)
    
    activities_percent=float(activities_total*ACTIVITIES_WEIGHTAGE/ACTIVITIES_TOTAL)
    
    total_percent=float(exam_percent+sports_percent+activities_percent)
    
    print("Total percentage=",total_percent)'''
    
'''ex1_max = int(input("Enter ex1: "))
ex2_max = int(input("Enter ex2: "))
sp_max = int(input("Enter sp: "))

ac1_max=(20*(30/100))
print('ac1_max',ac1_max)
ac2_max=(20*(30/100))
print('ac2_max',ac2_max)
ac3_max=(20*(30/100))
print('ac3_max',ac3_max)

ex1_wt_max=int(input('ex1_wt_max'))
ex2_wt_max=int(input('ex2_wt_max'))
sp_wt_max=int(input('sp_wt_max'))'''

'''num=int(input('enter the number'))
if (num % 2) == 0:

    print ("The number is even") '''
    
'''age=int(input('enter your age'))
if age>= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
'''


'''x,y=10,15
if x<y:
    print(x)
else:
    print(y)
    print("is the min")'''
    
number=int(input('enter the number'))
if number==10:
    print('number is equal to 10')
elif number==50:
    print('number is equal to 50')
elif number==100:
    print('number is equal to 100')
else:
    print('number is 10,50,100')

    