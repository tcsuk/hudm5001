### Programming Assignment: SQLite Interaction
Last updated: Oct 8, 2024  

**Instructions**  
Follow the instructions below. Copy all questions, code, and output into a document and submit through Canvas.  
A document in Word format is suggested, as you will include screenshots of your results.  

**TOTAL POINTS: 10**

1) (1 PT) In SQLite, create a database called *mydata.db*    
List the databases available in SQLite. Take a screenshot to show the database was created, and include it in your results document.

---  

**Questions 2-8 are to be executed in Python.**  

2) (1 PT) Create a dataset with five rows and three columns. One of the columns must include categorical data (e.g., industry, city).
The format needs to be a list of tuples.

3) (1 PT) Create a table in mydata.db called *mytable* and pass a schema.  End the transaction with a commit.

4) (1 PT) Insert your dataset into *mytable*. End the transaction with a commit.

5) (1 PT) Write and execute a query that returns all of the inserted records. Print the result.

6) (1 PT) Write and execute a query that filters out some of the inserted records based on a condition. Print the result.

7) (1 PT) Write and execute a query that uses a GROUP BY clause to aggregate on the categorical field. For example, you might compute the number of records
          for each level of industry (e.g., TECH  2, CONSUMER GOODS 3). Print the result. (Hint: [SQLite GROUP BY](https://www.sqlitetutorial.net/sqlite-group-by/))

9) (1 PT) Based on the results from one of the queries, load the results into a pandas dataframe. Print the dataframe.

---  

9) (1 PT) From SQLite, list the tables. You should see *mytable* listed. Take a screenshot to show the table was created, and include it in your results document.

10) (1 PT) From SQLite, write and execute a query on *mytable*. Take a screenshot to include the query and results in your results document.

---  
