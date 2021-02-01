math = input("請輸入數學成績")
math = int(math)
en = input("請輸入英文成績")
en = int(en)
if math > 100 or en > 100 :
    print("請重新輸入0~100的數")
elif math >= 90 and en >= 90 :
    print(" ")
    print("有獎品")
elif math < 90 and en < 90 :
    print(" ")
    print("要處罰")
else :
    print(" ")
    print("再加油")
    