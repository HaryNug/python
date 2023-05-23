def count_vowels(txt):
    vokal =("aeiouAIUEO")
    jumlah = 0
    for huruf in txt:
        if huruf in vokal:
            jumlah +=1
    return jumlah
print(count_vowels("WAchitore"))