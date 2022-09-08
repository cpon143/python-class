# W A P to input two string and concatente then further perform the following slice operation
# ---display the last four char
# ---display the char b/w 4 to 8
# ---display the char till 4th last

# string="hello"
# print(len(string))

# WAP to count no. of char in string

# str=input("enter any string")
# count=0
# for i in str:
#     count=count+1
# print(count)
# ------------------------------------------------

# wap to display char of string

# str=input("input string")
# for i in str:
#     print(i,end='')


# ---------------------
# wap to display traversal of string

str=input("entr the string")
rev=''
n=len(str)
count=n-1
while(count>=0):
    rev=rev+str[count]
    count=count-1
print("Reversed string",rev)