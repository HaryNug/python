# def penjumlahan(a,b):
#     hasil=(a+b)
#     return hasil
# c=penjumlahan(3,5)
# print (c)
# def dis(price,discount):
#     harga=price-price*(discount/100)
#     return harga
# a=dis(100,20)
# print (a)
import math
# def radiant_to_degrees(rad):
#     sudut=round(rad*(180/math.pi),1)
#     return sudut
# print (radiant_to_degrees(1))
# def circle_or_square(rad,area):
#     lingkaran=2*rad*math.pi 
#     persegi=math.sqrt(area)*4
#     if lingkaran>persegi:
#         return True 
#     else:
#         return False
# print (circle_or_square(5,100)) 
# def is_curzon(num):
#     curzon1=2**num+1
#     curzon2=2*num+1
#     hasil=False #deklarasi hasil nilai awalnya false
#     if curzon1%curzon2==0:
#         hasil=True #update nilai hasil jika if terpenuhi
#     else:
#         return False
# print (is_curzon(10))
# def relation_to_luke(name):
#     if(name=="Dart Vader"):
#         hub="father"
#     elif(name=="Leia"):
#         hub="sister"
#     elif(name=="Han"):
#         hub="broter in law"
#     elif(name=="R2D2"):
#         hub="droid"
#     else:
#         return "not detected"
#     say="Luke,i am your "+hub+"."
#     return say
# print (relation_to_luke("Han"))
# def relation_to_luke(name):
#     dic = {
#         "Dart Vader":"father",
#         "Leia":"sister",
#         "Han":"brother in law",
#         "R2D2":"droid"
#     }
#     say="Luke,i am your "+dic[name]+"."
#     return say
# print (relation_to_luke("Leia"))
# def series_resistance(lst):
#     hasil=sum(lst)
#     return hasil
# print (series_resistance([16,3.5,6]))
# def solve_for_exp(a, b):
#     hasil=math.ceil(math.log(b,a))
#     return hasil
# print (solve_for_exp(4,1024))
# def color_invert(rgb1,rgb2,rgb3):
#     hasil=((255-rgb1),(255-rgb2),(255-rgb3)) 
#     return hasil
# print (color_invert(165,170,221))
# def color_invert(rgb):
#     hasil=(abs(rgb[0]-255),abs(rgb[1]-255),abs(rgb[2]-255))
#     return hasil
# print (color_invert([165,170,221]))
# def end_corona(recovers, new_cases, active_cases):
#    hari =0
#    while active_cases > 0 :
#     active_cases = active_cases-(recovers-new_cases)
#     hari += 1
#    return math.ceil(hari)
# print (end_corona(4000,2000,77000))
# def calculator(num1, operator, num2):
#     if operator == "+" :
#         hasil = num1 + num2
#         return hasil
#     elif operator == "*":
#         hasil = num1 * num2
#         return hasil
#     elif operator == "/":
#         if num2 != 0: 
#             hasil = num1 / num2
#             return hasil
#         elif num2 == 0:
#             return "Can't divide by 0!"
#     elif operator == "-":
#         hasil = num1 - num2
#         return hasil
# print (calculator(12,"/",0))
# def damage(damage, speed, time):
#     if damage < 0 or speed < 0 :
#         return "invalid"
#     elif time == "second":
#         hasil = damage*speed*1
#         return hasil
#     elif time == "minute":
#         hasil = damage*speed*60
#         return hasil
#     elif time == "hour":
#         hasil = damage*speed*3600
#         return hasil
#     else :
#         hasil = "invalid"
#         return hasil
# print (damage(5,-5,"second"))
# print (damage(-7,-5,"minute"))
# print (damage(40,5,"our"))
# def asc_des_none(lst, s):
#     if s == "Asc":
#         hasil = sorted(lst)
#         return hasil
#     elif s == "Des":
#         hasil = sorted(lst, reverse=True)
#         return hasil
#     elif s == "none":
#         hasil = lst
#         return hasil
#     else :
#         hasil = "Tidak ada"
#         return hasil
# print (asc_des_none([1,25,14,36],"bebas"))
# def mood_today(mood):
#     if mood == "happy":
#         print("Today, I am feeling happy")
#     elif mood == "sad":
#         print("Today, I am feeling sad")
#     elif mood == " ":
#         print("Today, I am feeling neutral")
#     else :
#         print("Today, I don't feel anything")
# mood_today("biasa aja")
# def mood_today(mood):
#     if  mood :
#         print("Today, I am feeling "+mood)
#     else :
#         print("Today, I am feeling neutral")
# mood_today()
# def mood_today(mood="neutral"):
#     hasil = "Today, I am feeling "+ mood
#     return hasil
# print (mood_today())
# def multiply_two_numbers(num1, num2):
#     return num1 * num2
# multiply_two_numbers(5,10)
# def findLargestNum(nums):
#     return max(nums)
# print(findLargestNum([4,5,1,3]))
# def findLargestNum(nums):
#     for angka in (nums):
# def is_same_num(num1, num2):
#     if num1 == num2:
#         return True
#     else:
#         return False
# print(is_same_num(2,2))
# def less_than_or_equal_to_zero(num):
#     if num <= 0:
#         return True
#     else:
#         return False
# print(less_than_or_equal_to_zero(1))
# def greeting(name):
#    if name == "Mubashir":
#         return "Hello, my love!"
#    else:
#        return "Hello, " +name+"!"
# print(greeting("Mubashir"))
# def findLargestNum(nums):
#     hasil =nums[0]
#     for angka in nums:
#         if angka > hasil:
#             hasil = angka
#     return hasil
# print(findLargestNum([24,15,1,31,99,7,100,912]))
# def find_smallest_num(lst):
#     smallest =lst[0]
#     for angka in lst:
#         if angka < smallest:
#             smallest = angka
#     return smallest
# print(find_smallest_num([-76, 1.345, 1, 0]))
# def difference_max_min(lst):
#     terbesar = lst[0]
#     terkecil = lst[0]
#     for angka in lst:
#         if angka > terbesar :
#             terbesar = angka
#         if angka < terkecil :
#             terkecil = angka
#     hasil = terbesar - terkecil
#     return hasil
# print(difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]))
# def get_sum_of_elements(lst):
#     penjumlahan = 0
#     for angka in lst:
#         penjumlahan = penjumlahan+angka
#     return penjumlahan
# print(get_sum_of_elements([-2, 84, 23]))
# def num_to_dashes(num):
#     return "_"*num
# print(num_to_dashes(60))
# def is_triplet(n1, n2, n3):
#     a = (n1, n2, n3)
#     if n1**2 == n2**2+n3**2:
#         a = True
#     elif n2**2 == n1**2+n3**2:
#         a = True
#     elif n3**2 == n1**2+n2**2:
#         a = True
#     else :
#         a = False
#     return a
# print(is_triplet(1,2,3))

