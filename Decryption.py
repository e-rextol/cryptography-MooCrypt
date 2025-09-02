def split_index(x):
    a = x.split("/")
    free = 0
    split = []
    key = []
    for i in a:
        if "|" in i:
            for i2 in i:
                if i2 == "9":
                    split.append(free)
                    free = 0
                    continue
                elif i2 == "|":
                    continue
                else:
                    i2 = len(i2)
                    free += i2
        else:
            split.append(i)
    for i3 in split:
        if i3:
            key.append(i3)
    return key

def len_text(x):
    keyword = []
    free = 0
    for i0 in x:
        if isinstance(i0, str):
            for i in i0:
                 if i in ["R","e","l","a","x","A","t","i","o","n","&","%","#","/","|","?"]:
                    keyword.append(i)
                 elif i not in["R","e","l","a","x","A","t","i","o","n","&","%","#","/","|","?"]:
                    if i == "9":
                        keyword.append(free)
                        free = 0
                        continue
                    else:
                        i = len(i)
                        free += i

        elif isinstance(i0, int):
            i0 = i0/-2
            i0 = int(i0)
            keyword.append(i0)
    return keyword


def Return_value_int(y):
    keyword = []
    for i,x in enumerate(y):
        new = y
        if x == "R":
            plus_one = i+1
            if new[plus_one] == "?":
                o = chr(99)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 99
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "e":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(89)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 89
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "l":
            plus_one = i+1
            if new[plus_one] == "?":
                o = chr(79)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 79
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "a":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(69)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 69
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "x":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(59)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 59
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "A":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(49)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 49
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "t":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(39)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 39
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "i":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(29)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 29
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "o":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(9)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 19
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "n":
            plus_one = i + 1
            if new[plus_one] == "?":
                o = chr(9)
                keyword.append(o)
            else:
                next_index = new[plus_one]
                next_index += 9
                next_index = chr(next_index)
                keyword.append(next_index)
        elif x == "%":
            keyword.append(x)
        elif x == "#":
            keyword.append(x)
        elif x == "&":
            keyword.append(x)


    return keyword

def put_space(x):
    keyword = []
    for i in x:
            if isinstance(i,str) and i in ["#","%","&"]:
                keyword.append(" ")
                continue
            keyword.append(i)
    return keyword

def mixtext(x):
    keyword = ""
    for i in x:
        keyword += i
    return keyword

