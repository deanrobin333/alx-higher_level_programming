# Project 
## **0x01. Python - if/else, loops, functions**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Positive anything is better than negative nothing](#0)
	- [1. The last digit](#1)
	- [2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](#2)
	- [3. When I was having that alphabet soup, I never thought that it would pay off](#3)
	- [4. Hexadecimal printing](#4)
	- [5. 00...99](#5)
	- [6. Inventing is a combination of brains and materials. The more brains you use, the less material you need](#6)
	- [7. islower](#7)
	- [8. To uppercase](#8)
	- [9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important](#9)
	- [10. a + b](#10)
	- [11. a ^ b](#11)
	- [12. Fizz Buzz](#12)
	- [13. Insert in sorted linked list](#13)
	- [14. Smile in the mirror](#14)
	- [15. Remove at position](#15)
	- [16. ByteCode -> Python #2](#16)
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
**0. Positive anything is better than negative nothing**
- This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

    - You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py "here")
    - The variable `number` will store a different value every time you will run this program
    - You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
    - The output of the program should be:
        - The number, followed by
            - if the number is greater than 0: `is positive`
            - if the number is 0: `is zero`
            - if the number is less than 0: `is negative`
        - followed by a new line

```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
10 is positive
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`0-positive_or_negative.py`](./0-positive_or_negative.py)
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. The last digit**
- This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

    - You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py "here")
    - The variable `number` will store a different value every time you will run this program
    - You don’t have to understand what `import`, `random.randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
    - The output of the program should be:
        - The string `Last digit of`, followed by
        - the number, followed by
        - the string `is`, followed by the last digit of `number`, followed by
            - if the last digit is greater than 5: the string `and is greater than 5`
            - if the last digit is 0: the string `and is 0`
            - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
        - followed by a new line

    ```
    guillaume@ubuntu:~/0x01$ ./1-last_digit.py
    Last digit of 4205 is 5 and is less than 6 and not 0
    guillaume@ubuntu:~/0x01$ ./1-last_digit.py
    Last digit of -9200 is 0 and is 0
    guillaume@ubuntu:~/0x01$ ./1-last_digit.py
    Last digit of 5247 is 7 and is greater than 5
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`1-last_digit.py`](./1-last_digit.py)
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
- Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

    - You can only use one `print` function with string format
    - You can only use one loop in your code
    - You are not allowed to store characters in a variable
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`2-print_alphabet.py`](./2-print_alphabet.py)
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. When I was having that alphabet soup, I never thought that it would pay off**
- Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

    - Print all the letters except `q` and `e`
    - You can only use one `print` function with string format
    - You can only use one loop in your code
    - You are not allowed to store characters in a variable
    - You are not allowed to import any module

    ```
    guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
    abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
    ```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`3-print_alphabt.py`](./3-print_alphabt.py)
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Hexadecimal printing**
- Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

    - You can only use one `print` function with string format
    - You can only use one loop in your code
    - You are not allowed to store numbers or strings in a variable
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
...
96 = 0x60
97 = 0x61
98 = 0x62
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`4-print_hexa.py`](./4-print_hexa.py)
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. 00...99**
- Write a program that prints numbers from `0` to `99`.

    - Numbers must be separated by `,`, followed by a space
    - Numbers should be printed in ascending order, with two digits
    - The last number should be followed by a new line
    - You can only use no more than 2 `print` functions with string format
    - You can only use one loop in your code
    - You are not allowed to store numbers or strings in a variable
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`5-print_comb2.py`](./5-print_comb2.py)
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
- Write a program that prints all possible different combinations of two digits.
    
    - Numbers must be separated by `,`, followed by a space
    - The two digits must be different
    - `01` and `10` are considered the same combination of the two digits `0` and `1`
    - Print only the smallest combination of two digits
    - Numbers should be printed in ascending order, with two digits
    - The last number should be followed by a new line
    - You can only use no more than 3 `print` functions with string format
    - You can only use no more than 2 loops in your code
    - You are not allowed to store numbers or strings in a variable
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`6-print_comb3.py`](./6-print_comb3.py)
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. islower**
- Write a function that checks for lowercase character.

    - Prototype: `def islower(c):`
    - Returns `True` if `c` is lowercase
    - Returns `False` otherwise
    - You are not allowed to import any module
    - You are not allowed to use `str.upper()` and `str.isupper()`
    - [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord "Tips: ord()")
- You don’t need to understand `__import__`

```
guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`7-islower.py`](./7-islower.py)
    - Example file: [`7-main.py`](./7-main.py)
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. To uppercase**
- Write a function that prints a string in uppercase followed by a new line.
    
    - Prototype: `def uppercase(str):`
    - You can only use no more than 2 `print` functions with string format
    - You can only use one loop in your code
    - You are not allowed to import any module
    - You are not allowed to use `str.upper()` and `str.isupper()`
    - [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord "Tips: ord()")
- You don’t need to understand `__import__`
    
```
guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`8-uppercase.py`](./8-uppercase.py)
    - Example file: [`8-main.py`](./8-main.py)
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important**
- Write a function that prints the last digit of a number.
    
    - Prototype: `def print_last_digit(number):`
    - Returns the value of the last digit
    - You are not allowed to import any module
- You don’t need to understand `__import__`
    
```
guillaume@ubuntu:~/0x01$ ./9-main.py
8044
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`9-print_last_digit.py`](./9-print_last_digit.py)
    - Example file: [`9-main.py`](./9-main.py)
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. a + b**
- Write a function that adds two integers and returns the result.
    
    - Prototype: `def add(a, b):`
    - Returns the value of `a + b`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`10-add.py`](./10-add.py)
    - Example file: [`10-main.py`](./10-main.py)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. a ^ b**
- Write a function that computes `a` to the power of `b` and return the value.
    
    - Prototype: `def pow(a, b):`
    - Returns the value of `a ^ b`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`11-pow.py`](./11-pow.py)
    - Example file: [`11-main.py`](./11-main.py)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Fizz Buzz**
- Write a function that prints the numbers from 1 to 100 separated by a space.
    
    - For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
    - For numbers which are multiples of both three and five print `FizzBuzz`.
    - Prototype: `def fizzbuzz():`
    - Each element should be followed by a space
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
```
<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`12-fizzbuzz.py`](./12-fizzbuzz.py)
    - Example file: [`12-main.py`](./12-main.py)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. Insert in sorted linked list**
- **Technical interview preparation**:    
    - You are not allowed to google anything
    - Whiteboard first    
- Write a function in C that inserts a number into a sorted singly linked list.    
    - Prototype: `listint_t *insert_node(listint_t **head, int number);`
    - Return: the address of the new node, or `NULL` if it failed

```
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`13-insert_number.c`](./13-insert_number.c)
    - Header File: [`lists.h`](./lists.h)
    - Supporting File: [`linked_lists.c`](./linked_lists.c)
    - Example file: [`13-main.c`](./13-main.c)
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. Smile in the mirror**
- Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
    
    - You can only use one `print` function with string format
    - You can only use one loop in your code
    - You are not allowed to store characters in a variable
    - You are not allowed to import any module
    
```
guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`100-print_tebahpla.py`](./100-print_tebahpla.py)
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. Remove at position**
- Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).

    - Prototype: `def remove_char_at(str, n):`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`101-remove_char_at.py`](./101-remove_char_at.py)
    - Example file: [`101-main.py`](./101-main.py)
---
#### 16
###### [Table of Contents](#table-of-contents)
**16. ByteCode -> Python #2**
- Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:

    ```
      3           0 LOAD_FAST                0 (a)
                  3 LOAD_FAST                1 (b)
                  6 COMPARE_OP               0 (<)
                  9 POP_JUMP_IF_FALSE       16

      4          12 LOAD_FAST                2 (c)
                 15 RETURN_VALUE

      5     >>   16 LOAD_FAST                2 (c)
                 19 LOAD_FAST                1 (b)
                 22 COMPARE_OP               4 (>)
                 25 POP_JUMP_IF_FALSE       36

      6          28 LOAD_FAST                0 (a)
                 31 LOAD_FAST                1 (b)
                 34 BINARY_ADD
                 35 RETURN_VALUE

      7     >>   36 LOAD_FAST                0 (a)
                 39 LOAD_FAST                1 (b)
                 42 BINARY_MULTIPLY
                 43 LOAD_FAST                2 (c)
                 46 BINARY_SUBTRACT
                 47 RETURN_VALUE
    ```

    [tips - ByteCode](https://docs.python.org/3.4/library/dis.html "tips - ByteCode")

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x01-python-if_else_loops_functions`
    - File: [`102-magic_calculation.py`](./102-magic_calculation.py)
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
