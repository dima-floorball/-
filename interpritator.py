translation = {"абаюнда": "for", "абидна":"print", "кинь абаюдно":"input", "абибунда":"if", "гиперабибунда":"elif", "макакаюнда":"else", "кидаем абаюдна пока":"while"}

n = []
t = input()
while t != "close_programm":
    n.append(t)
    t = input()
code = '\n'.join(n)

nonono = ["for", "print", "input", "if", "elif", "else", "while"]

flag = True

for i in nonono:
    if i in code:
        print("Незнаю такую команду" + i)
        flag = False
if flag == True:
    for key, value in translation.items():
        code = code.replace(key, value)
    try:
        exec(code)
    except:
        print("Неизвестная ошибка, пожалуйста проверьте код и устраните лишние команды(")