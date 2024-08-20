FILE_NAME = 'D:\My Documents\Code\Python Code\PyFlo\\todo.txt'

def show_todo_list():
    todo_file = open(FILE_NAME, 'r')
    counter = 1
    for line in todo_file:
        line = line.strip('\n')
        print('  * (' + str(counter) + ') ' + line)
        counter += 1
    if counter == 1:
        print("Nothing in the list!")
    todo_file.close()

def add_to_todo_list(item):
    todo_file = open(FILE_NAME, 'a')
    todo_file.write(item + '\n')
    todo_file.close()

def remove_from_todo_list(number):
    todo_file = open(FILE_NAME, 'r')
    new_content = ''
    counter = 1
    for line in todo_file:
        if counter != number:
            new_content += line
        counter += 1
    todo_file.close()
    todo_file = open(FILE_NAME, 'w')
    todo_file.write(new_content)
    todo_file.close()

def main():
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

main()

