# Project: 0x0C. Python - Almost a circle

## Resources

#### Read or watch:

* [args/kwargs](https://intranet.alxswe.com/rltoken/7gc6UzxSL81HcuAwklUbuQ)  
* [JSON encoder and decoder](https://intranet.alxswe.com/rltoken/rGVU9mt57rVURGnjK6n4_Q)
* [unittest module](https://intranet.alxswe.com/rltoken/soictNXCPE18ASL3INoeew)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/uI9iskBCcNo5pc7j9Vy86A)
## Learning Objectives

### General

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# Requirements
## Python Scripts
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/python3```
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version ```2.8.*```)
* All your files must be executable
* The length of your files will be tested using ```wc```
* All your modules should be documented: ```python3 -c 'print(__import__("my_module").__doc__)'```
* All your classes should be documented: ```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```
* All your functions (inside and outside a class) should be documented: ```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Python Unit Tests
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files should end with a new line
* All your test files should be inside a folder ```tests```
* You have to use the [unittest module](https://intranet.alxswe.com/rltoken/soictNXCPE18ASL3INoeew)
* All your test files should be python files (extension: ```.py```)
* All your test files and folders should start with ```test_```
* Your file organization in the tests folder should be the same as your project: ex: for ```models/base.py```, unit tests must be in: ```tests/test_models/test_base.py```
* All your tests should be executed by using this command: ```python3 -m unittest discover tests```
* You can also test file by file by using this command: ```python3 -m unittest tests/test_models/test_base.py```
* We strongly encourage you to work together on test cases so that you don’t miss any edge case

## Tasks

| Task | File |
| ---- | ---- |
| 0. If it's not tested it doesn't work | [tests/](./tests/) |
| 1. Base class | [models/base.py, models/__init__.py](./models/base.py, models/__init__.py) |
| 2. First Rectangle | [models/rectangle.py](./models/rectangle.py) |
| 3. Validate attributes | [models/rectangle.py](./models/rectangle.py) |
| 4. Area first | [models/rectangle.py](./models/rectangle.py) |
| 5. Display #0 | [models/rectangle.py](./models/rectangle.py) |
| 6. __str__ | [models/rectangle.py](./models/rectangle.py) |
| 7. Display #1 | [models/rectangle.py](./models/rectangle.py) |
| 8. Update #0 | [models/rectangle.py](./models/rectangle.py) |
| 9. Update #1 | [models/rectangle.py](./models/rectangle.py) |
| 10. And now, the Square! | [models/square.py](./models/square.py) |
| 11. Square size | [models/square.py](./models/square.py) |
| 12. Square update | [models/square.py](./models/square.py) |
| 13. Rectangle instance to dictionary representation | [models/rectangle.py](./models/rectangle.py) |
| 14. Square instance to dictionary representation | [models/square.py](./models/square.py) |
| 15. Dictionary to JSON string | [models/base.py](./models/base.py) |
| 16. JSON string to file | [models/base.py](./models/base.py) |
| 17. JSON string to dictionary | [models/base.py](./models/base.py) |
| 18. Dictionary to Instance | [models/base.py](./models/base.py) |
| 19. File to instances | [models/base.py](./models/base.py) |
