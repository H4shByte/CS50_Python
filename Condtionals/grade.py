score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("grade: A")
elif score >= 80 and score <= 90:
    print("grade: B")
elif score >= 70 and score <= 80:
    print("grade: C")
else:
    print("grade: F")

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 90:
    print("B")
elif 70 <= score <= 80:
    print("C")
else:
    print("F")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
