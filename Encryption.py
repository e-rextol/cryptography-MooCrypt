
def put_keyword_and_cut_value (x):
    import random
    secret1 = []
    nn = "&%#"
    for i in x:
        for g in i:
            if g == " ":
                g = random.choice(nn)
                secret1.append(g)
            else:
                for ii in g:                                                                #RelaxAtion
                    if ord(ii) < 128 and ord(ii) >= 100:
                        ii = ord(ii)
                        ii -= 99
                        a1 = "R"
                        secret1.append(a1)
                        secret1.append(ii)
                    elif ord(ii) < 100 and ord(ii) >= 80:
                        ii = ord(ii)
                        ii -= 89
                        a2 = "e"
                        secret1.append(a2)
                        secret1.append(ii)
                    elif ord(ii) < 80 and ord(ii) >= 70:
                        ii = ord(ii)
                        ii -= 79
                        a3 = "l"
                        secret1.append(a3)
                        secret1.append(ii)
                    elif ord(ii) < 70 and ord(ii) >= 60:
                        ii = ord(ii)
                        ii -= 69
                        a4 = "a"
                        secret1.append(a4)
                        secret1.append(ii)
                    elif ord(ii) < 60 and ord(ii) >= 50:
                        ii = ord(ii)
                        ii -= 59
                        a5 = "x"
                        secret1.append(a5)
                        secret1.append(ii)
                    elif ord(ii) < 50 and ord(ii) >= 40:
                        ii = ord(ii)
                        ii -= 49
                        a6 = "A"
                        secret1.append(a6)
                        secret1.append(ii)
                    elif ord(ii) < 40 and ord(ii) >= 30:
                        ii = ord(ii)
                        ii -= 39
                        a7 = "t"
                        secret1.append(a7)
                        secret1.append(ii)
                    elif ord(ii) < 30 and ord(ii) >= 20:
                        ii = ord(ii)
                        ii -= 29
                        a8 = "i"
                        secret1.append(a8)
                        secret1.append(ii)
                    elif ord(ii) < 20 and ord(ii) >= 10:
                        ii = ord(ii)
                        ii -= 19
                        a9 = "o"
                        secret1.append(a9)
                        secret1.append(ii)
                    else:
                        ii = ord(ii)
                        ii -= 9
                        a10 = "n"
                        secret1.append(a10)
                        secret1.append(ii)
    return secret1

def put_slash_and_high(x):
    secret = []
    for i in x:
        if i in ["R","e","l","a","x","A","t","i","o","n","&","%","#","/","|"]:
            secret.append("/")
            secret.append(i)
        else:
            if i < 0:
                slash = "/"
                high = "|"
                secret.append(slash)
                i *= -2
                secret.append(i)
                secret.append(high)
            elif i == 0:
                secret.append("?")
            else:
                secret.append(i)

    return secret

def random_text (x):
    import random
    import string
    keyword = []
    free = ""
    for i in x:
        if i == "R" or i == "e" or i == "l" or i == "a" or i == "x" or i == "A" or i == "t" or i == "i" or i == "o" or i == "n" or i == "&" or i == "%" or i == "#" or i == "/" or i == "|" or i == "?":
            keyword.append(i)
        y = isinstance(i,int)
        if y == True:
            for ii in range(i):
                a = string.ascii_letters + string.digits
                a = a.replace("9", "").replace("R","").replace("e","").replace("l","").replace("a","").replace("x","").replace("A","").replace("t","").replace("i","").replace("o","").replace("n","")
                b = random.choice(a)
                free += b
                ii += 1
                if ii == i:
                    free += "9"
                    keyword.append(free)
                    free = ""

    return keyword

def fusion (x):
    keyword = ""
    for i in x:
        keyword += i
    return keyword



