function addTask() {
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value;

    if (task === "") {
        alert("Task cannot be empty!");
        return;
    }

    // Send the task to the backend
    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ task: task }),
    })
    .then(response => response.json())
    .then(data => {
        updateTaskList(data.tasks);
        taskInput.value = '';  // Clear input field
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateTaskList(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = "";  // Clear the list
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.textContent = task;
        taskList.appendChild(li);
    });
}

function fetchTasks() {
    fetch('/get_tasks')
        .then(response => response.json())
        .then(data => updateTaskList(data.tasks))
        .catch(error => console.error('Error:', error));
}

// Fetch tasks when the page loads
document.addEventListener('DOMContentLoaded', fetchTasks);