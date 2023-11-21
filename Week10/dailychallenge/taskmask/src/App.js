import React, { createContext, useContext, useReducer, useRef, useState } from "react";
import "./App.css";

// Context for managing tasks
const TaskContext = createContext();

// Actions
const ADD_TASK = "ADD_TASK";
const COMPLETE_TASK = "COMPLETE_TASK";
const REMOVE_TASK = "REMOVE_TASK";
const EDIT_TASK = "EDIT_TASK";
const FILTER_TASKS = "FILTER_TASKS";

// Reducer function
function taskReducer(state, action) {
  switch (action.type) {
    case ADD_TASK:
      const newTask = { id: Date.now(), text: action.text, completed: false };
      return [...state, newTask];
    case COMPLETE_TASK:
      return state.map((task) =>
        task.id === action.id ? { ...task, completed: true } : task
      );
    case REMOVE_TASK:
      return state.filter((task) => task.id !== action.id);
    case EDIT_TASK:
      return state.map((task) =>
        task.id === action.id ? { ...task, text: action.text } : task
      );
    case FILTER_TASKS:
      switch (action.filter) {
        case "all":
          return state;
        case "completed":
          return state.filter((task) => task.completed);
        case "active":
          return state.filter((task) => !task.completed);
        default:
          return state;
      }
    default:
      return state;
  }
}

function TaskProvider({ children }) {
  const [tasks, dispatch] = useReducer(taskReducer, []);

  return (
    <TaskContext.Provider value={{ tasks, dispatch }}>
      {children}
    </TaskContext.Provider>
  );
}

function TaskAdder() {
  const { dispatch } = useContext(TaskContext);
  const [taskText, setTaskText] = useState("");

  const handleAddTask = () => {
    if (taskText.trim() === "") return;
    dispatch({ type: ADD_TASK, text: taskText });
    setTaskText("");
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Add a new task"
        value={taskText}
        onChange={(e) => setTaskText(e.target.value)}
      />
      <button onClick={handleAddTask}>Add Task</button>
    </div>
  );
}

function TaskList() {
  const { tasks, dispatch } = useContext(TaskContext);
  const [editingTaskId, setEditingTaskId] = useState(null);
  const editedTaskText = useRef("");

  const handleCompleteTask = (id) => {
    dispatch({ type: COMPLETE_TASK, id });
  };

  const handleRemoveTask = (id) => {
    dispatch({ type: REMOVE_TASK, id });
  };

  const handleEditTask = (task) => {
    setEditingTaskId(task.id);
    editedTaskText.current = task.text;
  };

  const handleSaveEdit = (id) => {
    dispatch({ type: EDIT_TASK, id, text: editedTaskText.current });
    setEditingTaskId(null);
  };

  const handleFilter = (filter) => {
    dispatch({ type: FILTER_TASKS, filter });
  };

  return (
    <div>
      <div>
        <button onClick={() => handleFilter("all")}>Show All</button>
        <button onClick={() => handleFilter("completed")}>Show Completed</button>
        <button onClick={() => handleFilter("active")}>Show Active</button>
      </div>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {editingTaskId === task.id ? (
              <>
                <input
                  type="text"
                  value={editedTaskText.current}
                  onChange={(e) => (editedTaskText.current = e.target.value)}
                />
                <button onClick={() => handleSaveEdit(task.id)}>Save</button>
              </>
            ) : (
              <>
                <input
                  type="checkbox"
                  checked={task.completed}
                  onChange={() => handleCompleteTask(task.id)}
                />
                {task.text}
                <button onClick={() => handleRemoveTask(task.id)}>Remove</button>
                <button onClick={() => handleEditTask(task)}>Edit</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <TaskProvider>
        <h1>Task Manager</h1>
        <TaskAdder />
        <TaskList />
      </TaskProvider>
    </div>
  );
}

export default App;