import random
num = random.randrange(1,10)
guess = input("請猜一個1~10的數")
guess = int(guess)
while guess <1 or guess > 10:
    print(" ")
    print("請重新輸入一個1~10的數")
    guess = input("請猜一個1~10的數")
    guess = int(guess)
if guess == num :
    print("你猜對了")
else :
    print("你猜錯了")