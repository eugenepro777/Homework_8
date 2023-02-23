'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения
и удаления данных.
Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных.

'''
import time


def menu():
    phone_book = read_file()
    print("\n\tЧтение справочника.....'1'\n\
\tПоиск...........'2'\n\
\tДобавление информации...'3'\n\
\tУдаление информации...'4'\n\
\tИзменение информации...'5'\n\
\tОчистить справочник...'999'\n\
\tВыход из меню....'0'")
    mode = input("\nВыберите режим работы со справочником:\n-> ")
    match mode:
        case '1':            
            print_info(phone_book)
            time.sleep(2)
            menu()
        case '2':            
            search_info(phone_book)
            time.sleep(2)
            menu()
        case '3':            
            phone_book = new_contact(phone_book)            
        case '4':            
            delete_info(phone_book)        
        case '5':               
            change_info(phone_book)            
        case '999':
            clear_all(phone_book)
        case '0':
            exit()
        case _:
            print("Выберите пункт меню!")
            time.sleep(2)            
            menu()
    write_file(phone_book)


def read_file():
    with open('Homework_8\\bd.txt', 'r', encoding='utf-8') as file:
        telephone_book = file.readlines()
    return telephone_book

def print_info(telephone_book):
    if not telephone_book:
        print("Справочник пуст")
    else:
        for string in telephone_book:
            print(string.replace(";", " ").strip())

def write_file(telephone_book):    
    with open('Homework_8\\bd.txt', 'w', encoding='utf-8') as file:
        file.writelines(telephone_book)    

# поиск контактов
def search_info(telephone_book):
    select = input("Укажите как будем искать:\n\
...По фамилии: '1'\n...По имени: '2' -> ")
    temp = []    
    found = False
    match select:
        case '1':
            string_search = input("Введите фамилию: ")            
            full_string = string_search.capitalize() + ";"
            for string in telephone_book:
                if full_string in string:
                    temp.append(string)
                    found = True             
        case '2':
            string_search = input("Введите имя: ")            
            full_string = string_search.capitalize() + ";"
            for string in telephone_book:
                if full_string in string:
                    temp.append(string)
                    found = True                         
        case _:
            print("\nВыберите пункт меню!")
            time.sleep(2)            
            menu()
    if found == True:
        print_info(temp)
    else:
        print("\nКонтакт не найден\n")
        time.sleep(3)
        menu()

# добавление новых контактов
def new_contact(telephone_book):    
    str_first = input("Введите фамилию: ")
    str_last = input("Введите имя: ")
    str_patronymic = input("Введите отчество: ")    
    f_name = str_first.capitalize() + ";"    
    l_name = str_last.capitalize() + ";"    
    p_name = str_patronymic.capitalize() + ";"    
    phone_num = input("Введите номер телефона: ")         
    contact_details = (f_name + l_name + p_name + phone_num + "\n")
    telephone_book.append("\n" + contact_details)         
    print(f"...Контакт:\n{contact_details} добавлен!")
    return telephone_book

# удаление контактов
def delete_info(telephone_book):
    flag_run = True
    state = 0
    search = input("Укажите фамилию контакта\
для удаления (с заглавной буквы): ")    
    print()
    while flag_run:        
        for string in telephone_book:
            if search in string:                
                print(string.replace(";", " ").strip())                
                del_contact = string                
                state += 1
        if state > 1:
            search = input("...Уточните ФИО, через ';': ")
            state = 0
            continue
        if state == 0:
            print("Контакт не найден")
            return
        if state == 1:
            confirm = input(f"Подтвердите удаление {del_contact.strip()}\n\
...Удалить: '1'\n...Вернуться в меню: '2'\n -> ")
            match confirm:
                case '1':
                    telephone_book.remove(del_contact)
                    print(f"...Контакт: {del_contact} удален")
                    return
                case _:
                    menu()
                    
# изменение контактов
def change_info(telephone_book):
    flag_run = True
    state = 0
    temp = []
    search = input("Укажите фамилию контакта\
 для изменения номера (с заглавной буквы): ")    
    print()
    while flag_run:        
        for string in telephone_book:
            if search in string:                
                print(string.replace(";", " ").strip())                
                del_contact = string
                temp.append(string)               
                state += 1
        if state > 1:
            search = input("...Уточните ФИО, через ';': ")
            state = 0
            continue
        if state == 0:
            print("Контакт не найден")
            return
        if state == 1:
            new_phone_num = input("Введите новый номер телефона: ").strip()                        
            s = str(del_contact).strip().split(';')
            old_number = s[-1].strip()
            trans1 = str(s)
            trans2 = trans1.replace(old_number, new_phone_num)          
            new_contact = trans2.replace("', '", ";").replace("['","").replace("']","").strip()            
            print(trans2)
            print(new_contact)
            confirm = input(f"Подтвердите изменение {del_contact.strip()}\n\
...Изменить: '1'\n...Вернуться в меню: '2'\n -> ")
            match confirm:
                case '1':
                    telephone_book.append('\n' + new_contact)
                    telephone_book.remove(del_contact)                    
                    print(f"...Контакт: {del_contact} изменен")
                    return
                case _:
                    menu()

def clear_all(telephone_book):
    mode = input("Вы уверены?\n-> Y/N")
    match mode:
        case 'Y':            
            telephone_book.clear()
            return
        case 'N':            
            time.sleep(2)
            menu()   


def main():
    menu()

if __name__ == '__main__':
    main()
