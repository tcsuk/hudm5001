# Test-Driven Development (TDD) and Unit Testing

Unit testing gives you the confidence that your code does what you think it does. 

Here are some benefits that come with test-driven development (TDD) and performing unit tests:

- Developers can work in a predictable way on developing code
- Programmers write their own unit tests
- You can get a rapid response for testing small changes
- It encourages programmers to build many highly-cohesive, loosely-coupled modules to make unit testing easier
 
Other benefits include:

- Allows you to do what’s next knowing what you’ve done is okay
- Allows you to make changes
- Avoids a growing “house of cards”
- Documents your intentions to others
- Gives you a more satisfying experience
 

**Unit Testing Steps**  
Step 1	
Decide how to test a method and write the test.
Write the test before (maybe while) writing code itself.
It forces you to understand what you’re building.

Step 2	 
Run the test yourself together with all other tests.
You run them, not someone else.

Step 3	 
This test and all others must pass together.
Do not add features until all tests pass.
 

**Unit Testing**  
Usually you’ll write a number of unit tests per method to be able to fully test out each of the methods.  
The main portion of the unit test is the “assert” statements within the unit test. These assert statements check if the code you’re trying to test has passed or failed the test.


**Python Assert Methods**  
The module unittest provides a family of assert methods to help check for failures.

**NOTE: Ultimately, you want to write your tests so that when the output matches the expected value, it passes the test.**   

The *TestCase* class provides a number of methods to check for and report failures, such as:

Method	Checks that...
|method |condition|
--- |---|
|assertEqual(a, b)|a==b|
|assertNotEqual(a, b)|a!=b|
|assertTrue(x)|bool(x) is True|
|assertFalse(x)|bool(x) is False|
|assertIs(a, b)|a is b|
|assertIsNot(a, b)|a is not b|
|assertIsNone(x)|x is None|
|assertIsNotNone(x)|x is not None|
|assertIn(a, b)|a in b|
|assertNotIn(a, b)|a not in b|
|assertIsInstance(a, b)|isinstance(a, b)|
|assertNotIsInstance(a, b)|not isinstance(a, b)|


**Note:**

All of the assert methods (except assertRaises(), assertRaisesRegexp()) accept a msg argument that, if specified, is used as the error message on failure.

Remember, in order to test your code, you must do the following:

- Set up what’s needed for testing. Create objects, allocate resources, create relationships, etc.
- Call the method to be tested.
- Verify that the method did what you expected.
- The above two are achieved by using an assert statement.
- Clean up (optional).

**Naming Conventions**  
Test files should include the name of the class you are testing. Each unit test method should be appropriately named, describing the kind of test being performed as closely as possible.


**Test Coverage**  
How do you know that your set of tests really exercises all of your code? There are tools for code coverage, which is the percentage of code that automated tests cover. It's not sufficient to create one unit test for each method. Typically, a method may have a number of test cases associated with it.

A coverage tool runs your code and gives a report of what is covered. Examples include:

- Clover (used by Web-CAT)
- Cobertura (Eclipse plug-in)

Coverage: [based on the amount of unit tests we can write]  

- % of lines covered (we could get pretty close with the number of unit tests we write)
- % of flows covered (often 0%: due to infinite options – no matter how many unit test we write)
- % of input sequences covered (often 0%: input sequences can be infinite, so coverage is essentially 0% no matter how many unit tests we write)

**Important Notes Regarding Unit Testing**  
- If your test can fail in more than one way, make a separate test for each of those ways.
- Do not mix many tests in one unit test. It’s better to separate them.
- Use the optional “msg” (message) parameter to clearly describe what went wrong when running tests that failed.
 
**Exhaustive Testing and Equivalence Classes**  
Let’s assume we have an infinite number of options as input to a method. For discussion, let’s consider numbers.  
There are infinite numbers in the negative direction and in the positive direction.  
For exhaustive testing, by implication, we have to test each input one-by-one, which is impossible.
 
To overcome that challenge, you can employ equivalence classes when you test methods.  
For each input space, identify an *equivalence class*: a set of inputs that should behave in the same way as they go through your program.  
Maybe the even numbers behave one way but odd numbers behave another.  
Maybe the numbers 1 through 20 behave one way, but numbers outside this range (21+, and 0 and below) behave another way.  
Once you’ve identified equivalence classes (there WILL be a finite and usually manageable number of them) then you need to pick a few representative samples from the equivalence class to test as inputs.  
So instead of testing all the negative numbers, pick 5 to 10 negative numbers.  
Don’t forget to test the boundaries, the middle of the class, and unique (and strange!) corner cases.
