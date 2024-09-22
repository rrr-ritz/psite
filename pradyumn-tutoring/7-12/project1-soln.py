test1 = int(input("Enter your first score ===> "))
test2 = int(input("Enter your second score ==> "))
test3 = int(input("Enter your third score ===> "))

average = (test1 + test2 + test3) / 3
print(f"Your average score between the 3 tests was {average}%.")

if average == 100:
    print("Wow, you aced it!")
elif average >= 90:
    print("Great job!")
elif average >= 80:
    print("Good job.")
elif average >= 70:
    print("There's always next time...")
elif average >= 60:
    print("Yikes.")
else:
    print("Bruh")