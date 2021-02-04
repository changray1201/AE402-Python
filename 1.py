import os.path
if os.path.isfile("1.txt"):
    print("檔案存在")
    doc = open('1.txt',"w")
    for i in range(10000) :
        doc.write("8787878787")
        doc.write(" ")
    doc.close()

    doc = open('1.txt',"r")
    letter = doc.read()
    print(letter)

else :
    print("檔案不存在")
    