todo = []

while True:
    user_input = input("Task (Type '--help' for commands):")
    if user_input == '--exit':
        break
    elif user_input == '--help':
        print(f"Commands:\n--exit: exit the program\n--clear: clear the current list and document\n--print: print the todo-list\n--print document: print the todo-list document\n--complete <task_index>: mark a task as completed")
    elif user_input == '--clear':
        todo=[]
        with open("todo.txt", "w") as file:
            pass
        print('todo-list cleared!')
    elif user_input == '--print':
        print(todo)
    elif user_input.startswith('--complete'):
        try:
            task_index = int(user_input.split()[1])
            if 0 <= task_index < len(todo):
                todo[task_index]['completed'] = True
                print(f"Task {task_index} completed!")
                with open("todo.txt", "w") as file:
                    for task in todo:
                        if task['completed']:
                            file.write(f"{task['task:']} ***\n")
                        else:
                            file.write(f"{task['task:']}\n")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid command. Usage: --complete <task_index>")
    else:
        todo.append({"task:": user_input, "completed": False})
        with open("todo.txt", "w") as file:
            for task in todo:
                if task['completed']:
                    file.write(f"{task['task:']} ***\n")
                else:
                    file.write(f"{task['task:']}\n")

print('todo-list created!')

import requests

api_key = ""

with open("todo.txt", "r") as file:
    file_content = file.read()

url = "https://pastebin.com/api/api_post.php"

login_data = {
    'api_dev_key': api_key,
    'api_user_name': '',
    'api_user_password': ''
}

data = {
    "api_dev_key": api_key,
    "api_option": "paste",
    "api_paste_code": file_content,
    "api_paste_name": "automated-todo-list",
    "api_paste_private": "1",
    "api_user_key": None
}

login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print(login.status_code)
print('User token: ', login.text)

data['api_user_key'] = login.text

r = requests.post(url, data=data)

if r.status_code == 200:
    print("Your todo-list has been successfully uploaded to pastebin!", r.text)
else:
    print("Upload Failed:", r.status_code)
