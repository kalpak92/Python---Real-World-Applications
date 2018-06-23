# Python - Environment Setup

## Python Environment Variables

Here are important environment variables, which can be recognized by Python −

| Sr.No. | Variable & Description                                       |
| :----: | ------------------------------------------------------------ |
|   1    | **PYTHONPATH**<br />It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer. |
|   2    | **PYTHONSTARTUP**<br />It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH. |
|   3    | **PYTHONCASEOK**<br />It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable to any value to activate it. |
|   4    | **PYTHONHOME**<br />It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy. |

## Running Python

There are three different ways to start Python −

### Interactive Interpreter

You can start Python from Unix, DOS, or any other system that provides you a command-line interpreter or shell window.

Enter **python** the command line.

Start coding right away in the interactive interpreter.

```shell
$python # Unix/Linux
or
python% # Unix/Linux
or
C:> python # Windows/DOS
```

Here is the list of all the available command line options −

| Sr.No. | Option & Description                                         |
| :----: | ------------------------------------------------------------ |
|   1    | **-d**<br />It provides debug output.                        |
|   2    | **-O**<br />It generates optimized bytecode (resulting in .pyo files). |
|   3    | **-S**<br />Do not run import site to look for Python paths on startup. |
|   4    | **-v**<br />verbose output (detailed trace on import statements). |
|   5    | **-X**<br />disable class-based built-in exceptions (just use strings); obsolete starting with version 1.6. |
|   6    | **-c cmd**<br />run Python script sent in as cmd string      |
|   7    | **file**<br />run Python script from given file              |