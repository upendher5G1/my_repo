print("....SIMPLE CALCULATOR....")
while True:
    a=float(input("enter a :"))
    b=float(input("enter b :"))
    choice=input("1)addition(+)\n2)subtract(-)\n3)multpication(*)\n4)divison(/)\n5)exit\nenter operations:")
    if choice=="+":
        print("result:",a+b)
    elif choice=="-":
        print("result:",a-b)
    elif choice=="*":
        print("result:",a*b)
    elif choice=="/":
        if b!=0:
            print("result:",a/b)
        else:
            print("cannot divide by zero")
    elif choice=="5":
        print("exit calculator....")
        break
    else:
        print("invalid choice")