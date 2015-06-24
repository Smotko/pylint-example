# Pylint example

`module_two` uses `TestSomething` defined in `module_one` and running
`pylint module_two` resulted in:

```
************* Module tests.module_two.test_something_else
W:  7, 0: Class has no __init__ method (no-init)
E: 11, 8: Instance of 'TestSomethingElse' has no 'assertEquals' member (no-member)
```

The issue was that `TestModule` imported something not in my pythonpath
`from flask.ext.testing import TestCase`. Of course, pylint picks this up
correctly:

```
************* Module tests.module_one.test_something
F:  3, 0: Unable to import 'flask.ext.testing' (import-error)
W:  7, 0: Class has no __init__ method (no-init)
E: 11, 8: Instance of 'TestSomething' has no 'assertEquals' member (no-member)
R:  7, 0: Too few public methods (1/2) (too-few-public-methods)
```

But I still missed it because the code I was was working on is huge
(even with the correctly set up PYTHONPATH the original module_one has
more than 500 lint warnings :/).
