Query Set запросы по заданию модуля 19.2.

Задача "Я буду устанавливать все игры!":
Для выполнения вам понадобится решение предыдущей задачи, а именно модели Buyer и Game из приложения task1.

При помощи QuerySet запросов необходимо создать 3 записи Buyer и 3 записи Game в вашу базу данных.
Все значения для полей этих записей выберите самостоятельно со следующими условиями:
Только один Buyer должен быть младше 18. (age)
Только одна Game должна быть без ограничения возраста. (age_limited)
После создания всех объектов свяжите их полем buyer у записей Game. Просто присвоить значение при создании объектов не получится. Для присвоения используйте метод set(objects), который принимает коллекцию объектов, например:
Game.objects.get(id=1).buyer.set((first_buyer, second_buyer)) - здесь игра c id=1 приобретается покупателями first_buyer и second_buyer.
При назначении покупателей для игр соблюсти следующие правила:
Только один из Buyer должен обладать всеми Game.
Buyer с возрастом меньше 18 не выдавать игры с ограничением по возрасту.

 Консольные запросы:
 
 Buyer.objects.create(name="Alex", balance=1000, age=17)
<Buyer: Alex>
>>> Buyer.objects.create(name="Slark", balance=1500, age=27)  
<Buyer: Slark>
>>> Buyer.objects.create(name="John", balance=4500, age=37)  
<Buyer: John>
>>> Game.objects.create(title="Dota2" , cost='200' , size='20.5' , description='Time killer' , age_limited = True)  
<Game: Dota2>
>>> Game.objects.create(title='CS' , cost=250 , size=25.4 , description='Team killer' , age_limited = True)        
<Game: CS>
>>> Game.objects.create(title='MineKraft' , cost=2500 , size=1225.78 , description='Land killer')           
<Game: MineKraft>
Game.objects.get(id=2).buyer.add(3)
>>> Game.objects.get(id=1).buyer.set((2,3))                    
>>> Game.objects.get(id=3).buyer.set((1,2,3))
