# Project 
## **0x04. Python - More Data Structures: Set, Dictionary**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Squared simple](#0)
	- [1. Search and replace](#1)
	- [2. Unique addition](#2)
	- [3. Present in both](#3)
	- [4. Only differents](#4)
	- [5. Number of keys](#5)
	- [6. Print sorted dictionary](#6)
	- [7. Update dictionary](#7)
	- [8. Simple delete by key](#8)
	- [9. Multiply by 2](#9)
	- [10. Best score](#10)
	- [11. Multiply by using map](#11)
	- [12. Roman to Integer](#12)
	- [13. Weighted average!](#13)
	- [14. Squared by using map](#14)
	- [15. Delete by value](#15)
	- [16. CPython #1: PyBytesObject](#16)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. Squared simple**
- Write a function that computes the square value of all integers of a matrix.

    - Prototype: `def square_matrix_simple(matrix=[]):`
    - `matrix` is a 2 dimensional array
    - Returns a new matrix:
        - Same size as `matrix`
        - Each value should be the square of the value of the input
    - Initial matrix should not be modified
    - You are not allowed to import any module
    - You are allowed to use regular loops, `map`, etc.

```
guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`0-square_matrix_simple.py`](./0-square_matrix_simple.py)
	- Example file: [`0-main.py`](./0-main.py)
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Search and replace**
- Write a function that replaces all occurrences of an element by another in a new list.

    - Prototype: `def search_replace(my_list, search, replace):`
    - `my_list` is the initial list
    - `search` is the element to replace in the list
    - `replace` is the new element
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`1-search_replace.py`](./1-search_replace.py)
	- Example file: [`1-main.py`](./1-main.py)
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Unique addition**
- Write a function that adds all unique integers in a list (only once for each integer).

    - Prototype: `def uniq_add(my_list=[]):`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`2-uniq_add.py`](./2-uniq_add.py)
	- Example file: [`2-main.py`](./2-main.py)
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. Present in both**
- Write a function that returns a set of common elements in two sets.

    - Prototype: `def common_elements(set_1, set_2):`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`3-common_elements.py`](./3-common_elements.py)
	- Example file: [`3-main.py`](./3-main.py)
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Only differents**
- Write a function that returns a set of all elements present in only one set.

    - Prototype: `def only_diff_elements(set_1, set_2):`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`4-only_diff_elements.py`](./4-only_diff_elements.py)
	- Example file: [`4-main.py`](./4-main.py)
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Number of keys**
- Write a function that returns the number of keys in a dictionary.

    - Prototype: `def number_keys(a_dictionary):`
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`5-number_keys.py`](./5-number_keys.py)
	- Example file: [`5-main.py`](./5-main.py)
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Print sorted dictionary**
- Write a function that prints a dictionary by ordered keys.

    - Prototype: `def print_sorted_dictionary(a_dictionary):`
    - You can assume that all keys are strings
    - Keys should be sorted by alphabetic order
    - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
    - Dictionary values can have any type
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`6-print_sorted_dictionary.py`](./6-print_sorted_dictionary.py)
	- Example file: [`6-main.py`](./6-main.py)
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Update dictionary**
- Write a function that replaces or adds key/value in a dictionary.

    - Prototype: `def update_dictionary(a_dictionary, key, value):`
    - `key` argument will be always a string
    - `value` argument will be any type
    - If a key exists in the dictionary, the value will be replaced
    - If a key doesn’t exist in the dictionary, it will be created
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`7-update_dictionary.py`](./7-update_dictionary.py)
	- Example file: [`7-main.py`](./7-main.py)
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Simple delete by key**
- Write a function that deletes a key in a dictionary.

    - Prototype: `def simple_delete(a_dictionary, key=""):`
    - `key` argument will be always a string
    - If a key doesn’t exist, the dictionary won’t change
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`8-simple_delete.py`](./8-simple_delete.py)
	- Example file: [`8-main.py`](./8-main.py)
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Multiply by 2**
- Write a function that returns a new dictionary with all values multiplied by 2

    - Prototype: `def multiply_by_2(a_dictionary):`
    - You can assume that all values are only integers
    - Returns a new dictionary
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`9-multiply_by_2.py`](./9-multiply_by_2.py)
	- Example file: [`9-main.py`](./9-main.py)
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Best score**
- Write a function that returns a key with the biggest integer value.

    - Prototype: `def best_score(a_dictionary):`
    - You can assume that all values are only integers
    - If no score found, return `None`
    - You can assume all students have a different score
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`10-best_score.py`](./10-best_score.py)
	- Example file: [`10-main.py`](./10-main.py)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Multiply by using map**
- Write a function that returns a list with all values multiplied by a number without using any loops.

    - Prototype: `def multiply_list_map(my_list=[], number=0):`
    - Returns a new list:
        - Same length as `my_list`
        - Each value should be multiplied by `number`
    - Initial list should not be modified
    - You are not allowed to import any module
    - You have to use `map`
    - Your file should be max 3 lines

```
guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`11-multiply_list_map.py`](./11-multiply_list_map.py)
	- Example file: [`11-main.py`](./11-main.py)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Roman to Integer**
- **Technical interview preparation**:
    - You are not allowed to google anything
    - Whiteboard first

- Create a function `def roman_to_int(roman_string):` that converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals "Roman numeral") to an integer.
    - You can assume the number will be between 1 to 3999.
    - `def roman_to_int(roman_string)` must return an integer
    - If the `roman_string` is not a string or `None`, return 0

```
guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707

I = 1
III = 3
XXI = 21
CXXIV = 124
89 = 0
None = 0
XCIX = 99
LXXXIX = 89
CMLXXX = 980
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`12-roman_to_int.py`](./12-roman_to_int.py)
	- Example file: [`12-main.py`](./12-main.py)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. Weighted average!**
- Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`

    - Prototype: `def weight_average(my_list=[]):`
    - Returns `0` if the list is empty
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./100-main.py
Average: 2.80
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`100-weight_average.py`](./100-weight_average.py)
	- Example file: [`100-main.py`](./100-main.py)
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. Squared by using map**
- Write a function that computes the square value of all integers of a matrix using `map`

    - Prototype: `def square_matrix_map(matrix=[]):`
    - `matrix` is a 2 dimensional array
    - Returns a new matrix:
        - Same size as `matrix`
        - Each value should be the square of the value of the input
    - Initial matrix should not be modified
    - You are not allowed to import any module
    - You have to use `map`
    - You are not allowed to use `for` or `while`
    - Your file should be max 3 lines

```
guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`101-square_matrix_map.py`](./101-square_matrix_map.py)
	- Example file: [`101-main.py`](./101-main.py)
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. Delete by value**
- Write a function that deletes keys with a specific value in a dictionary.

    - Prototype: `def complex_delete(a_dictionary, value):`
    - If the value doesn’t exist, the dictionary won’t change
    - All keys having the searched value have to be deleted
    - You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`102-complex_delete.py`](./102-complex_delete.py)
	- Example file: [`102-main.py`](./102-main.py)
---
#### 16
###### [Table of Contents](#table-of-contents)
**16. CPython #1: PyBytesObject**
- Create two C functions that print some basic info about Python lists and Python bytes objects.

- Python lists:
	- Prototype: `void print_python_list(PyObject *p);`
	- Format: see example

- Python bytes:
	- Prototype: `void print_python_bytes(PyObject *p);`
	- Format: see example
	- Line “first X bytes”: print a maximum of 10 bytes
	- If `p` is not a valid `PyBytesObject`, print an error message (see example)
	- Read `/usr/include/python3.4/bytesobject.h`

- About:
	- Python version: 3.4
	- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
	- You are not allowed to use the following macros/functions:
		- `Py_SIZE`
		- `Py_TYPE`
		- `PyList_GetItem`
		- `PyBytes_AS_STRING`
		- `PyBytes_GET_SIZE`

```
julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ python3 103-tests.py
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
julien@ubuntu:~/CPython$
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [`103-python.c`](./103-python.c)
    - Example file: [`103-test.py`](./103-test.py)
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
