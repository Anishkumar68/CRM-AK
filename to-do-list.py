empty_list = []


def add_task(**kwargs):

    a = kwargs

    for i in a:
        value = a[i]
        empty_list.append(value)

    print(empty_list)


add_task(
    task1=str(input("enter your task: ")),
    task2=str(input("enter your task: ")),
    task3=str(input("enter your task: ")),
)
