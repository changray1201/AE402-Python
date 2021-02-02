en = input("請輸入英文成績")
math = input("請輸入數學成績")
en =int(en)
math = int(math)
while not (en <= 100 and en >= 0 and math <= 100 and math >= 0) :#判斷成績是否合理
    print(" ")
    print("請重新輸入1~100的數")
    en = input("請輸入英文成績")
    math = input("請輸入數學成績")
    en =int(en)
    math = int(math)
if (en >= 90 and math >=90) or en == 100 or math == 100:#判斷是否能拿到獎學金
    print("可獲得獎學金")
else :
    print("不可獲得獎學金")