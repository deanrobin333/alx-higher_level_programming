# Project 
## **0x00. Python - Hello, World**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Run Python file](#0)
	- [1. Run inline](#1)
	- [2. Hello, print](#2)
	- [3. Print integer](#3)
	- [4. Print float](#4)
	- [5. Print string](#5)
	- [](#6)
	- [](#7)
	- [](#8)
	- [](#9)
	- [](#10)
	- [](#11)
	- [](#12)
	- [](#13)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of *this* project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
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
**0. Run Python file**
- Write a Shell script that runs a Python script.
- The Python file name will be saved in the environment variable `` `$PYFILE` ``

```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`0-run`](./0-run)
	- Example file: [`0-main.py`](./0-main.py)
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Run inline**
- Write a Shell script that runs Python code.
- The Python code will be saved in the environment variable `$PYCODE`

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`1-run_inline`](./1-run_inline)
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Hello, print**
- Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

    - Use the function `print`

```
guillaume@ubuntu:~/py/0x00$ ./2-print.py
"Programming is like building a multilingual puzzle
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`2-print.py`](./2-print.py)
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. Print integer**
- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py "here")
    - The output of the script should be:
        - the number, followed by `Battery street`,
        - followed by a new line
    - You are not allowed to cast the variable `number` into a string
    - Your code must be 3 lines long
    - You have to use f-strings [tips](https://realpython.com/python-f-strings/ "tips")

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`3-print_number.py`](./3-print_number.py)
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Print float**
- Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py "here")
    - The output of the program should be:
        - `Float:`, followed by the float with only 2 digits
        - followed by a new line
    - You are not allowed to cast `number` to string
    - You have to use f-strings

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`4-print_float.py`](./4-print_float.py)
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Print string**
- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py "source code") in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py "here")
    - The output of the program should be:
        - 3 times the value of `str`
        - followed by a new line
        - followed by the 9 first characters of `str`
        - followed by a new line
    - You are not allowed to use any loops or conditional statement
    - Your program should be maximum 5 lines long

    ```
    guillaume@ubuntu:~/py/0x00$ ./5-print_string.py
    Holberton SchoolHolberton SchoolHolberton School
    Holberton
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`5-print_string.py`](./5-print_string.py)
---
#### 6
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 7
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 8
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 9
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 10
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 11
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 12
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---
#### 13
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [``](./)
---

<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
