filename = "text.txt" #cоздается переменная filename, которая хранит имя файла text.txt. 
with open(filename, "r", encoding="utf-8") as file: #открывает файл "text.txt" для чтения (r) в кодировке UTF-8. 
   text = file.read() #Считывает все содержимое файла в переменную text. 
   words = text.split() #Разбивает строку text на список слов
   word_count = len(words) #Подсчитывает количество слов в списке words и сохраняет результат в переменную word_count. 
   print(word_count) #Выводит количество слов word_count

