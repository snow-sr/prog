const addBtn = document.getElementById("addBtn").addEventListener("click", createNewTask)
const list = document.getElementById("List");
const tasks = [];
const solved = [];


//Takes the input value and creates a task with it, creates the task at array and rund syncTask()
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


//Read the tasks array and create the elements at HTML @task = Text to be created as a task
function syncTask(task){

  if(task.solved){
    list.querySelector(`#${task.id}`).remove();
  }

  if(!task.solved){
  list.innerHTML += `<li class="hover:text-red-500" id="${task.id}" onclick="removeTask(${task.id})">${task.message}</id>`
  }


};


//Finds and remove the element searched  @taskId = Id of the task you're trying to remove
function removeTask(taskId){ 
  
  let id = taskId.id;

  let findTask = tasks.find(tsk => tsk.id === id)

  findTask.solved = true;
  solved.push(findTask)
  syncTask(findTask)
  
  let remove = tasks.indexOf(findTask)
  tasks.splice(remove, 1)

}


//Listening to ENTER to create a new task without using forms
document.addEventListener ('keypress', (event) => {
  const keyName = event.key;
  if(keyName == "Enter"){
    createNewTask()
  }
});
