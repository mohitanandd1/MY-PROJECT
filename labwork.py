
# print("hello worlds")
# print("my name is mohit sisodiya")
# print("am a MCA student")

#print ("name: ", name)

# old = False
# a = None

# print(type(old))
# print(type(a))/

# num=int(input("Enter a number: "))
# if(num%2==0):
#     print("num is even")
# else:
#     print("num is odd")

# a=int(input("Enter 1st no: "))
# b=int(input("Enter 2nd no: "))
# c=int(input("Enter 3rd no: "))

# if(a>=b and b>=c):
#     print("First no is largest", a)

# elif(b>=c):
#     print("second no is largest", b)

# else:
#     print("third no is largest",c)

# x=int(input("enter the num"))
# if(x%7==0):
#     print("divisible by 7")

# else:
#     print("not divisible by 7")


# a=int(input("Enter 1st no: "))
# b=int(input("Enter 2nd no: "))
# c=int(input("Enter 3rd no: "))
# d=int(input("Enter 4th no: "))

# if(a>=b and b>=c and c>=d):
#     print("First no is largest", a)

# elif(b>=c and c>=d):
#     print("second no is largest", b)

# elif(c>=d):
#     print("c is the largest", c)
# else:
#     print("third no is largest", d)



# import math

# a=int(input("enter 1st no: "))
# operator=input("mention your operator:")
# b=int(input("enter 2nd no: "))

# if(operator=='+'):
#     print(a+b)
# elif(operator=='-'):
#     print(a-b)
# elif(operator=='*'):
#     print(a*b)
# elif(operator=='/'):
#     print(a/b)
# elif(operator=='%'):
#     print(a%b)
# elif(operator=='**'):
#     print(a**b)
# elif(operator=='**2'):
#     print(a**2)
# elif(operator=='sqrt'):
#     print(math.sqrt(a))
# else: 
#     print("error")



# num=int(input("Enter the number: "))
# if num>0:
#     print("The number is positive")

# else:
#     print("The number is negative")


# num=int(input("Enter your marks: "))
# if num>= 90:
#     print("grade A")

# elif num >=80 and num<70:
#     print("grade B")

# elif num>=70 and num<60:
#     print("grade C")

# elif num>=60:
#      print("grade D")

# marks=int(input("ENter your marks"))
        
# if marks>=90:
#     grade="a"

# elif marks>=80:
#     grade="b"

# elif marks>=70:
#     grade="c"

# else:
#     grade="f"
# print("Your grade is",grade)/


# for i in range(1,6):
#     print(i)

# for a in range (1,11):
#     print(a)
    

# import math

# a=int(input("enter 1st no: "))
# operator=input("mention your operator:")
# b=int(input("enter 2nd no: "))

# if(operator=='+'):
#     print(a+b)
# elif(operator=='-'):
#     print(a-b)
# elif(operator=='*'):
#     print(a*b)
# elif(operator=='/'):
#     print(a/b)
# elif(operator=='%'):
#     print(a%b)
# elif(operator=='**'):
#     print(a**b)
# elif(operator=='**2'):
#     print(a**2)
# elif(operator=='sqrt'):
#     print(math.sqrt(a))
# else: 
#     print("error")



# a=int(input("enter 1st no: "))
# b=int(input("enter 2nd no: "))
# c=int(input("enter 3rd no: "))

# if a>b and b>c:
#     print("a is the greatest")

# elif b>c:
#     print("b is the greatest")

# else:
#     print("c is the greatest")


# a=int(input("Enter the number: "))
# fact=1
# for i in range(1,a+1):
#     fact=fact*1

# print(fact)

###average of the list lab3#####
# values = input("Enter numbers in list : ")

# numbers = [float(x) for x in values.split()]
# average = sum(numbers) / len(numbers)
# print("The average is:", average)


###__---------------maximum element in a list-----------------
# values = input("enter the numbers for a list: ")
# numbers = [float(x) for x in values.split()]
# maximum = max(numbers)
# print("maximum number in alist is : ", maximum)


###-------------------------
# values = input("Enter number in list: ")
# number= [float(x) for x in values.split()]
# minimum = min(number)
# print("minimum nmbr in list: ", minimum)

###-----------------------------
# values = input("enter the number: ")
# number = [float(x) for x in values.split()]
# int 
# Avg = Avg(number)
# print("avg nmbr in list: ", Avg)