# def flip_end_chars(txt):
#     if txt == list(txt):
#         print ("Incompatible.")
#     elif txt == txt[0]:
#         print("Incompatible.")
#     elif txt[0]==txt[::-1][0:1]:
#         print("Two's a pair.")
#     else :
#         print (txt[::-1][0:1]+txt[1:-1]+txt[0:1])
# flip_end_chars("susu")

# def flip_end_chars(txt):
#     a = (txt)
#     if a == list(txt):
#         a = "Incompatible."
#         return a
#     elif a == txt[0]:
#         a="Incompatible."
#         return a
#     elif txt[0]==txt[::-1][0:1]:
#         a="Two's a pair."
#         return a
#     else :
#         a = txt[::-1][0:1]+txt[1:-1]+txt[0:1]
#         return a
# print(flip_end_chars("Ada"))

# def string_string(kata):
#     a=[kata[start:start+2] for start in range(0, len(kata), 2)]
#     print(a)
# string_string("airforces")

# def string_pairs(s):
#     if len(s)==0:
#         return[]
#     [s[start:start+2] for start in range(0, len(s),2)]

#     if len(s)%2==1:
#         s +="*"
#     s =[s[start:start+2] for start in range(0, len(s),2)]
#     print (s)
# string_pairs("airforces")

# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def compare_age(self, other):
# 		if self.age==other.age:
# 			print(other.name+" is the same age as me.")
# 		elif self.age<other.age:
# 			print(other.name+" is older than me.")
# 		elif self.age>other.age:
# 			print(other.name+" is younger than me.")
# p1 = Person("Samuel", 24)
# p2 = Person("Joel", 36)
# p3 = Person("Lily", 24)

# p3.compare_age(p2)

# def hacker_speak(txt): 
#     to_remov = {"a": "4", "e": "3", "i": "1", "o": "0","s":"5" }
#     for char in to_remov.keys():
#       txt = txt.replace(char, to_remov[char])
#     print (txt)
# hacker_speak("become a coder")

# def is_isogram(txt):
#     huruf_unik = []
#     for huruf in txt:
#         if huruf not in huruf_unik:
#             huruf_unik.append(huruf)
#         else:
#             return False
#     return True
       
# print(is_isogram("algorism"))

# def count_ones(num):
#     biner = bin(num)
#     jumlah = 0
#     for angka in biner:
#         if angka == "1":
#             jumlah +=1
#     return jumlah
# print(count_ones(999))

# def count_vowels(txt):
#     vokal =("aeiou")
#     jumlah = 0
#     for huruf in txt:
#         if huruf in vokal:
#             jumlah +=1
#     return jumlah
# print(count_vowels("Palm"))

# def factorial(num):
#     faktorial = 1
#     for angka in range(1,num+1):
#          faktorial=faktorial*angka
#     return faktorial
# print(factorial(13))
# def evenly_divisible(a, b, c):
#     jumlah = []
#     for angka in range(a,b+1):
#         # print(angka)
#         if angka%c == 0:
#             jumlah.append(angka)
#     print(sum(jumlah))           
# evenly_divisible(1,10,20)