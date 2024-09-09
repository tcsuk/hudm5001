### Instructions for Forking and Cloning HUDM5001 Course Repo     

You will do these things:
1) Check if you have *git* on your machine by opening a terminal and typing `git`.    
If your screen doesn't fill with *git* commands, you don't have *git*.  

You can download it [here](https://git-scm.com/downloads)  
NOTE: *git* is a tool for version controlling software on a machine, while *GitHub* allows users to share software online.

2) Create a GitHub account [here](https://github.com/)
3) Create your GitHub personal access token. This will allow you to authenticate your machine and push updates to a repo.  
   
   Steps:  
   Settings (top right) -> Developer Settings -> Personal access tokens ->  Tokens (classic) ->
   Generate New Token -> save this token somewhere secure

4) Fork the course repo (click **fork** button at top right of repo page). This will create a separate copy of the repo in your account.
5) Visit your account and find the copied course repo. Clone the repo to your personal machine.  
Steps for cloning:  
i. open a terminal (on Windows, Powershell is a fairly good terminal)  
ii. change directory to a path for your repo, using **cd** command.  
iii. from the forked repo in your GitHub account, click the green Code button and click the clipboard.  
iv. return to the terminal and type:  

`git clone [url]`  

where [url] is where you paste the url from the clipboard.  
this will clone the repo to your machine.  
if things worked correctly, you will find the directory structure at that path on your machine.  
