def countPairs(projectCosts, target):
    hasil=0
    for i in projectCosts:
        for j in projectCosts:
            if j-i==target:
                hasil+=1

    return hasil
print(countPairs([1,5,3,4,2],2))
# print(countPairs([5,3,4,2,2],2))