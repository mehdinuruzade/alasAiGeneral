"""
İstifadəçidən iki ədəd daxil etməsini istəyin (məsələn, "Birinci ədədi daxil edin:", "İkinci ədədi
daxil edin:"). Bu ədədlər string kimi daxil ediləcək. Hər iki ədədi float tipinə çevirin. Daha
sonra bu iki ədəd üzərində toplama, çıxma, vurma və bölmə əməliyyatlarını yerinə yetirin və
nəticələri uyğun cümlələrlə (məsələn, "Cəm: ...", "Fərq: ...") çap edin.
○ Istifadə edilməlidir: input(), Casting (float()), Operatorlar (riyazi), print().
"""
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

print("Addition:" , num_1 + num_2)
print("Subtraction:" , num_1 - num_2)
print("Multiplication:" , num_1 * num_2)
print("Division:" , num_1 / num_2)


"""
İstifadəçidən bir tam ədəd daxil etməsini istəyin. Bu ədədi int tipinə çevirin. if, else şərt
ifadələrindən istifadə edərək ədədin müsbət, mənfi, yoxsa sıfır olduğunu yoxlayın və uyğun
məlumatı çap edin.
○ Istifadə edilməlidir: input(), Casting (int()), Operatorlar (müqayisə), if, elif,
else.
"""

whole_num = int(input("Enter a whole number: "))

if whole_num == 0 :
    print("Entered number is 0. O is an whole number.")
elif whole_num >0 :
    print(f"Entered number is a positive number. {whole_num} is an whole number.")
else:
    print(f"Entered number is a negative number. {whole_num} is not an whole number.")

"""
İstifadəçidən bir söz daxil etməsini istəyin. Daha sonra həmin sözün içində axtarılacaq bir
hərfi daxil etməsini istəyin. find() string metodundan istifadə edərək hərfin sözdə ilk rast
gəldiyi indeksi tapın. Əgər hərf tapılarsa, indeksini çap edin. Əgər tapılmazsa ( find() -1
qaytarırsa), "Hərf sözdə tapılmadı." mesajını çap edin.
○ Istifadə edilməlidir: input(), String, find(), Operatorlar (müqayisə), if, else.
"""

the_word = input("Enter a word: ")
find_in_word = input("Enter a letter to find in the word: ")

result = the_word.find(find_in_word)
if result == -1:
    print("Entered letter is not in the word.")
else:
    print(result)

"""
İstifadəçidən bir cümlə və axtarılacaq bir söz daxil etməsini istəyin. in operatorundan istifadə
edərək daxil edilən sözün cümlənin içində olub-olmadığını yoxlayın. Nəticəyə əsasən "Söz
cümlədə tapıldı." və ya "Söz cümlədə tapılmadı." mesajını çap edin.
○ İstifadə edilməlidir: input(), String, in operatoru, if, else.
"""

user_input = input("Enter any sentence: ")
word_input = input("Enter any word to search inside the sentence: ")
if(word_input in user_input):
    print("The word found in sentence")
else:
    print("The word not found in sentence")

"""
İstifadəçidən ən azı 5 hərfdən ibarət bir söz daxil etməsini istəyin. Daxil edilən sözün:
○ İlk hərfini.
○ Son hərfini.
○ İkinci hərfdən dördüncü hərfə qədər olan hissəsini (ikinci və dördüncü daxil olmaqla,
yəni indeks 1-dən 4-ə qədər). çap edin.
○ İstifadə edilməlidir: input(), String, İndeksləmə [], Slicing[:].
"""

user_input2 = input("Enter any word at least 5 letters long: ")
print("The first letter",user_input2[0])
print("The last letter",user_input2[-1])
print("From letter 2 to letter 4",user_input2[1:4])

"""
Bir neçə (ən azı 4) tam ədəddən ibarət bir list yaradın. Listi çap edin. Listin 2-ci indeksindəki
(yəni üçüncü) elementi çap edin. Listin 1-ci indeksindəki (yəni ikinci) elementinin dəyərini
başqa bir ədədlə dəyişdirin. Dəyişdirilmiş listi yenidən çap edin.
○ İstifadə edilməlidir: List, İndeksləmə [], Elementlərin dəyişdirilməsi.
"""

lst = [4,7,12,21,4,5,56,87,93]
print("Full list:",lst)
print("3rd elemenet in list:",lst[2])
lst.insert(1,45)
print("2nd element changed:",lst)

"""
Bir neçə şəhər adından ibarət bir list yaradın. İstifadəçidən listə əlavə etmək istədiyi yeni bir
şəhər adı və bu şəhərin hansı indeksə əlavə edilməsini istədiyini soruşun. insert()
metodundan istifadə edərək şəhəri istifadəçinin daxil etdiyi indeksə əlavə edin. Listi çap edin.
○ İstifadə edilməlidir: input(), List, insert(), print().
"""

cities = ["Baku","Paris","Milan","New York","Tokio"]
new_city_input = input("Enter a city name: ")
insert_index_input = int(input("Enter an index to insert the city name: "))
cities.insert(insert_index_input, new_city_input.title())
print("New city has been added to index",insert_index_input)
print("New list of cities:",cities)

"""
İstifadəçidən vergüllə ayrılmış meyvə adları sətiri daxil etməsini istəyin (məsələn,
"alma,banan,gilas,nar"). Bu stringi split(',') metodundan istifadə edərək ayrı-ayrı meyvə
adlarından ibarət bir listə çevirin. Alınan listi çap edin.
○ İstifadə edilməlidir: input(), String, split(), List.
"""
fruits_input = input("Enter fruit names seperated by ',': ")
fruits = fruits_input.split(",")
print("Fruit list:",fruits)

"""
İstifadəçidən bir cümlə daxil etməsini istəyin. split() metodundan istifadə edərək cümləni
sözlərinə ayırın və bu sözləri bir listdə saxlayın. Alınan söz listini çap edin. Daha sonra
len() funksiyasından istifadə edərək listdəki sözlərin sayını tapın və uyğun məlumatı çap
edin (məsələn, "Cümlədə X söz var.").
○ İstifadə edilməlidir: input(), String, split(), List, len().
"""

sentence_input = input("Enter any sentence: ")
words = sentence_input.split(" ")
print(words)
print("The sentence contains", len(words), "words")

"""
İstifadəçidən bir-birinin ardınca iki ayrı ədəd daxil etməsini istəyin. Bu ədədləri int tipinə
çevirin və bir listdə saxlayın. Pythonun max() funksiyasından istifadə etmədən, sadəcə if,,
else şərt ifadələri və müqayisə operatorlarından istifadə edərək listdəki ən böyük ədədi tapın
və onu çap edin.
○ İstifadə edilməlidir: input(), Casting (int()), List, Operatorlar (müqayisə), if,,
else.
"""
num_input_1 = int(input("Enter first number: "))
num_input_2 = int(input("Enter second number: "))
num_list = [num_input_1, num_input_2]
print(num_list)
if num_list[0] < num_list[1]:
    print("The max number is in list is:",num_list[1])
elif num_list[0] >  num_list[1]:
    print("The max number is in list is:", num_list[0])
else:
    print("Both numbers are equal")