def z_1(n):
    sl={"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(sl)
    n=input("Введите страну: ")
    print(sl[n])
    for key in sorted(sl):
        print(key, "-",sl[key])
    return ""
def z_2(n):
    sl = {"авеинорст": 1,"дклмпу": 2,"бгёья": 3,"йы": 4,"жзхцч": 5,"шэю": 8, "фщъ": 10}
    n=input("Веведите слово: ")
    k=0
    n.lower()
    for i in n:
        for key in sl:
            if i in key:
                k+=sl[key]
    s="Кол-во очков: "+str(k)
    return s

def z_3_1(n):
    st={"Алиева": "Аида","Аузяк": "Екатерина","Ахмедов": "Муслим","Беликова": "Нелли","Бигалиев": "Амин","Васильев":"Aртём","Гумерова": "Эвелина"}
    leng={"Алиева":["Английский","Русский", "Китайский", "Корейский", "Японский"],
         "Аузяк" :["Английский","Русский"],
         "Ахмедов":["Китайский", "Корейский","Английский"],
         "Беликова":["Английский","Русский", "Корейский"],
         "Бигалиев" :["Английский","Русский"],
         "Васильев":["Русский","Японский"],
         "Гумерова":["Русский"],}
    n=input("Введите фамилию студента: ")
    if st.get(n)==False:
        print("Такого студента не существует")
    else:
        print(len(leng[n]))
    return ""
def z_3_2(n):
    st = {"Алиева": "Аида", "Аузяк": "Екатерина", "Ахмедов": "Муслим", "Беликова": "Нелли", "Бигалиев": "Амин",
          "Васильев": "Aртём", "Гумерова": "Эвелина"}
    leng = {"Алиева": ["Английский", "Русский", "Китайский", "Корейский", "Японский"],
            "Аузяк": ["Английский", "Русский"],
            "Ахмедов": ["Китайский", "Корейский", "Английский"],
            "Беликова": ["Английский", "Русский", "Корейский"],
            "Бигалиев": ["Английский", "Русский"],
            "Васильев": ["Русский", "Японский"],
            "Гумерова": ["Русский"], }
    ml={}
    kl={}
    for key in leng:
        if len(leng[key])>1:
            ml[key]=st[key]
        for i in leng[key]:
            if i=="Китайский":
                kl[key] = st[key]
    print("Студенты которые знают больше 1 языка:")
    for key in ml:
        print(key,ml[key])
    print("Студенты которые знают китайский:")
    for key in kl:
        print(key,kl[key])
print(z_1(" "))
print(z_2(" "))
print(z_3_1(" "))
print(z_3_2(" "))
