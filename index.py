# simple if and nested elif conditions samples:
# username="virat"
# password="cricket"
# actual_username=input("Enter the name ")
# actual_password=input("Enter the password ")
# if username==actual_username and password==actual_password:
#     print("Login Successfull")
# elif username!=actual_username and password != actual_password:
#     print("invalid username or password ")
# elif username != actual_username :
#     print("invalid username")
# else:
#     print("Login unsuccessfull")

# Loops :for loop and while loop:
# for i in range(0,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# # 3 multiples code
# for i in range(0,101,3):
#     print(i)
# # tables:
# # 1.0
# for i in range(1,11):
#     print(4,'X',i,'=',i*4)
# # 1.1
# for i in range(0,101,5):
#     print(5,'X',int(i/5),'=',i)

# sum:
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

# n=5
# print((n * (n+1))/2)

print("enter the positive numbers or else i will stop executon")
while True:
    num1 = float(input("enter the number"))
    if num1<=0:
        break
    print(num1)

num2=1
while num2>0:
    num2 = float(input("enter a number"))
    print(num2)


