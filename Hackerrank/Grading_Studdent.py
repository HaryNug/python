def gradingStudents(grades):
    for i in range(0,len(grades)): 
        # range kalo isinya[0,4] yang dibaca cuman[0,1,2,3]
        if grades[i]>40 and grades[i]%5>2:
            grades[i]= grades[i] + (5-grades[i]%5)
            
        elif grades[i] > 37 and grades[i] <40:
            grades[i]=grades[i] + (5-grades[i]%5)
    return grades                
print(gradingStudents([73,67,38,33]))

# nyoba for tanpa range
# nyoba pake while sekalian