# Notes from learning Python via Automate the Boring Stuff

### General
Print returns None (Python adds it)

### Git / GitHub
Do not create README.md and .gitignore up front - confuses the Git when you want to make the initial push.

- Use "pip freeze > requirements.txt" to copy all dependencies to a file that is easy for users to install.
- If you initiate Git in each directory and connect with respective GitHub repo, you first push for one project, and later want to push the files for another project, no problem! ALso no problem with environments. Each directory from CLI has its own associated repo hidden and Git handles everything.



### Functions
#### General
Every function should have a return value

Function call stack, frame objects

try and except go good with "raise Exception("exception message")"

"assert" test should crash the program if it fails

Instead of print(), use logging.debug - more controllable and easily deactivated (at TOP tho)

#### Scopes
Local and global Scopes - watch out! Variables living only locally in function
- multiple local scopes can run at once and have same-name variables, BUT which cannot be utilized from one local scope to another
- thus, give all variables DIFFERENT names
    - good practice
- write global variableName in first row of function to set the value of that variable globally

Enumerate - cool function to use in for loops on lists when you need both index and item
- for index, item in list("a","b","c"): print (index, item)

Both variables as well as lists can be augmentally assigned (+=)