# Task1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Привет, меняаааа ааабв аааааа, ааабвб, абвббббааа"
text = text.split()
text_new = []
print("Исходный текст", text)

for i in range(len(text)):
    if "абв" not in text[i]: 
        text_new.append(text[i])

print("Отформатированный текст:"," ".join(text_new))