import random
num = random.randint(0,20) #產生數字
guess = int(input("猜一個數"))
i = 1
while i < 5:
    if guess == num :
        print(" ")
        print("猜對了")
        i = 5
    elif guess < num :
        print(" ")
        print("太小了")
        print("猜了" , i , "次")
        guess = int(input("再猜一個數"))
    else :
        print(" ")
        print("太大了")
        print("猜了" , i , "次")
        guess = int(input("再猜一個數"))
    i += 1
if i >= 5 :
    print(" ")
    print("你好爛")
    