const addBtn = document.getElementById("addBtn").addEventListener("click", createNewTask)
const list = document.getElementById("List");
const tasks = [];
const solved = [];

function createNewTask(){
  let taskToBeCreated = document.getElementById("InputTask").value;

  if(taskToBeCreated){
    
  let newTask = {
    "message": taskToBeCreated,
    "solved": false,
    "id": "task" + Date.now(),
  };

  let task = tasks.push(newTask);

  syncTask(tasks[task-1]);  

  document.getElementById("InputTask").value = ""

  };

};

function syncTask(task){

  if(task.solved){
    list.querySelector(`#${task.id}`).remove();
  }

  if(!task.solved){
  list.innerHTML += `<li class="hover:text-red-500" id="${task.id}" onclick="removeTask(${task.id})">${task.message}</id>`
  }


};

function removeTask(taskId){ 
  
  let id = taskId.id;

  let findTask = tasks.find(tsk => tsk.id === id)

  findTask.solved = true;
  solved.push(findTask)
  syncTask(findTask)
  
  let remove = tasks.indexOf(findTask)
  tasks.splice(remove, 1)

}
