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
	- [6. Play with strings](#6)
	- [7. Copy - Cut - Paste](#7)
	- [8. Create a new sentence](#8)
	- [9. Easter Egg](#9)
	- [10. Linked list cycle](#10)
	- [11. Hello, write](#11)
	- [12. Compile](#12)
	- [13. ByteCode -> Python #1](#13)
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
**6. Play with strings**
- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py "source code") to print `Welcome to Holberton School!`

    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py "here")
    - You are not allowed to use any loops or conditional statements.
    - You have to use the variables `str1` and `str2` in your new line of code
    - Your program should be exactly 5 lines long

    ```
    guillaume@ubuntu:~/py/0x00$ ./6-concat.py
    Welcome to Holberton School!
    guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
    5 6-concat.py
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`6-concat.py`](./6-concat.py)
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Copy - Cut - Paste**
- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py "source code")

    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py "here")
    - You are not allowed to use any loops or conditional statements
    - Your program should be exactly 8 lines long
    - `word_first_3` should contain the first 3 letters of the variable `word`
    - `word_last_2` should contain the last 2 letters of the variable `word`
    - `middle_word` should contain the value of the variable `word` without the first and last letters

    ```
    guillaume@ubuntu:~/py/0x00$ ./7-edges.py
    First 3 letters: Hol
    Last 2 letters: on
    Middle word: olberto
    guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
    8 7-edges.py
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`7-edges.py`](./7-edges.py)
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Create a new sentence**
- Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py "source code") to print `object-oriented programming with Python`, followed by a new line.
    
    - You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py "here")
    - You are not allowed to use any loops or conditional statements
    - Your program should be exactly 5 lines long
    - You are not allowed to create new variables
    - You are not allowed to use string literals
    
    ```
    guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
    object-oriented programming with Python
    guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
    5 8-concat_edges.py
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`8-concat_edges.py`](./8-concat_edges.py)
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Easter Egg**
- Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

    - Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`9-easter_egg.py`](./9-easter_egg.py)
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Linked list cycle**
- **Technical interview preparation**:
    
    - You are not allowed to google anything
    - Whiteboard first
    - This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
    
    Write a function in C that checks if a singly linked list has a cycle in it.
    
    - Prototype: `int check_cycle(listint_t *list);`
    - Return: `0` if there is no cycle, `1` if there is a cycle
    
    Requirements:
    
    - Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `` `free` ``
        
```
carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle        
```

> Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`10-check_cycle.c`](./10-check_cycle.c)
	- Header file: [`lists.h`](./lists.h)
	- Supporting file: [`10-linked_lists.c`](./10-linked_lists.c)
	- Example file: [`10-main.c`](./10-main.c)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Hello, write**
- Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

    - Use the function `write` from the `sys` module
    - You are not allowed to use `print`
    - Your script should print to `stderr`
    - Your script should exit with the status code `1`

```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`100-write.py`](./100-write.py)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Compile**
- Write a script that compiles a Python script file.    
- The Python file name will be stored in the environment variable `$PYFILE`    
- The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` \=> output filename: `my_main.pyc`)
    

```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
```
<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`101-compile`](./101-compile)
	- Example file: [`main.py`](./main.py)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. ByteCode -> Python #1**
- Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

    ```
      3           0 LOAD_CONST               1 (98)
                  3 LOAD_FAST                0 (a)
                  6 LOAD_FAST                1 (b)
                  9 BINARY_POWER
                 10 BINARY_ADD
                 11 RETURN_VALUE
    ```

    - Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html "Python bytecode")

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x00-python-hello_world`
    - File: [`102-magic_calculation.py`](./102-magic_calculation.py)
---

<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
