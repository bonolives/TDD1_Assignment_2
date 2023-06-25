# TDD1_Assignment_2

The goal of this exercise is to demonstrate how to evolve the multiply example using a Test First approach, from the first test, through to the last test.

If you are good with Git, commit after each refactor to keep the history of the evolution of your solution. That way Git keeps your history for you. Otherwise, just comment out the old code as your solution evolves.

Don't forget, this new approach might feel a bit like wearing new shoes, but as you practice it, the technique will become more familiar and comfortable.

outline of the steps to take( this can apply to both Javascript and Python language)

Setup ( Javascript):

Create a new node.js project
Install and configure a local copy of eslint. Don't install it globally for reasons I mentioned before.
Install mocha as a dev dependency
Install chai as a dev dependency
Create a test directory
Create a test.js inside that test directory
Create a multiply.js
Update npm script to run tests using mocha
setup (Python): for python make sure to use, Pytest, Pylint and Black.

Test First TDD Cycle 1

Red: Write your first test: assertEqual(multiply(1, 1), 1); in ./test/test.js
Red: Run the test. Did it pass? No! Becasue you haven't written the multiply function yet!
Get the test to pass, by writing a multiply function, that is just enough code to pass the test, i.e. function multiply (a, b) { return 1; }
Run the test? Does it pass? Should do! Now we are green!
Refactor? Probably not necessary!
Test First TDD Cycle 2

Red. Write the next test. Run the tests: assertEqual(multiply(2, 2),4)
Green: Update multiply() to pass the second test. Make sure the first test still passes too!
Do I need to refactor? Nope, its pretty simple
Test First TDD Cycle 3

Red. Write the next test: assertEqual(3, 3), 9)
Red/Green: Does it pass, maybe, depends on your solution.
Green: Update multiply() to pass the third test, if you need to. Make sure you didnt break test 1 or test 2! If you did, fix them.
Do I need to refactor? Nope, its pretty simple
Fourth Test Cycle

Red. assertEqual(4, 4), 16)
Oh! Its green!
Fifth Test Cycle

Red: assertEqual(23, 45), 23 * 45)
Oh! Its till green!
