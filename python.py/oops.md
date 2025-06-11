File handling:
File handling allows a program to read, write, append, or create files. It helps store and access data permanently, unlike variables (which are temporary).
Common File Modes:
Mode	Purpose
'r'	Read (file must exist)
'w'	Write (creates or overwrites file)
'a'	Append (adds to end of file)
'x'	Create new file (error if exists)
'b'	Binary mode (e.g. images)
't'	Text mode (default)
Basic Syntax:
Python:  file = open("filename.txt", "mode")
file.write("Hello!")
file.close()
Why Use File Handling:
•	Store user input
•	Write logs and reports
•	Load data (e.g., from .txt, .csv, .json)
•	Save AI model outputs or chatbot logs
Exception Handling in Python:
exception handling is used to catch errors that happen during program execution and prevent the program from crashing.
Common Keywords:
Keyword	Purpose
Try - 	Code that may throw an error
Except -	Handle the error
Else -	Run if no error occurs
Finally -	Always runs (clean-up code)
Raise -	Manually throw an error
Basic Syntax:
python
CopyEdit
try:
    # risky code
    x = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero.")
finally:
    print("Done.")
Why Use Exception Handling:
•	Avoid crashes when errors occur
•	Handle user input mistakes
•	Detect missing files or invalid data
•	Improve user experience (friendly error messages)




