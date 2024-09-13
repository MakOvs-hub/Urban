'''
Усложним программу запрашивающую жанры музыки.
'''
import pprint

import requests  # модуль для запросов, у меня почему-то не установился
from threading import Thread

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = 'какой-то токен доступа'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

genre = requests.get(RANDOM_GENRE_API_URL).json()  # запросит строку и переведет в json
data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN,
                                            'q': genre})  # в params передаем GET-параметры после вопросительного знака
# в URL(& - разделитель, по типу ключ-значение) str - 70
pprint.pprint(data.json())  # pprint ровно тот же функционал, но делает "красиво"
data = data.json()
song_id = data['response']['hits'][0]['result']['api_path'])  # обращаемся к данным из запроса
print(f'{GENIUS_URL}{song_id}/apple_music_player')
# откроет композицию в плеере яблока

'''
Добавим в реализацию потоки. Напишем код заново.
'''

import pprint
import queue
import requests  # модуль для запросов, у меня почему-то не установился
from threading import Thread, Event  # эвент своеобразный выключатель(флажок) с True или False

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = 'какой-то токен доступа'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'


class GetGenre(Thread):
    def __init__(self, queue, stop_event):
        self.queue = queue  # принимаем очередь
        self.stop_event = stop_event  # принимаем стоп эвент
        super().__init__()  # инициализируем инит класса потоков

    def run(self):
        while not self.stop_event.is_set():  # условие цикла - пока эвент не перешел в позицию True
            genre = requests.get(RANDOM_GENRE_API_URL).json()  # достаем из этого URL жанры и кладем в очередь
            self.queue.put(genre)


class Genius(Thread):
    all_songs = []

    def __init__(self, queue, stop_event, counter):
        self.queue = queue
        self.stop_event = stop_event
        self.counter = counter  # сколько нам в общей сложности необходимо объектов
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():  # условие цикла - пока эвент не перешел в позицию True
            genre = self.queue.get()  # достаем из очереди и обращаемся
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN,
                                                        'q': genre})  # в params передаем GET-параметры после вопросительного знака
            # в URL(& - разделитель, по типу ключ-значение)
            data = data.json()  # переводим в json и парсим str 67
            try:
                song_id = data['response']['hits'][0]['result']['api_path'])  # обращаемся к данным из запроса
                self.all_songs.append({'genre': genre, 'song': f'{GENIUS_URL}{song_id}/apple_music_player'})
                if self._list_is_filled():  # проверяем на заполненность, интересная особенность - при лимите в 100, по итогу будет 109,
                # тк 100 файл переведет event в set, но очередь к тому моменту заполнена -
                # в итоге следующие 9 также переведут event в set и пойдут в список
                    self.stop_event.set()
            except IndexError as e:
                self.run()  # перезапустим метод при ошибке

    def _list_is_filled(self):
        return len(self.all_songs) >= self.counter


queue = queue.Queue()  # инициализация очереди
stop_event = Event()  # инициализация event
counter = 100  # кол-во объектов
genre_list = []  # список для хранения тредов жанра
genius_list = []  # список для хранения джениуса
for _ in range(6):  # создание тредов жанра
    t = GetGenre(queue, stop_event)
    t.start()
    genius_list.append(t)

for _ in range(10):  # создание тредов джениуса
    t = Genius(queue, stop_event, counter)
    t.start()
    genius_list.append(t)

for t in genre_list:  # соответственно джойним все треды
    t.join()

pprint.pprint(Genius.all_songs)
