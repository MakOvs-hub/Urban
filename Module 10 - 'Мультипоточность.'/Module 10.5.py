import multiprocessing
import datetime


def read_info(name):
    all_data = []
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


# Мультипроцессно

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as p:
        p.map(read_info, list_name)
    end = datetime.datetime.now()
    print(end - start)
