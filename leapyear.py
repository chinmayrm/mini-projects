print("Welcome to Leap Year Finder")
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print(f"{year}, Is Leap Year")
else:
    print(f"{year}, Is Not a Leap Year")

print("Thank You For Using Leap Year Finder")
