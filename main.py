from random import randint

spisok = ['Паша','Маша', 'Галя','Инна','Марина',"Никита",'Петя','Витя','Миша','Лера','Таня','Аня','Соня','Полина']
def FFF (sp, num):
    newsp= []
    for i in range(num):
        rn=randint(0, len(sp)-1)

        newsp.append(sp[rn])
    return newsp

print(FFF(spisok,20))
