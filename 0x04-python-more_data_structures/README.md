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

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Multiply by using map**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Roman to Integer**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. Weighted average!**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. Squared by using map**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. Delete by value**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---
#### 16
###### [Table of Contents](#table-of-contents)
**16. CPython #1: PyBytesObject**

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x04-python-more_data_structures`
    - File: [``](./)
	- Example file: [`-main.py`](./-main.py)
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
