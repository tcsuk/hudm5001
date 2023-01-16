### GitHub Assignment

Follow the instructions to accomplish the tasks below.  
Complete the action items in **bold**, entering solutions into a file that you'll submit on Collab.  
A Word doc or equivalent will be suitable as you'll need to include images. Make sure your solutions are numbered and easy to read.

#### TOTAL POINTS: 4

NOTE: All students are expected to complete this assignment and earn full credit. If an extension is needed, please discuss with the instructor.  

1) You are going to fork the PyTorch repo to your GitHub account (this creates your forked copy that you can modify).  
Aside: PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing.  
Visit this website:  

https://github.com/pytorch/pytorch  

After the fork, you should see the PyTorch repo in your account.

In the GUI, click Add file > Create new file  
Call the file "myfile" and write "Hello World" in the file  
Congrats, you just used the GUI to create and modify a file in your copy of the PyTorch repo!  

Browse to the bottom and click the Commit new file button.
Scroll down and you should see your file in the list.

**Action Item 1:** Take a screen shot which shows myfile and the PyTorch logo at the bottom.    
Paste the screen shot into your solution file. (1 PT)

2) Clone the forked copy to your local machine  
After cloning, open the file called version.

**Action Item 2:** Paste the contents of the version into your solution file. (1 PT)

3) Feel free to browse around in the directory to look at the files.  
In particular, open this file in an application that views python files (e.g., Spyder):  

/pytorch/torch/optim/sparse_adam.py

look at the components of the file, and we will also review in class.  

**Action Item 3:** Search for the word SparseAdam, and count how many times it appears in the file.  
Enter this value into your solution file. (1 PT)  

4) Next, you will create a new file in the forked copy on your local machine, and push it back to GitHub.  
This allows you to "socialize" your new file with other users who have access to the forked copy.

Create a text file in the forked copy, calling it hello_world.txt.  
Enter the line: [your_name] was here!  
where you'll substitute your first name for [your_name]  
Save the file.  

Next, you will commit the file so it will be version controlled.  
Open a terminal  
Navigate to the directory containing the repo.  
At the command line, where > means prompt, commit your file by issuing these lines:  

```
> git add hello_world.txt  
> git commit -m 'added file hello_world'
```

Lastly, you'll push your new file to the GitHub fork.  

`> git push`

Return to GitHub and you should see the new file.  

**Action Item 4:** Take a screen shot which shows the hello_world.txt file and the PyTorch logo at the bottom.  
Paste the screen shot into your solution file. (1 PT)  

Congratulations, these were big steps working with git and GitHub!
