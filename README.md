# Notes from learning Python via Automate the Boring Stuff

Print returns None (Python adds it)
Every function should have a return value

Function call stack, frame objects

Local and global Scopes - watch out! Variables living only locally in function
- multiple local scopes can run at once and have same-name variables, BUT which cannot be utilized from one local scope to another
- thus, give all variables DIFFERENT names
    - good practice
- write global variableName in first row of function to set the value of that variable globally

try and except go good with "raise Exception("exception message")"

"assert" test should crash the program if it fails 