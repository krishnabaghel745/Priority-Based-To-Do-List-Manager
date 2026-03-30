import streamlit as st
from src.task_manager import load_tasks, add_task, delete_task, complete_task

st.title("📝 Priority To-Do List")

# Add Task
task_input = st.text_input("Enter Task")
priority = st.selectbox("Select Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if task_input:
        add_task(task_input, priority)
        st.success("Task added!")
    else:
        st.warning("Please enter a task")

# Display Tasks
tasks = load_tasks()

st.subheader("Your Tasks")

for i, task in enumerate(tasks):
    col1, col2, col3, col4 = st.columns([3,1,1,1])

    with col1:
        status = "✅" if task["completed"] else "❌"
        st.write(f"{status} {task['task']}")

    with col2:
        st.write(task["priority"])

    with col3:
        if st.button("Done", key=f"done{i}"):
            complete_task(i)

    with col4:
        if st.button("Delete", key=f"del{i}"):
            delete_task(i)