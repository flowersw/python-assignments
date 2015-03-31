# Web calculator

## Description

Create a simple web-based calculator.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* The very basics of making a web application

### Performance Objectives

After completing this assignment, you should be able to:

* Create a web (Flask or Django) app

## Details

### Deliverables

* A Git repo called web-calculator containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Create a simple web application that works as a calculator. The first page, which you get to via a GET request to `/`, should have a form with two text boxes, a dropdown box for the operation (+, -, *, /) and a button to calculate.

The form uses POST to go to a second page at `/calc` which shows the results of your calculation.

## Hard Mode

In addition to the requirements from **Normal Mode**:

1. The form should also appear on the second page -- the calculation results page. The first operand should be filled in with the results of the previous calculation.

2. Add [Foundation](http://foundation.zurb.com/) or [Bootstrap](http://getbootstrap.com/) to your application to make it look nicer.

## Additional Resources

* [Full Stack Python](http://www.fullstackpython.com/)
* [Django documentation](https://docs.djangoproject.com/en/1.7/)
* [The main Flask site](http://flask.pocoo.org/)
* [Explore Flask](https://exploreflask.com/)

