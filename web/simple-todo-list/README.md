# Simple Todo List

## Description

Create a simple web-based todo list. This is a two-day assignment.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Simple database usage
* Testing web applications

## Details

### Deliverables

* A Git repo called simple-todo-list containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Day 1

### Normal Mode

Create a simple todo list that looks similar to the following:

![wireframe](todo.png)

You will need to handle three situations:

* Showing the main todo list
* Submitting a new todo
* Deleting checked todos

The new todo form and current todos form should be separate HTML forms.

Your application should be tested.

### Hard Mode

In addition to the requirements from **Normal Mode**:

* Add in a way to edit current todos.
* Change the behavior from deleting checked todos to marking them as done and removing them from the page. Then add a new page to show completed todos.

## Day 2

### Normal Mode

First, finish Hard Mode for day 1.

Then:

* Add a new field to todos for the due date. This field is not required when creating or editing a todo.
* If a todo is overdue, display that fact somehow. You can emphasize the todo, use a color or text label, or something else.
* Sort the todos by due date descending. The ones without a due date can be on either side of the rest of them.
* Sort the completed todos by date completed descending.

### Hard Mode

* Research foreign keys and relationships between models. Create a Note model and allow notes to be added to todos. You will likely want to make a page for each todo to show all the notes and add new ones.
