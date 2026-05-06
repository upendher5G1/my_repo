a=float(input("enter a :"))
b=float(input("enter b :"))
choice=input("enter 1 for add,2 for sub,3 for mul,4 for div,5 for exit")
if choice=="1":
    print(a+b)
elif choice=="2":
    print(a-b)
elif choice=="3":
    print(a*b)
elif choice=="4":
    print(a/b)
else:
    print("invalid choice")