# Pytest

## Create your first test

Create a simple test function with just four lines of code:

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

That’s it. You can now execute the test function:

```python
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:5: AssertionError
========================= 1 failed in 0.12 seconds =========================
```

This test returns a failure report because `func(3)` does not return `5`.

## Run multiple tests

`pytest` will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

## Assert that a certain exception is raised

Use the `raises` helper to assert that some code raises an exception:

```python
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

Execute the test function with “quiet” reporting mode:

```python
$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12 seconds
```

## Group multiple tests in a class

Once you develop multiple tests, you may want to group them into a class. pytest makes it easy to create a class containing more than one test:

```python
# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```

`pytest` discovers all tests following its [Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery), so it finds both `test_`prefixed functions. There is no need to subclass anything. We can simply run the module by passing its filename:

```python
$ pytest -q test_class.py
.F                                                                   [100%]
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________

self = <test_class.TestClass object at 0xdeadbeef>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, 'check')
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
1 failed, 1 passed in 0.12 seconds
```

The first test passed and the second failed. You can easily see the intermediate values in the assertion to help you understand the reason for the failure.

# Usage and Invocations

## Calling pytest through `python -m pytest`

New in version 2.0.

You can invoke testing through the Python interpreter from the command line:

```python
python -m pytest [...]
```

This is almost equivalent to invoking the command line script `pytest [...]` directly, except that calling via `python` will also add the current directory to `sys.path`.

## Possible exit codes

Running `pytest` can result in six different exit codes:

| Exit code 0: | All tests were collected and passed successfully          |
| ------------ | --------------------------------------------------------- |
| Exit code 1: | Tests were collected and run but some of the tests failed |
| Exit code 2: | Test execution was interrupted by the user                |
| Exit code 3: | Internal error happened while executing tests             |
| Exit code 4: | pytest command line usage error                           |
| Exit code 5: | No tests were collected                                   |

## Getting help on version, option names, environment variables

```python
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
```

## Stopping after the first (or N) failures

To stop the testing process after the first (N) failures:

```python
pytest -x            # stop after first failure
pytest --maxfail=2    # stop after two failures
```

## Specifying tests / selecting tests

Pytest supports several ways to run and select tests from the command-line.

#### **Run tests in a module**

```python
pytest test_mod.py
```

#### **Run tests in a directory**

```python
pytest testing/
```

#### **Run tests by keyword expressions**

```python
pytest -k "MyClass and not method"
```

This will run tests which contain names that match the given *string expression*, which can include Python operators that use filenames, class names and function names as variables. The example above will run `TestMyClass.test_something` but not `TestMyClass.test_method_simple`..

#### **Run tests by node ids**

Each collected test is assigned a unique `nodeid` which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by `::`characters.

##### To run a specific test within a module:

```
pytest test_mod.py::test_func
```

##### Another example specifying a test method in the command line:

```
pytest test_mod.py::TestClass::test_method
```

##### **Run tests by marker expressions**

```
pytest -m slow
```

Will run all tests which are decorated with the `@pytest.mark.slow` decorator.

##### **Run tests from packages**

```
pytest --pyargs pkg.testing
```

This will import `pkg.testing` and use its filesystem location to find and run tests from.

## Modifying Python traceback printing

Examples for modifying traceback printing:

```python
pytest --showlocals # show local variables in tracebacks
pytest -l           # show local variables (shortcut)

pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
pytest --tb=long    # exhaustive, informative traceback formatting
pytest --tb=short   # shorter traceback format
pytest --tb=line    # only one line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no      # no traceback at all
```

The `--full-trace` causes very long traces to be printed on error (longer than `--tb=long`). It also ensures that a stack trace is printed on **KeyboardInterrupt** (Ctrl+C). This is very useful if the tests are taking too long and you interrupt them with Ctrl+C to find out where the tests are *hanging*. By default no output will be shown (because KeyboardInterrupt is caught by pytest). By using this option you make sure a trace is shown.

## Dropping to [PDB](http://docs.python.org/library/pdb.html) (Python Debugger) on failures

