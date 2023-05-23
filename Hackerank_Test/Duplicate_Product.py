def numDuplicates(name, price, weight):
    uniq = []
    for i in range(len(name)):
        item = [name[i], price[i], weight[i]]
        if item not in uniq:
            uniq.append(item)
    dups = len(name) - len(uniq)
    return dups
print(numDuplicates(["ball","bat","glove","glove","glove"],[2,3,1,2,1],[2,5,1,1,1]))