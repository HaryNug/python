def migratoryBirds(arr):
    birds={}
    char=set(arr)
    for i in char:
        birds[i] = arr.count(i)
    print(max(birds, key=birds.get))
    
migratoryBirds([1,2,3,4,5,4,3,2,2,1,3,4])