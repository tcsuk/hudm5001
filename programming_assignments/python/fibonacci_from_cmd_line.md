# Running Fibonacci from the Command Line

**INSTRUCTIONS**  
In this exercise, you will practice running Python scripts from the command line (CL).  
After completing `recursion.ipynb` you will have written the function `fibonacci_robust`.

1) Place `fibonacci_robust` in a script called `fibonacci.py`, noting where you have saved it.  

Add some lines of code to:
- print a title
- call the function with `n=6` and print the result

2) Launch the Anaconda Prompt to run Python from the CL  
On a Windows machine, you would select Start and then begin typing Anaconda Prompt  

3) At the prompt, change directory to the script location (using the cd command)  
4) At the prompt, type:

`python fibonacci.py`

This should print the results

5) Make a new file called `fibonacci_arg.py` that takes *n* as an argument, computes the function with the passed *n*, and prints the result.  
Hint these things will be helpful:  
import sys  
sys.argv  

We will discuss more in class  

6) Run `fibonacci_arg.py` at the CL and verify the result.

For example, at the prompt type:

`python fibonacci_arg.py 6`

This likely breaks. Why?  
Hint: what is the data type of the argument? What does it need to be?  
Make sure you can get the correct result to print.
