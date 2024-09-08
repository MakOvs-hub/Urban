import multiprocessing
import datetime

all_data = []
def read_info(name):
    with open(name, 'r', encoding='utf-8') as fil:
        for readline in fil:
            all_data.append(readline)
            if len(readline) == 0:
                return

list_name = ['./Files/file 1.txt', './Files/file 2.txt', './Files/file 3.txt', './Files/file 4.txt']

# Линейно
# start = datetime.datetime.now()
# for i in list_name:
#     read_info(i)
# end = datetime.datetime.now()
# print(end-start)
# print(len(all_data))

# Мультипроцессно
start = datetime.datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, list_name)
end = datetime.datetime.now()
print(end-start)
print(len(all_data))