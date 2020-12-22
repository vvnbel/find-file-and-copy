import itertools
import os
import shutil

path = 'F:\\FORTEST_IN'
path2 = 'F:\\FORTEST_OUT'
folders = []
folders_rec_cup = []
new = []
folders_os_walk =[]
list_to_download = []
list_folders = []
folderstest = []
folderstest_rec = []
list_folders_2 = []


def bypassfolders(path, level=1):
    folders.append(os.path.basename(path))
    # folders_rec_cup.append(os.path.split(path))
    # print('level=', level, os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            folderstest_rec.append(path + '\\' + i)#выводит правильыне пути
            bypassfolders(path + '\\' + i, level + 1)
        for bank in ready:
            if bank in folders and bank not in new:
                new.append(bank)
                # shutil.copyfile(bank, path2)

# def bypassfolders_walk(path, level=1):
#     for paz, dirs, files in os.walk(path):
#         folders_os_walk.append(path + '\\' + paz)
#         for d in dirs:
#             list_folders.append(d)
#             #shutil.copyfile(paz + '\\' + dirs, path2)

def bypassfolders_walk(path, level=1):
    for paz, dirs, files in os.walk(path):
        folders_os_walk.append(paz)
        folderstest.append(os.path.split(path))
        for d in dirs:
            list_folders.append(d)
            #shutil.copyfile(paz + '\\' + dirs, path2)


# list_folders = list(dict.fromkeys(list_folders)) #промежуточное


def oneDArray(x):
    return list(itertools.chain(*x))


all = []
with open('C:\\Users\\Zver\\test1\\2.txt', encoding='utf-8') as f:
    for row in f:
        b = row.split(';')
        b.pop(0)
        all.append(b)
ready = oneDArray(all)
while '\n' in ready:
    ready.remove('\n')
ready.remove('')
print(ready) # выводит список условия задачи готовый
bypassfolders(path)
bypassfolders_walk(path) #*******************************************функция OS.WALK


f.close()


for i_bank in ready:
    if i_bank in list_folders:
        list_to_download.append(i_bank)
list_to_download = dict.fromkeys(list_to_download)

# folders_os_walk.pop(0)
# print(folders_os_walk) # OS.WALK - все пути папок на сервере СПИСОК - а отсюда пути
# print(list_folders) # OS.WALK - все папки на сервере - список - ВАЖНО
# print(list_to_download) # OS.WALK - кортеж папка на закачку - нон
# print(folderstest) #os.walk TEST CUPPLE


folders.pop(0)
res = dict(zip(folders, folderstest_rec))
print(res)



# print(folders) #рекурсия - выводит список всех папок на сервере !!!!!!!!!!!!!!! - отсюда названия папок
# print(new) #рекурсия - выводит папки которые надо перекопировать
# print(folders_rec_cup) #выводит кортежи из рекурсии путь - папка
# print(folderstest_rec) # выводит пути из рекурсии правильные

# target_path = os.path.join(path, 'file_ololo')
# copy_path = os.path.join(base_path, 'managed', 'file_ololo_new')
#
# if os.path.exists(target_path):
#     shutil.copyfile(target_path, copy_path)