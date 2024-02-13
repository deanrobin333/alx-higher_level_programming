# Project 
## **p**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Print a list of integers](#0)
	- [1. Secure access to an element in a list](#1)
	- [2. Replace element](#2)
	- [3. Print a list of integers... in reverse!](#3)
	- [4. Replace in a copy](#4)
	- [5. Can you C me now?](#5)
	- [6. Lists of lists = Matrix](#6)
	- [7. Tuples addition](#7)
	- [8. More returns!](#8)
	- [9. Find the max](#9)
	- [10. Only by 2](#10)
	- [11. Delete at](#11)
	- [12. Switch](#12)
	- [13. Linked list palindrome](#13)
	- [14. CPython #0: Python lists](#14)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### C

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl "betty-style.pl") and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl "betty-doc.pl")
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. Print a list of integers**
- Write a function that prints all integers of a list.

    - Prototype: `def print_list_integer(my_list=[]):`
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

```
guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [`0-print_list_integer.py`](./0-print_list_integer.py)
    - Example file: [`0-main.py`](./0-main.py)
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Secure access to an element in a list**
- Write a function that retrieves an element from a list like in C.

    - Prototype: `def element_at(my_list, idx):`
    - If `idx` is negative, the function should return `None`
    - If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
    - You are not allowed to import any module
    - You are not allowed to use `try/except`

```
guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [`1-element_at.py`](./1-element_at.py)
    - Example file: [`1-main.py`](./1-main.py)
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Replace element**
- Write a function that replaces an element of a list at a specific position (like in C).

    - Prototype: `def replace_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should not modify anything, and returns the original list
    - If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
    - You are not allowed to import any module
    - You are not allowed to use `try/except`

```
guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [`2-replace_in_list.py`](./2-replace_in_list.py)
    - Example file: [`2-main.py`](./2-main.py)
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. Print a list of integers... in reverse!**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Replace in a copy**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Can you C me now?**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Lists of lists = Matrix**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Tuples addition**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. More returns!**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Find the max**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Only by 2**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Delete at**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Switch**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. Linked list palindrome**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. CPython #0: Python lists**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x03-python-data_structures`
    - File: [``](./)
    - Example file: [`-main.py`](./-main.py)
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