###-------------------------------


# import pandas as pd
# import numpy as np
# data = {
#     "Student_ID": [1,2,3,4,5,6,7,8,9],
#     "Study_hours": [3,4,2,4,3,5.5,6,7,4],
#     "Marks": [67,np.nan,78.6,89.8,45,67.7,78,np.nan,67],
#     "Attendance": [89,78,67.4,89.5,100,56,78,99.9,np.nan],
#     "Department": ["CS","CA","CS","CS","MEDICAL","MEDICAL","CS","MEDIACL","CS"],
#     "Result" : ["pass", "pass","pass","FAil","pass","fail","pass","fail","pass"]

# }
# df = pd.DataFrame(data , columns=["Student_ID", "Study_hours", "Marks","Attendance","Department","Result"])
# df.to_csv("student_data.csv",index=False)
# print(df)

# import pandas as pd
# df = pd.read_csv("student_data.csv")
# print(df.head())

# print(df.isnull())        # Shows True/False for each cell
# print(df.isnull().sum())

# feature engineering
# df["Marks"].fillna(df["Marks"].mean(), inplace=True)
# df["Attendance"].fillna(df["Attendance"].mean(), inplace=True)
# pr

# package fundamental;
# import java.util.Scanner;

# interface Circle {
#     void areaCircle(double r);
# }

# interface Rectangle {
#     void areaRectangle(double l, double b);
# }

# interface Triangle {
#     void areaTriangle(double base, double height);
# }

# class AreaShapes implements Circle, Rectangle, Triangle {

#     public void areaCircle(double r) {
#         double area = Math.PI * r * r;
#         System.out.println("Area of Circle = " + area);
#     }

#     public void areaRectangle(double l, double b) {
#         double area = l * b;
#         System.out.println("Area of Rectangle = " + area);
#     }

#     public void areaTriangle(double base, double height) {
#         double area = 0.5 * base * height;
#         System.out.println("Area of Triangle = " + area);
#     }

#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         AreaShapes obj = new AreaShapes();

#         System.out.println("Choose Shape:");
#         System.out.println("1. Circle");
#         System.out.println("2. Rectangle");
#         System.out.println("3. Triangle");

#         int choice = sc.nextInt();

#         switch(choice) {
#             case 1:
#                 System.out.print("Enter radius: ");
#                 double r = sc.nextDouble();
#                 obj.areaCircle(r);
#                 break;

#             case 2:
#                 System.out.print("Enter length: ");
#                 double l = sc.nextDouble();
#                 System.out.print("Enter breadth: ");
#                 double b = sc.nextDouble();
#                 obj.areaRectangle(l, b);
#                 break;

#             case 3:
#                 System.out.print("Enter base: ");
#                 double base = sc.nextDouble();
#                 System.out.print("Enter height: ");
#                 double h = sc.nextDouble();
#                 obj.areaTriangle(base, h);
#                 break;

#             default:
#                 System.out.println("Invalid choice!");
#         }

#         sc.close();
#     }
# }


#import seaborn as sns
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [10, 20, 25, 30, 40, 50, 60, 70]
# plt.plot(x, y)
# plt.title("Line Plot Example")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()



# LINEAR REGRESSION



# ----------------------------------------------PRACTICE----------------------------------------------------
# ----------------------EVEN/ODD------------------------
# n=int(input("enter a num: "))
# if n%2==0:
#     print("Even")
# else:
#     print("odd")

# # ----------------------LARGEST OF THREE NUMBERS----------------------
# a=int(input("enter 1st num:"))
# b=int(input("enter 2st num:"))
# c=int(input("enter 3st num:"))

# # largest=a
# # if b>largest:
# #     print("b is the largest")
# # if c>largest:
# #     print("c is the largest")
# # print("largest",largest)
# if a>b>c:
#     print("a is the largest")
# elif b>c:
#         print("b is the largest")
# else:
#         print("c is the largest")

# # --------------------------------TABLE FORMAT-------------------------------
# n=int(input("enter a num: "))
# for i in range(1,11):
#     print(f"{n}*{i}=",n*i)

# # --------------------------------FACTORIAL FORMAT---------------------------------
# n=int(input("enter your num: "))
# fact=1
# # for i in range(1,n+1):
# #      fact*=i
# # print("fact: ", fact)
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("fact: ",fact) 

