import excelWriter
import excelReader
import path_root

def menu():
    text = """
    выберите действие с программой:
    1 - прочитать файл
    2 - записать в файл
    3 - посмотреть содержимое папки
    4 - создать папку
    5 - удалить файл/папку
    6 - переименовать файл/папку
    7 - существует ли путь?
    8 - получить размер
    9 - время последнего изменения
    -------------------------------
    0 - завершить работу
    """
    print(text)
    choice = int(input())
    return choice
def main():
    choice = menu()
    while choice != 0:
        path = input('Введите путь: ')
        my_path = path_root.MyPath(path)
        match choice:
            case 1:
                content = my_path.read_file()
                print(content)
            case 2:
                text = input('Текст для файла:')
                my_path.write_file(text)
                print('успешно записано!')
            case 3:
                try:
                    my_path.list_dir()
                except ValueError as e:
                    print(e)
            case 4:
                try:
                    my_path.create_dir()
                    print('создано!')
                except ValueError as e:
                    print(e)
            case 5:
                try:
                    my_path.delete()
                    print('удалено!')
                except ValueError as e:
                    print(e)
            case 6:
                new_name = input('введите новое имя: ')
                try:
                    my_path.rename(new_name)
                    print('готово!')
                except ValueError as e:
                    print(e)
            case 7:
                if my_path.is_exists():
                    print('такой путь существует!')
                else:
                    print('пути не существует.')
            case 8:
                try:
                    size = my_path.get_size()
                    print(f'размер файла {size} байт')
                except ValueError as e:
                    print(e)
            case 9:
                print('последнее изменение:', my_path.get_mtime())
        choice = menu()



main()



