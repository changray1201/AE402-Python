import os.path

d = {}
t = 0
def buildMenu() :
    print('=>')      
    print('1.加入詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')
    print(' ')
    
print('#####歡迎使用我的英語寶典#####')
print('**************************')

if os.path.isfile("dic.txt") :
    doc = open("dic.txt","r")
    print("old file")
    
else :
    doc = open("dic.txt","w")
    doc = open("dic.txt","r")
    print("new file")
    
for row in doc.readlines() :
    data = row.split(':')

    key = data[0]
    value = data[1]
    value = value.strip()
    
    d[key] = value
print(d)

doc.close()


condition = True
while condition :
    buildMenu()
    
    sel = input("請輸入欲使用功能的編號") #選擇功能
    
    if sel == '1' : #輸入單字
        while condition :
            word = input('請輸入單字(按0離開)')
            if word == '0' : #設定退出
                break
            elif word not in d : #加入單字
                mean = input('請輸入該單字的意思')
                d[word] = mean
                print('添加成功')
            else : #避免重複
                print("單字已經存在")
            doc = open("dic.txt","w")
            
            for k,v in d.items() :
                doc.write(k)
                doc.write(':')
                doc.write(v)
                doc.write('\n')
            doc.close()
            
    elif sel == '2' : #顯示所有單字
        if not os.path.isfile("dic.txt") :
            print("目前字典是空的")
        
        else :
            doc = open("dic.txt","r")
            docr = doc.read()
            print(docr)
            
    elif sel == '3' : #英翻中
        while condition :
            word = input('請輸入欲查詢的單字(按0離開)')
            t = 0
            if word == '0' :  #設定退出
                break
            else :
                for k,v in d.items() :
                    if k == word : #顯示單字
                        print(v)
                        t = 1
                if t == 0 : #查無單字的情況
                    print('查無此單字')
                        
    
    elif sel == '4' : #中翻英
        while condition :
            mean = input('請輸入欲查詢單字的中文(按0離開)')
            t = 0
            if mean == '0' : #設定退出
                break
            else :
                for k,v in d.items() :
                    if v == mean :
                        print(k)
                        t = 1
                if t == 0 :
                    print('查無此單字')
    elif sel == '5' : #測驗
        while condition :
            score = 0 #分數歸零
            for k,v in d.items() :
                print(v)
                word = input('請輸入此單字的英文')
                if word == k :
                    print("獲得1分")
                    score += 1
                else :
                    print("答錯了，共得到" , score , "分")
                    break
            print("恭喜你完成了所有測驗，共獲得" , score , "分")
            break #結束
    elif sel == '6' : #退出
        doc.close()
        condition = False
    else :
        print('請輸入數字1~6以使用本辭典的功能')