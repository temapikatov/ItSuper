class TaskBoard {
  constructor(boardElement) {
    this.boardElement = boardElement;
    this.tasks = [];
  }

  addTask(title, description) {
    // Создаем новую задачу
    const newTask = new Task(title, description);

    // Добавляем задачу в массив задач и на доску
    this.tasks.push(newTask);
    this.boardElement.appendChild(newTask.element);

    return newTask;
  }

  removeTask(task) {
    // Удаляем задачу из массива задач и с доски
    const taskIndex = this.tasks.indexOf(task);
    if (taskIndex !== -1) {
      this.tasks.splice(taskIndex, 1);
      task.element.remove();
    }
  }
}

class Task {
  constructor(title, description) {
    // Создаем HTML-элемент задачи
    const taskElement = document.createElement('div');
    taskElement.classList.add('task');
    taskElement.innerHTML = `
      <div class="task-header">
        <h3>${title}</h3>
        <button class="delete-task-btn">Удалить</button>
      </div>
      <p>${description}</p>
    `;

    // Сохраняем свойства задачи
    this.title = title;
    this.description = description;
    this.element = taskElement;

    // Добавляем обработчик события на кнопку удаления задачи
    const deleteTaskBtn = taskElement.querySelector('.delete-task-btn');
    deleteTaskBtn.addEventListener('click', () => {
      taskBoard.removeTask(this);
    });
  }
}