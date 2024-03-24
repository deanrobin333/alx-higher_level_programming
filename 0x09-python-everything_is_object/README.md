# Project
## **0x09. Python - Everything is object**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Who am I?](#0)
	- [1. Where are you?](#1)
	- [2. Right count](#2)
	- [3. Right count =](#3)
	- [4. Right count =](#4)
	- [5. Right count =+](#5)
	- [6. Is equal](#6)
	- [7. Is the same](#7)
	- [8. Is really equal](#8)
	- [9. Is really the same](#9)
	- [10. And with a list, is it equal](#10)
	- [11. And with a list, is it the same](#11)
	- [12. And with a list, is it really equal](#12)
	- [13. And with a list, is it really the same](#13)
	- [14. List append](#14)
	- [15. List add](#15)
	- [16. Integer incrementation](#16)
	- [17. List incrementation](#17)
	- [18. List assignation](#18)
	- [19. Copy a list object](#19)
	- [20. Tuple or not?](#20)
	- [21. Tuple or not?](#21)
	- [22. Tuple or not?](#22)
	- [23. Tuple or not?](#23)
	- [24. Who I am?](#24)
	- [25. Tuple or not](#25)
	- [26. Empty is not empty](#26)
	- [27. Still the same?](#27)
	- [28. Same or not?](#28)
	- [29. #pythonic](#29)
	- [30. Low memory cost](#30)
	- [31. int 1/3](#31)
	- [32. int 2/3](#32)
	- [33. int 3/3](#33)
	- [34. Clear strings](#34)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### `.txt` Answer Files

- Only one line
- No Shebang
- All your files should end with a new line

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. Who am I?**

- What function would you use to get the type of an object?

- Write the name of the function in the file, without `()`.


<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`0-answer.txt`](./0-answer.txt)
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Where are you?**

- How do you get the variable identifier (which is the memory address in the CPython implementation)?

- Write the name of the function in the file, without `()`.


<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`1-answer.txt`](./1-answer.txt)
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Right count**

- In the following code, do `a` and `b` point to the same object?
Answer with Yes or No.

```
>>> a = 89

>>> b = 100
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`2-answer.txt`](./2-answer.txt)
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. Right count =**

- In the following code, do `a` and `b` point to the same object?
Answer with Yes or No.

```
>>> a = 89

>>> b = 89
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`3-answer.txt`](./3-answer.txt)
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Right count =**

- In the following code, do `a` and `b` point to the same object?
Answer with Yes or No.

```
>>> a = 89

>>> b = a
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`4-answer.txt`](./4-answer.txt)
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Right count =+**

- In the following code, do `a` and `b` point to the same object?
Answer with Yes or No.

```
>>> a = 89

>>> b = a + 1
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`5-answer.txt`](./5-answer.txt)
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Is equal**

- What do these 3 lines print?

```
>>> s1 = "Best School"

>>> s2 = s1
>>> print(s1 == s2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`6-answer.txt`](./6-answer.txt)
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Is the same**

- What do these 3 lines print?

```
>>> s1 = "Best"

>>> s2 = s1
>>> print(s1 is s2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`7-answer.txt`](./7-answer.txt)
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Is really equal**

- What do these 3 lines print?

```
>>> s1 = "Best School"

>>> s2 = "Best School"
>>> print(s1 == s2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`8-answer.txt`](./8-answer.txt)
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Is really the same**

- What do these 3 lines print?

```
>>> s1 = "Best School"

>>> s2 = "Best School"
>>> print(s1 is s2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`9-answer.txt`](./9-answer.txt)
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. And with a list, is it equal**

- What do these 3 lines print?

```
>>> l1 = [1, 2, 3]

>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`10-answer.txt`](./10-answer.txt)
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. And with a list, is it the same**

- What do these 3 lines print?

```
>>> l1 = [1, 2, 3]

>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`11-answer.txt`](./11-answer.txt)
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. And with a list, is it really equal**

- What do these 3 lines print?

```
>>> l1 = [1, 2, 3]

>>> l2 = l1
>>> print(l1 == l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`12-answer.txt`](./12-answer.txt)
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. And with a list, is it really the same**

- What do these 3 lines print?

```
>>> l1 = [1, 2, 3]

>>> l2 = l1
>>> print(l1 is l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`13-answer.txt`](./13-answer.txt)
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. List append**

- What does this script print?

```
l1 = [1, 2, 3]

l2 = l1
l1.append(4)
print(l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`14-answer.txt`](./14-answer.txt)
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. List add**

- What does this script print?

```
l1 = [1, 2, 3]

l2 = l1
l1 = l1 + [4]
print(l2)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`15-answer.txt`](./15-answer.txt)
---
#### 16
###### [Table of Contents](#table-of-contents)
**16. Integer incrementation**

- What does this script print?

```
def increment(n):

    n += 1

a = 1
increment(a)
print(a)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`16-answer.txt`](./16-answer.txt)
---
#### 17
###### [Table of Contents](#table-of-contents)
**17. List incrementation**

- What does this script print?

```
def increment(n):

    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`17-answer.txt`](./17-answer.txt)
---
#### 18
###### [Table of Contents](#table-of-contents)
**18. List assignation**

- What does this script print?

```
def assign_value(n, v):

    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`18-answer.txt`](./18-answer.txt)
---
#### 19
###### [Table of Contents](#table-of-contents)
**19. Copy a list object**

- Write a function `def copy_list(l):` that returns a copy of a list.


   - The input list can contain any type of objects
   - Your file should be maximum 3-line long (no documentation needed)
   - You are not allowed to import any module


```
guillaume@ubuntu:~/0x09$ cat 19-main.py

#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`19-copy_list.py`](./19-copy_list.py)
---
#### 20
###### [Table of Contents](#table-of-contents)
**20. Tuple or not?**

a = ()


- Is `a` a tuple? Answer with `Yes` or `No`.

```
a = (1)

b = (1)
a is b
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`20-answer.txt`](./20-answer.txt)
---
#### 21
###### [Table of Contents](#table-of-contents)
**21. Tuple or not?**

a = (1, 2)


- Is `a` a tuple? Answer with `Yes` or `No`.

```
a = (1, 2)

b = (1, 2)
a is b
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`21-answer.txt`](./21-answer.txt)
---
#### 22
###### [Table of Contents](#table-of-contents)
**22. Tuple or not?**

a = (1)


- Is `a` a tuple? Answer with `Yes` or `No`.

```
a = ()

b = ()
a is b
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`22-answer.txt`](./22-answer.txt)
---
#### 23
###### [Table of Contents](#table-of-contents)
**23. Tuple or not?**

a = (1, )


- Is `a` a tuple? Answer with `Yes` or `No`.

```
guillaume@ubuntu:~/0x09$ cat 100-main.py

#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`23-answer.txt`](./23-answer.txt)
---
#### 24
###### [Table of Contents](#table-of-contents)
**24. Who I am?**

- What does this script print?

```
guillaume@ubuntu:~/0x09$ cat 101-main.py

#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`24-answer.txt`](./24-answer.txt)
---
#### 25
###### [Table of Contents](#table-of-contents)
**25. Tuple or not**

- What does this script print?

```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`25-answer.txt`](./25-answer.txt)
---
#### 26
###### [Table of Contents](#table-of-contents)
**26. Empty is not empty**

- What does this script print?

```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`26-answer.txt`](./26-answer.txt)
---
#### 27
###### [Table of Contents](#table-of-contents)
**27. Still the same?**

>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)


- Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`27-answer.txt`](./27-answer.txt)
---
#### 28
###### [Table of Contents](#table-of-contents)
**28. Same or not?**

>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)


- Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`28-answer.txt`](./28-answer.txt)
---
#### 29
###### [Table of Contents](#table-of-contents)
**29. #pythonic**

- Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):


   - Format: see example
   - Your file should be maximum 4-line long (no documentation needed)
   - You are not allowed to import any module


```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`100-magic_string.py`](./100-magic_string.py)
---
#### 30
###### [Table of Contents](#table-of-contents)
**30. Low memory cost**

- Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.


   - You are not allowed to import any module


```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`101-locked_class.py`](./101-locked_class.py)
---
#### 31
###### [Table of Contents](#table-of-contents)
**31. int 1/3**

julien@ubuntu:/python3$ cat int.py
a = 1
b = 1
julien@ubuntu:/python3$


- Assuming we are using a CPython implementation of Python3 with default options/configuration:


   - How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
   - How many int objects are created by the execution of the second line of the script (`103-line2.txt`)


```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`103-line1.txt`](./103-line1.txt)
    - File: [`103-line2.txt`](./103-line2.txt)
---
#### 32
###### [Table of Contents](#table-of-contents)
**32. int 2/3**

julien@ubuntu:/python3$ cat int.py
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$


- Assuming we are using a CPython implementation of Python3 with default options/configuration:


   - How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
   - How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
   - After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (`104-line3.txt`)
   - After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
   - How many int objects are created by the execution of the last line of the script (`104-line5.txt`)


```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`104-line1.txt`](./104-line1.txt)
    - File: [`104-line2.txt`](./104-line2.txt)
    - File: [`104-line3.txt`](./104-line3.txt)
    - File: [`104-line4.txt`](./104-line4.txt)
    - File: [`104-line5.txt`](./104-line5.txt)
---
#### 33
###### [Table of Contents](#table-of-contents)
**33. int 3/3**

julien@twix:/tmp/so$ cat int.py
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$


- Assuming we are using a CPython implementation of Python3 with default options/configuration:


   - Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)
   - Why? (optional blog post :))


- Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS`

- 

```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`105-line1.txt`](./105-line1.txt)
---
#### 34
###### [Table of Contents](#table-of-contents)
**34. Clear strings**

guillaume@ubuntu:/python3$ cat string.py
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$


- Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):


   - How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
   - How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
   - After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
   - After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
   - How many string objects are created by the execution of the last line of the script (`106-line5.txt`)


```

<br></br>
- Repo
    - GitHub repository: `alx-higher_level_programming`
    - Directory: `0x09-python-everything_is_object`
    - File: [`106-line1.txt`](./106-line1.txt)
    - File: [`106-line2.txt`](./106-line2.txt)
    - File: [`106-line3.txt`](./106-line3.txt)
    - File: [`106-line4.txt`](./106-line4.txt)
    - File: [`106-line5.txt`](./106-line5.txt)
---


<br></br>
<div align="right">
    <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
