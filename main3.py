#take marks as input from the user
print("Enter marks obtained in 4 subjects:")
math = int(input("maths"))
eng = int(input("english:"))
lit = int(input("literature:"))
urdu = int(input("urdu:"))
#lets calculate the percentage of these marks
sum  = math+eng+lit+urdu
print("sum of math, english, literature and urdu")
perc = (sum/400)*100
print(end= "percentage marks = ")
print(perc)