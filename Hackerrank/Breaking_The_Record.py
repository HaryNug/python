# def breakingRecords(scores):
#     hasil=[0,0]
#     highest_score = lowest_score =scores[0]
#     for a in scores:
#         if highest_score < a:
#             highest_score=a
#             hasil[0]+=1
#         if lowest_score> a:
#             lowest_score=a
#             hasil[1]+=1
#     return hasil
# print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))

# TIDAK PERLU WADAH HASIL
def breakingRecords(scores):
    highest_score = lowest_score =scores[0]
    total_highest=total_lowest=0
    for a in scores:
        if highest_score < a:
            highest_score=a
            total_highest+=1
        if lowest_score> a:
            lowest_score=a
            total_lowest+=1
    return [total_highest,total_lowest]
print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))