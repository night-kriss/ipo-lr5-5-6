#Считывайте строки из файла (text.txt) 
#и создайте новый файл (output.txt), заменяя каждую букву 'о' на 'a' в строках.
with open("text.txt", "r", encoding="utf-8") as file:
      text = file.read()
# Вывод содержимого файла на экран
print("Содержимое исходного файла:")
print(text)
# Замена буквы 'о' на 'a'
rtext=text.replace('а','о')
# Запись изменённого текста в новый файл
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(rtext)
# Вывод изменённого текста на экран
print("Содержимое нового файла:")
print(rtext)   
    
    
    
