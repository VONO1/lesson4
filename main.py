from random import randint

spisok = ['Паша','Маша', 'Галя','Инна','Марина',"Никита",'Петя','Витя','Миша','Лера','Таня','Аня','Соня','Полина']

#функция создания списка
def FFF (sp, num):
    newsp= []
    for i in range(num):
        rn=randint(0, len(sp)-1)

        newsp.append(sp[rn])
    return newsp

#создаём список
names_list=FFF(spisok,20)
print(names_list)

#сортировка:
names_counter = {}
for word in names_list:
     if word in names_counter:
         names_counter[word] += 1
     else:
         names_counter[word] = 1

popular_words = sorted(names_counter, key = names_counter.get, reverse = True)

top_3 = popular_words[:1]
print(top_3)


#print(FFF(spisok,20))
