# HW: Unit Testing a Book Lover Class
### TOTAL POINTS: 12

This activity involves:

Designing a complete class, given basic requirements  
Designing and creating a number of unit tests  
1. Here are some requirements for a “BookLover” class. Write the BookLover class, making sure to adhere to these requirements:

 

**a. FIELDS: (1 point for including all fields in class)**  

|attribute |description|
|--- |---|
|name|The name of the person (type:string)|
|email|The person’s email, serving as a unique identifier (type:string)|
|fav_genre|The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction).  (type:string)|
|num_books|Keeps track of the number of books the person has read (type:int)|
|book_list|a list of tuples, where each tuple consists of the title of the book the person has read, followed by the person’s rating of that book (scale of 0–5, where 0 means the person did not like the book at all, and 5 means the person loved the book.) Example: book_list = [(“Jane Eyre”, 4), (“The Odyssey”, 3), (“The Divine Comedy”, 5)]


**b. FUNCTIONS: (5 points; 1 point per correct function)**  

|fcn |description|
|--- |---|
|__init__ (Constructor)	|`name`, `email`, and `fav_genre` are mandatory fields that need to be passed into the constructor; however, `num_books` and `book_list` are optional fields. Use these default parameters: num_books=0, book_list=[] (As for the parameter order, use the order specified in the “Fields” section above. Do not add any additional fields of your own.)
|Method 1: addBook(bookName, rating)	|This function takes a book name (string) and rating (0–5) as input and tries to add it to `book_list`. Only add a book to the person’s `book_list` if that book doesn’t already exist. It is sufficient to match on book name.|
|Method 2: hasRead(bookName)	|This function takes a book name (string) as input and determines if the person has read the book (that is, if that book name is in `book_list`). The method should return True if the person has read the book, False otherwise.
|Method 3: numBooksRead()	|This function takes no parameters and returns the total number of books the person has read (make use of the num_books field).
|Method 4: favBooks()	|This function takes no parameters and returns a list of the person’s most favorite books (list of book titles). Books displayed in this list should have a rating greater than (but not including) 3.


2. To test out your BookLover class, you will write a test suite of unit tests.  
Write the unit tests below, starting all your function names with “test_”.  
Run your test cases, and ensure all your unit tests pass.  

**Unit Tests (Total 6 points; one point per passing test)**  
Test 1 addBook(): add a book and test it's in `book_list`  
Test 2 addBook(): add the same book twice. test it's in `book_list` only once  
Test 3 hasRead(): pass a book in the list and test the answer is True  
Test 4 hasRead(): pass a book NOT in the list and use assertFalse to test the answer is True  
Test 5 numBooksRead(): add some books to the list, and test `num_books` matches expected.  
Test 6 favBooks(): add some books with ratings to the list, making sure some of them have rating > 3. Your test should check that the returned books have rating > 3.  

**Hint for writing unit tests:**  
1) The code snippet below shows the start of a class for the Test Suite.
A book lover called `reader` is created.
In test_add_book(), notice how the reader is referenced with self.  

```
class BookLoverTestSuite(unittest.TestCase): 
    
    # create a book lover
    reader = BookLover('Steven','smt@gmail.com','drama')
    
    def test_add_book(self):        
        self.reader.addBook('Great Gatsby',5)
```

2) The `unittests` package will run the tests in alphabetical order, which might come as a surprise, and it can foul up your test results.
If you insert numbers in your function names, you can get them to run in the order you want (top down):

test_1_rest_of_name  
test_2_rest_of_name  
...  

3) Note the data accumulates in the object as you run additional tests

4) To run the tests, put this code at the bottom of your script:

```
if __name__ == '__main__':
    unittest.main() 
```

**FILE SUBMISSION**  
Your submitted file should include all code, and output showing that all tests ran with OK message.
