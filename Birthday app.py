a={}
while True:
    print("1.Display DOB")
    print("2.Add to birthday")
    print("3.Exit")
    b=int(input("Enter an option"))
    if b==1:
        if len(a.keys())==0:
               print("Oops, no content")
        else:
               name=input("enter name")
               birthday=a.get(name,"Data not found")
               print(birthday)
    elif b==2:
               name=input("Friend's name? :")
               date=input("DOB? :")
               a[name]=date
               print("Added")
    elif b==3:
        
              print("Enter to exit")
              exit()
    else:
               print("Enter a valid option")
