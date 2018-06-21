import random
n= random.randint(0,9)
while 0==0:


 guess=int(input("Enter a guess number"))


 if guess > n:
        print("Your answer is less than required")
 elif guess < n:
        print("Your answer is greater than required")
 if guess == n:
     print("Your answer is PERFECT!! Congratulations!!")
     break