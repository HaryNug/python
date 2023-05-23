# def string_pairs(s):
#     if len(s)==0:
#         return[]
#     [s[start:start+2] for start in range(0, len(s),2)]

#     if len(s)%2==1:
#         s +="*"
#     s =[s[start:start+2] for start in range(0, len(s),2)]
#     print (s)
# string_pairs("airforces")