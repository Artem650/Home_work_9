import sys

contacts = {}

def parse(user_input):
    user_input_list = user_input.split(' ')
    command = user_input_list[0]
    args = user_input_list[1:]
    return (command, args)

# Опис функції помилок введення користувача повинні оброблятися за допомогою декоратора input_error
# Обробляє винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError)
def input_error(function):
    def inner(*args):
        try:
            return function(*args)
        except KeyError:
            return "The name isn't in contacts. Enter your user name, please."
        except ValueError:
            return "ValueError: Give me your name and phone, please."
        except IndexError:
            return "IndexError: Give me your name and phone, please."
        except TypeError:
            return "You entered invalid numbers of arguments for this command."
    return inner

#Опис функції,яка зберігає у пам'яті новий контакт
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name}: {phone} was successfully added."

#Опис функції, яка зберігає в пам'яті новий номер телефону існуючого контакту
@input_error
def change_contact(name, phone):
    contacts.update({name: phone})
    return f"Contact {name}: {phone} was successfully changed."

#Опис функції, яка виводить у консоль номер телефону для зазначеного контакту
@input_error
def get_phone(name):
    phone = contacts[name]
    return f"For {name} the phone is {phone}."

#Опис функції, яка виводить всі збереженні контакти з номерами телефонів у консоль
def show_all():
    phone_book = ''
    for name, contact in contacts.items():
        phone_book += f"{name} : {contact}\n"
    return phone_book

def sayhello():
    return "How can I help you?"

def end():
    return "Good bye!"

def main():

    handler_commands = {"hello": sayhello,
                        "add": add_contact,
                        "change": change_contact,
                        "phone": get_phone,
                        "show all": show_all,
                        ".": end,
                        "close": end,
                        "exit": end,
                        "good bye": end}

    while True:
        user_input = input('Enter text please: ')
        if user_input.lower() in handler_commands.keys():
            output = handler_commands[user_input.lower()]()
            print(output)
            if output == "Good bye!":
                sys.exit()
        else:
            command, args = parse(user_input.lower())
            if command in handler_commands.keys():
                print(handler_commands[command](*args))
            else:
                print("You enter an invalid command, please enter one of the next commands: "
                    "'hello', 'show all', 'add', 'change', 'phone', '.', 'close', 'exit', 'good bye'")


if __name__ == '__main__':
    main()

