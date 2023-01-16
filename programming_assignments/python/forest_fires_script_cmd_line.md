# Forest Fires Script from CL

**INSTRUCTIONS**

In this assignment, you will:
- move code from a Jupyter notebook to a script
- make modifications to the script
- run it from the command line
- screen shot your solutions into a document and submit thru Collab

Here are the details:
1) Start with the solutions from the Forest Fires assignment, found in Resources > Solutions > forest_fires_function_assignments_solns.ipynb

2) Copy all code into a script

3) Modify the code to print these objects, which are all created when the code runs. Put a carriage return like this in your print statements, to get blank line separators:
print(some_object, '\n')

Each item is worth 1 PT, for **TOTAL 10 POINTS**:

- your name and short description of the script
- path_to_data
- fire.head(3)
- coord_builder(X, Y)[:5]
- (min(area), max(area))
- lx(area[-10:])
- np.unique(month)
- uniq_mos
- arr_filt
- sum_sq_err(FFMC)

4) Modify the script to take `path_to_data` as a command-line argument (recall this involves importing `sys` and using `sys.argv`)

5) Save the script and run from command line (e.g., using Anaconda Prompt)

6) Screen shot the results, paste into document, and submit through Collab

Be sure that all solutions are in the submitted document.
