import sys

contacts = {}

def parse(user_input):
    user_input_list = user_input.split(' ')
    command = user_input_list[0]
    args = user_input_list[1:]
    return (command, args)

def input_error(function):
    def inner(*args):
        try:
            return function(*args)
        except KeyError:
            return "The name is not in contacts. Enter user name, please."
        except ValueError:
            return "ValueError: Give me name and phone, please."
        except IndexError:
            return "IndexError: Give me name and phone, please."
        except TypeError:
            return "You entered invalid numbers of arguments for this command."
    return inner

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name}: {phone} was successfully added."

@input_error
def change_contact(name, phone):
    contacts.update({name: phone})
    return f"Contact {name}: {phone} was successfully changed."

@input_error
def get_phone(name):
    phone = contacts[name]
    return f"For {name} the phone is {phone}."

def show_all():
    phone_book = ''
    for name, contact in contacts.items():
        phone_book += f"{name} : {contact}\n"
    return phone_book

def greeting():
    return "How can I help you?"

def end():
    return "Good bye!"

def main():

    handler_commands = {"hello": greeting,
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
                print("You entered an invalid command, please enter one of the next commands: "
                    "'hello', 'show all', 'add', 'change', 'phone', '.', 'close', 'exit', 'good bye'")


if __name__ == '__main__':
    main()