# # -------------------------------PRIME NUM/COMPOSITE NUM-----------------------------------
# # Prime number check

# num = int(input("Enter a number: "))

# if num <= 1:
#     print(num, "is not a prime number")
# else:
#     i = 2
#     is_prime = True
#     while i <= num // 2:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")


# ------------------------------------------TRIAL-FUNCTION_OF_STRING---------------------------------
# str1 = "Hello_Everyone!_This_is_Mohit_Anand,_trying_my_carrier_in_python_as_a_data_analytics"
# print(str1)
# # length= len(str1)
# print(len(str1))
# print(str1.title())
# print(str1.lower())
# print(str1.upper())
# print(str1.count("M",1,80))
# print(str1.find("Mohit",1,50))
# print(str1.index("d",1,50))
# print(str1.endswith("Analytics"))
# print(str1.endswith("data"))
# print(str1.endswith("analytics"))
# print(str1.isalnum())
# print(str1.isspace())
# print(str1.islower())
# print(str1.isupper())
# print(str1.istitle())
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
# print(str1.replace('o','@'))
# print(str1.partition('Mohit'))

# ------------------------------------------------------PRACTICE QUESTIONS--------------------------------------
# -----------------------------------------------------VOWEL-CONSONENT COUNT----------------------------------------
# str1='Hello_world'
str1=input("write your string: ")
vowels='aeiouAEIOU'
a=len(str1)
vowel_count=sum([+1 for char in str1 if char in vowels])
consonent_count= a-vowel_count
print("vowel_count: ", vowel_count)
print("consonent_count: ",consonent_count)

# -----------------------------------------------------------PALINDROME-------------------------
# list1=input("enter a list1 (use space between two elements): ")
# list2=input("enter a list2(use space between two elements): ")
# numbers1 = list(map( list1.split()))
# numbers2 = list(map( list2.split()))

# print("Your list is:", numbers1)
# print("Your list is:", numbers2)

list1=[23, 56, 'mohit', 7.98]
list2=[7.98,'mohit', 56, 23]
a=list1[::-1]
if a==list2:
    print("list2 is a palindrome of list 1")
else:
    print("list2 is not the palindrome of list1")


# -------------------------------------------------length of list without len() function-----------------------
list1 = [89, 67, 78, 'mohit', 7.90,89,67,56,45,'ram','shyam',7.56789]
count = 0

for i in list1:
    count += 1

print("Number of elements in list:", count)

# -----------------------------------------------------sorting withouit sort()-------------------------------
# --------------------------------------------------------BUBBLE SORT-------------------------------------------
list1=[10,30,20,25,78,45,34]
n=len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]> list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
    print("sorted list: ", list1)

# -------------------------------------------------SELECTION SORT-----------------------------------------------
# list1=[10,30,20,25,78,45,34]
# for i in range(len(list1)):
#     min_index=i
# for j in range(i+1,len(list1)):
#     if list1[j]<list1[min_index]:
#         min_index=j
# list1[i],list1[min_index]=list1[min_index],list1[i]
# print("sorted list: ",list1)



# ----------------------------------------------------------------FACTORIAL--------------------------------
num=int(input("input a number: "))
n=num
factorial=[]
for i in range(1,n+1):
    if n%i==0:
        factorial.append(i)
        print( factorial)

# -------------------------------OR----------------------------------------------
num=int(input("input a number: "))
n=num
factorial=[]
for i in range(1,n//2):
    if n%i==0:
        factorial.append(i)
factorial.append(n)
print(factorial)
# -----------------------------OR-----------------------------------------------
from math import sqrt
num=int(input("input a number: "))
n=num
factorial=[]
for i in range(1,int(sqrt(n)+1)):
    if n%i==0:
        factorial.append(i)
    if n//i !=i:
        factorial.append(n//i)
    factorial.sort()
print(factorial)

# ----------------------------------------------------------ARMSTRONG NUMBERS--------------------------------------------
num=int(input("enter a number: "))
n=num
total=0
nod=len(str(n))
while n>0:
    ld=n%10
    total=total+(ld**nod)
    n=n//10
print(total==num)

# ------------------------------------------------PALINDROME--------------------------------------------------------------

num=int(input("enter a number: "))
num=n
result=0
while n>0:
    