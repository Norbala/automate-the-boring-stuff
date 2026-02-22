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

Instead of print(), use logging.debug - more controllable and easily deactivated (at TOP tho)

Enumerate - cool function to use in for loops on lists when you need both index and item
- for index, item in list("a","b","c"): print (index, item)

Both variables as well as lists can be augmentally assigned (+=) 