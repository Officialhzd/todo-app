# 📝 Command-Line To-Do List App

A simple, powerful command-line To-Do application built with Python. This app allows you to manage daily tasks with ease—add, view, and delete tasks grouped by creation date—all from your terminal.

Styled with the beautiful `rich` library for better readability and user experience.

---

## 🚀 Features

- ✅ Add tasks with a required title and optional description.
- 📅 Assign due dates with automatic validation.
- 📂 Group tasks by the day they were added.
- 🗂 View all tasks for today or a specific day.
- ⏰ Highlights tasks due today or overdue.
- ❌ Delete specific tasks by ID.
- 🧹 Delete all tasks for a particular day.
- 💾 Tasks persist between sessions via a local `tasks.json` file.

---

## 📦 Requirements

- Python 3.8+
- [`rich`](https://github.com/Textualize/rich)

Install required packages with:

```bash
pip install rich
```

## 📁 Project Structure

.
├── main.py         # Main CLI interface
├── storage.py      # Handles saving/loading task data
├── todo.py         # Task structure and validation
├── tasks.json      # Auto-generated data file
└── README.md       # You're here!


## 💡 Tips
Tasks are grouped and displayed by creation date.

Task IDs are assigned alphabetically (A, B, C... AA, AB, etc).

Use due dates to get reminders for what’s urgent.

Don't forget to install rich for a better UI experience.


## 🧠 Future Improvements (Optional Ideas)
 Add task completion marking.

 Add priority levels.

 Export tasks to CSV or PDF.

 Search tasks by keyword.


Crafted with simplicity and clarity in mind.
Enjoy managing your day from the terminal ✨

## 📄 License
This project is open source and free to use.