Python comes with a builtin Python debugger called [PDB](http://docs.python.org/library/pdb.html). `pytest` allows one to drop into the [PDB](http://docs.python.org/library/pdb.html) prompt via a command line option:

```python
pytest --pdb
```

This will invoke the Python debugger on every failure. Often you might only want to do this for the first failing test to understand a certain failure situation:

```python
pytest -x --pdb   # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures
```

Note that on any failure the exception information is stored on `sys.last_value`, `sys.last_type` and `sys.last_traceback`. In interactive use, this allows one to drop into postmortem debugging with any debug tool. One can also manually access the exception information, for example:

```python
>>> import sys
>>> sys.last_traceback.tb_lineno
42
>>> sys.last_value
AssertionError('assert result == "ok"',)
```

## Setting breakpoints

To set a breakpoint in your code use the native Python `import pdb;pdb.set_trace()` call in your code and pytest automatically disables its output capture for that test:

- Output capture in other tests is not affected.
- Any prior test output that has already been captured and will be processed as such.
- Any later output produced within the same test will not be captured and will instead get sent directly to `sys.stdout`. Note that this holds true even for test output occurring after you exit the interactive [PDB](http://docs.python.org/library/pdb.html) tracing session and continue with the regular test run.

# Writing and reporting of assertions in tests

## Asserting with the `assert` statement

`pytest` allows you to use the standard python `assert` for verifying expectations and values in Python tests. For example, you can write the following:

```python
# content of test_assert1.py
def f():
    return 3

def test_function():
    assert f() == 4
```

to assert that your function returns a certain value. If this assertion fails you will see the return value of the function call:

```python
$ pytest test_assert1.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_assert1.py F                                                    [100%]

================================= FAILURES =================================
______________________________ test_function _______________________________

    def test_function():
>       assert f() == 4
E       assert 3 == 4
E        +  where 3 = f()

test_assert1.py:5: AssertionError
========================= 1 failed in 0.12 seconds =========================
```

`pytest` has support for showing the values of the most common subexpressions including calls, attributes, comparisons, and binary and unary operators. (See [Demo of Python failure reports with pytest](https://docs.pytest.org/en/latest/example/reportingdemo.html#tbreportdemo)). This allows you to use the idiomatic python constructs without boilerplate code while not losing introspection information.

However, if you specify a message with the assertion like this:

```python
assert a % 2 == 0, "value was odd, should be even"
```

then no assertion introspection takes places at all and the message will be simply shown in the traceback.

See [Advanced assertion introspection](https://docs.pytest.org/en/latest/assert.html#assert-details) for more information on assertion introspection.

## Assertions about expected exceptions

In order to write assertions about raised exceptions, you can use `pytest.raises` as a context manager like this:

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

and if you need to have access to the actual exception info you may use:

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)
```

`excinfo` is a `ExceptionInfo` instance, which is a wrapper around the actual exception raised. The main attributes of interest are `.type`, `.value` and `.traceback`.

Changed in version 3.0.

In the context manager form you may use the keyword argument `message` to specify a custom failure message:

```python
>>> with raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
...    pass
... Failed: Expecting ZeroDivisionError
```

If you want to write test code that works on Python 2.4 as well, you may also use two other ways to test for an expected exception:

```python
pytest.raises(ExpectedException, func, *args, **kwargs)
pytest.raises(ExpectedException, "func(*args, **kwargs)")
```

both of which execute the specified function with args and kwargs and asserts that the given `ExpectedException` is raised. The reporter will provide you with helpful output in case of failures such as *no exception* or *wrong exception*.

Note that it is also possible to specify a “raises” argument to `pytest.mark.xfail`, which checks that the test is failing in a more specific way than just having any exception raised:

```python
@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
```

Using `pytest.raises` is likely to be better for cases where you are testing exceptions your own code is deliberately raising, whereas using `@pytest.mark.xfail` with a check function is probably better for something like documenting unfixed bugs (where the test describes what “should” happen) or bugs in dependencies.

Also, the context manager form accepts a `match` keyword parameter to test that a regular expression matches on the string representation of an exception (like the `TestCase.assertRaisesRegexp` method from `unittest`):

```python
import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()
```

The regexp parameter of the `match` method is matched with the `re.search` function. So in the above example `match='123'` would have worked as well.

## Making use of context-sensitive comparisons

New in version 2.0.

`pytest` has rich support for providing context-sensitive information when it encounters comparisons. For example:

```
# content of test_assert2.py

def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
```

if you run this module:

```
$ pytest test_assert2.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_assert2.py F                                                    [100%]

================================= FAILURES =================================
___________________________ test_set_comparison ____________________________

    def test_set_comparison():
        set1 = set("1308")
        set2 = set("8035")
>       assert set1 == set2
E       AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
E         Extra items in the left set:
E         '1'
E         Extra items in the right set:
E         '5'
E         Use -v to get the full diff

test_assert2.py:5: AssertionError
========================= 1 failed in 0.12 seconds =========================
```

Special comparisons are done for a number of cases:

- comparing long strings: a context diff is shown
- comparing long sequences: first failing indices
- comparing dicts: different entries

See the [reporting demo](https://docs.pytest.org/en/latest/example/reportingdemo.html#tbreportdemo) for many more examples.

## Defining your own assertion comparison

It is possible to add your own detailed explanations by implementing the `pytest_assertrepr_compare` hook.

- `pytest_assertrepr_compare`(*config*, *op*, *left*, *right*)[[source\]](https://docs.pytest.org/en/latest/_modules/_pytest/hookspec.html#pytest_assertrepr_compare)

  return explanation for comparisons in failing assert expressions.Return None for no custom explanation, otherwise return a list of strings. The strings will be joined by newlines but any newlines *in* a string will be escaped. Note that all but the first line will be indented slightly, the intention is for the first line to be a summary.Parameters:**config** ([*_pytest.config.Config*](https://docs.pytest.org/en/latest/reference.html#_pytest.config.Config)) – pytest config object

As an example consider adding the following hook in a [conftest.py](https://docs.pytest.org/en/latest/fixture.html#conftest-py) file which provides an alternative explanation for `Foo` objects:

```python
# content of conftest.py
from test_foocompare import Foo
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ['Comparing Foo instances:',
                '   vals: %s != %s' % (left.val, right.val)]
```

now, given this test module:

```python
# content of test_foocompare.py
class Foo(object):
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
```

you can run the test module and get the custom output defined in the conftest file:

```python
$ pytest -q test_foocompare.py
F                                                                    [100%]
================================= FAILURES =================================
_______________________________ test_compare _______________________________

    def test_compare():
        f1 = Foo(1)
        f2 = Foo(2)
>       assert f1 == f2
E       assert Comparing Foo instances:
E            vals: 1 != 2

test_foocompare.py:11: AssertionError
1 failed in 0.12 seconds
```

