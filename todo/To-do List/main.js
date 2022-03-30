const addBtn = document.getElementById("addBtn").addEventListener("click", createNewTask)
const list = document.getElementById("List");
const tasks = [];
const solved = [];

function createNewTask(){
  let taskToBeCreated = document.getElementById("InputTask").value;
  let newTask = {
    "message": taskToBeCreated,
    "solved": false,
    "id": taskToBeCreated.split(" ")[0]
  };

  let task = tasks.push(newTask);
  syncTask(tasks[task-1]);
};

function syncTask(task){

  if(!task.solved){
  list.innerHTML += `<li class="hover:text-red-500" id="${task.id}" onclick="removeTask(${task.id})">${task.message}</id>`
  };


};

function removeTask(taskId){ 
  console.log(taskId.id)
  let findTask = tasks.find(a => a.id === taskId.id)
  console.log(findTask)
  findTask.solved = true;
  solved.push(findTask)
  
  let remove = tasks.indexOf(findTask)
  tasks.splice(remove, 1)

  console.table(tasks)
}
