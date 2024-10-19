n = int(input("Enter a number: "))

if n%2!=0 and 1<=n<=100:
    print("Weird")
elif 1<n<6:
    print("Not Weird")
elif 5<n<21:
    print("Weird")
elif 101>n>20:
    print("Not Weird")
else:
    raise ValueError("The number is either less than 1 or greater than 100.")