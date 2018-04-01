# Python Directory and Files Management

If there are a large number of [files to handle](https://www.programiz.com/python-programming/file-operation) in your Python program, you can arrange your code within different directories to make things more manageable.

A directory or folder is a collection of files and sub directories. Python has the `os` [module](https://www.programiz.com/python-programming/modules), which provides us with many useful methods to work with directories (and files as well).

## Get Current Directory

We can get the present working directory using the `getcwd()` method.

This method returns the current working directory in the form of a string. We can also use the `getcwdb()` method to get it as bytes object.

```python
>>> import os

>>> os.getcwd()
'C:\\Program Files\\PyScripter'

>>> os.getcwdb()
b'C:\\Program Files\\PyScripter'
```

The extra backslash implies escape sequence. The `print()` function will render this properly.

```python
>>> print(os.getcwd())
C:\Program Files\PyScripter
```

## Changing Directory

We can change the current working directory using the `chdir()` method.

The new path that we want to change to must be supplied as a string to this method. We can use both forward slash (/) or the backward slash (\) to separate path elements.

It is safer to use escape sequence when using the backward slash.

```python
>>> os.chdir('C:\\Python33')

>>> print(os.getcwd())
C:\Python33
```

## List Directories and Files

All files and sub directories inside a directory can be known using the `listdir()` method.

This method takes in a path and returns a list of sub directories and files in that path. If no path is specified, it returns from the current working directory.

```python
>>> print(os.getcwd())
C:\Python33

>>> os.listdir()
['DLLs',
'Doc',
'include',
'Lib',
'libs',
'LICENSE.txt',
'NEWS.txt',
'python.exe',
'pythonw.exe',
'README.txt',
'Scripts',
'tcl',
'Tools']

>>> os.listdir('G:\\')
['$RECYCLE.BIN',
'Movies',
'Music',
'Photos',
'Series',
'System Volume Information']
```

## Making a New Directory

We can make a new directory using the `mkdir()` method.

This method takes in the path of the new directory. If the full path is not specified, the new directory is created in the current working directory.

```python
>>> os.mkdir('test')

>>> os.listdir()
['test']
```

## Renaming a Directory or a File

The `rename()` method can rename a directory or a file.

The first argument is the old name and the new name must be supplies as the second argument.

```python
>>> os.listdir()
['test']

>>> os.rename('test','new_one')

>>> os.listdir()
['new_one']
```

## Removing Directory or File

A file can be removed (deleted) using the `remove()` method.

Similarly, the `rmdir()` method removes an empty directory.

```python
>>> os.listdir()
['new_one', 'old.txt']

>>> os.remove('old.txt')
>>> os.listdir()
['new_one']

>>> os.rmdir('new_one')
>>> os.listdir()
[]
```

However, note that `rmdir()` method can only remove empty directories.

**In order to remove a non-empty directory we can use the `rmtree()` method inside the `shutil` module.**

```python
>>> os.listdir()
['test']

>>> os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'

>>> import shutil

>>> shutil.rmtree('test')
>>> os.listdir()
[]
```

