# urutan=[9,8,7,6,5,4,3,2,1,0]
# operation=[3,6]
# left= urutan[0:3]
# mid=urutan[3:(6+1)][::-1]
# right=urutan[(6+1):len(urutan)]
# print(left+mid+right)
def ReverseArrayQueries(arr,operations):
    result=arr
    for i in operations:
        left=result[0:i[0]]
        mid=result[i[0]:i[1]+1][::-1]
        right=result[i[1]+1:len(result)]
        result=left+mid+right
    return result
print(ReverseArrayQueries([9,8,7,6,5,4,3,2,1,0],[[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]))
print(ReverseArrayQueries([1,2,3],[[0,2],[1,2],[0,2]]))
print(ReverseArrayQueries([5,2,5,1],[[1,2],[1,1]]))