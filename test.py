apps = 3
des = 3
back = 2
front = 1
game = 0

def result():
    global apps, des, back, front, game
    mas = {"apps" : apps, "des" : des, "back" : back, "front" : front, "game" : game}
    maxkey = (max(mas, key=mas.get))#Создаём массив отсартированый по значениям
    maxval = (mas[maxkey])
    mas2 = {maxkey : maxval}#второй словарь с уже заданным максимальным ключом и значением
    for i, j in mas.items():
        if(maxkey != i and maxval == j):#Смотрим есть ли такое же значение в mas у другого ключа
            mas2.update({i : j})
    return mas2


res = {} 
res = result()

begintext = "У вас есть предрасположенность к "

for i in res:
        if i == "apps":
            begintext += "созданию приложений, "
        if i == "des":
            begintext += "веб-дизайну, "
        if i == "back":
            begintext += "бэк-энду, "
        if i == "front":
            begintext += "фронт-энду, "
        if i == "game":
            begintext += "разработке игр, "

print(begintext)