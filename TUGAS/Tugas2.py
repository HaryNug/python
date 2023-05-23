def flip_end_chars(txt):
    a = (txt)
    if a == list(txt):
        a = "Incompatible."
        return a
    elif a == txt[0]:
        a="Incompatible."
        return a
    elif txt[0]==txt[::-1][0:1]:
        a="Two's a pair."
        return a
    else :
        a = txt[::-1][0:1]+txt[1:-1]+txt[0:1]
        return a
print(flip_end_chars("Cat, dog, and mouse."))
print(flip_end_chars("ada"))
print(flip_end_chars("Ada"))
print(flip_end_chars("z"))
print(flip_end_chars([1,2,3]))