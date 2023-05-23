# list1 = [5,9,2,10]
# list1 = 10

# fungsi yang apapun parameternya selalu return 1
# karena parameter tidak digunakan dalam fungsi tsb
# def fungsi_pangkat_5(angka):
#     return 1**5

# print(fungsi_pangkat_5("")+10)

# increment
# value = 2
# value = value +10

# nilai = 2
# nilai += 10
# print(value)

# print(nilai)


def jazzify(lst):
    # res = []
    # for i in lst:
    #     if "7" not in i:
    #         i+="7"
    #     res.append(i)

    # return res

    # for i in range(len(lst)):
    #     if "7" not in lst[i]:
    #         lst[i]+="7"
    # return lst

    i=0
    while i < 3:
        if "7" not in hurf[i]:
            hurf[i]+="7"
        i+=1
    return lst

hurf = ['A', 'Z7', 'b', 'c', 'u', 'y']
print(jazzify(hurf))
