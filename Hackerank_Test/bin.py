def changeAds(base10): # 8/8
    base2 = bin(base10)
    num = base2[2:]
    str1 = ""
    for i in range(len(num)):
        if num[i] == "0":
            str1 += "1"
        else:
            str1 += "0"
    return int("0b"+str1, base=2)