line = input(">>> Write, pls").strip()  # убираем пробелы слева и справа

parts = line.split()  # разбиваем строку по пробелам (лучше без ' ')

if not parts:
    print("Пустая команда")
else:
    cmd = parts[0]      # первое слово — команда
    args = parts[1:]   # остальные слова — аргументы





