def get_prefered(task_1, task_2):
    if task_1.description == "Wash Dishes" and task_2.description == "Cook Dinner":
        return task_1
    elif task_1.description == "Cook Dinner" and task_2.description == "Clean Windows":
        return task_1
    elif task_1.description == "Clean Windows" and task_2.description == "Wash Dishes":
        return task_1
    elif task_1.description == "Wash Dishes" and task_2.description == "Wash Clothes":
        return task_1
    elif task_1.description == "Cook Dinner" and task_2.description == "Do Ironing":
        return task_1
    elif task_1.description == "Clean Windows" and task_2.description == "Do Ironing":
        return task_1
    elif task_1.description == "Do Ironing" and task_2.description == "Wash Clothes":
        return task_1
    elif task_1.description == "Do Ironing" and task_2.description == "Wash Dishes":
        return task_1
    elif task_1.description == "Wash Clothes" and task_2.description == "Cook Dinner":
        return task_1
    elif task_1.description == "Wash Clothes" and task_2.description == "Clean Windows":
        return task_1
    return task_2