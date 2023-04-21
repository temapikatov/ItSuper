class TaskBoard:
    def __init__(self, board_element):
        self.tasks = []
        self.board_element = board_element

    def add_task(self, title, description):
        # Создаем новую задачу
        new_task = Task(title, description)

        # Добавляем задачу в список задач и на доску
        self.tasks.append(new_task)
        self.board_element.append(new_task.element)

        return new_task

    def remove_task(self, task):
        # Удаляем задачу из списка задач и с доски
        if task in self.tasks:
            self.tasks.remove(task)
            self.board_element.remove(task.element)


class Task:
    def __init__(self, title, description):
        # Создаем HTML-элемент задачи
        task_element = TaskElement()
        task_element.add_class("task")
        task_element.set_inner_html("<div class=\"task-header\">" +
                                    "<h3>" + title + "</h3>" +
                                    "<button class=\"delete-task-btn\">Удалить</button>" +
                                    "</div>" +
                                    "<p>" + description + "</p>")

        # Сохраняем свойства задачи
        self.title = title
        self.description = description
        self.element = task_element

        # Добавляем обработчик события на кнопку удаления задачи
        delete_task_btn = task_element.query_selector(".delete-task-btn")
        delete_task_btn.add_event_listener("click", lambda event: self.remove_from_board())

    def remove_from_board(self):
        task_board = self.element.get_task_board()
        if task_board:
            task_board.remove_task(self)

class Priority:
    def __init__(self, level):
        self.level = level

    LOW = Priority("Low")
    MEDIUM = Priority("Medium")
    HIGH = Priority("High")
