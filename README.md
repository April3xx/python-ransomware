# python-ransomware
Basic ransomware proof of concept with Python 3.7.
## task 
 - [ ] rename file extensions to any file extensions
    - ~[X] make args pass to be more flexible eg. don't need to type --action --key just assert it for more robust~
    - [ ] add file extension parameter to the program
    - [ ] seperate decrypt/encrypt if needed
 - [X] f.truncate() to fix random strings being append after decrypt
 ## design
   1. self-destroy
   2. send key to remote server
   3. encrypt all filetype but not system file
   4. propagate through network
      
## special features
   1. try to destroy as many backup as possible
      eg. encrypt and push encrypted code to github
   
