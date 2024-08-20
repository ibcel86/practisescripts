todo_list = ["Task 1", "Task 2"]

while True:
  new_task = input("Enter the task: ")
  todo_list.append("new_task")
  print(f"{new_task} added")

  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}") 
      index += 1