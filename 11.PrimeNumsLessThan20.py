# Write a Python script that prints prime numbers less than 20
print("Prime numbers between 1 to 20 are:")
limit = 20
for num in range(limit):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)