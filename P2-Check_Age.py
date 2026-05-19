n = int(input("Enter your age:"))

if(n<=18):
    print("you are a child")
elif(n>13 and n<18):
    print("you are a teenager")
elif(n>18 and n<60):
    print("you are an adult")
else:
    print("you are a senior citizen")