def cmd_help(args): #подсказка команд, которые активны в боте(например)
    print("Команды: help, add <name> <qty>, list, exit")

def cmd_add( args):
    if len(args) < 2:
        print("Использование: add <name> <qty>, у вас либо нету названия, либо количества")
    return
    name = args[0]
    qty = int(args[1])
    printf(f'добавлено {name} x{qty}')

    #обработка ошибок
    try :
        qty = int(args[1])
    except ValueError:
        print("qty должно быть целым числом, например: add milk 2")
        return

commands = {
    "help": cmd_help,
    "add": cmd_add,
}

while True : #infinity consol
    line = input(">>> Write, pls").strip()
    parts = line.split()
    if not parts:
        continue
    else:
        cmd, args = parts[0], parts[1:]

    if cmd == 'exit' :
        break

    action = commands.get(cmd)
    if action is None:
        print("Неизвестная команда. Напишите help.")
        continue


