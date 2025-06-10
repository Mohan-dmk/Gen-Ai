1)
WHAT IS A IDENTIFIER?
An identifier is the name you use to identify variables, functions, classes, modules, or objects in your code.
It’s basically what you name things.
🚫 Rules for Writing Identifiers:
1.	Must start with a letter (A–Z or a–z) or an underscore (_)
2.	Can contain letters, digits (0–9), and underscores
3.	Cannot start with a digit (e.g., 2name is invalid ❌)
4.	Cannot be a Python keyword (like if, class, for, while, etc.)

2) What is a induction?
In Python, indentation means adding spaces at the beginning of a line to show that some lines belong together. Indentation tells Python which lines of code are inside a function, loop, or condition.
Summary:
•	Indentation = spaces at the beginning of lines
•	Python needs it to group related code
•	Usually use 4 spaces for indentation
•	It shows what code is inside a function, loop, or if-statement

3) What is a Doc string?
A docstring (short for documentation string) is a special string written inside triple quotes “""" """ to describe what your function, class, or module does.
It's like a built-in note or explanation for someone reading your code — or even for your future self!

4) What is a string?
A string is a sequence of characters — like letters, numbers, spaces, and symbols — surrounded by quotes.
name = "Mohan"
greeting = 'Hello'
sentence = """This is a multi-line string."""
You can use:
•	Double quotes "Hello"
•	Single quotes 'Hello'
•	Triple quotes """Hello""" or '''Hello''' for multi-line strings

String Index:
A string index is the position number of each character in a string.
It tells you where each character is located.
Let’s say we have a string:
word = "Python"
Each character in "Python" has an index like this:
Character	P	Y	t	h	o	n
Index	0	1	2	3	4	5
So:
•	word[0] → 'P'
•	word[2] → 't'
•	word[5] → 'n'						
Python also lets you count from the end using negative indexes:
Character	P	y	t	h	O	n
Index	-6	-5	-4	-3	-2	-1
So:
•	word[-1] → 'n' (last letter)
•	word[-3] → 'h'
String update:  You can’t change a character in-place, but you can build a new string using slicing or other operations.
Example: Update a Character
python
CopyEdit
text = "Python"
# Change 'P' to 'J' → make it "Jython"

new_text = "J" + text[1:]
print(new_text)  # Output: Jython
You're not changing text, you're creating a new one.

String Delete : You can't delete a part of a string directly.
But you can: A) Delete the whole string:
python
CopyEdit
text = "Hello"
del text
# Now `text` is gone
B) Create a new string without certain characters
python
CopyEdit
text = "Hello"
# Remove 'H'
new_text = text[1:]
print(new_text)  # Output: ello


5) What is a Log System?
A log system is a part of a program or software that:
Automatically records events, messages, or errors into a file (or console, or server) — so that developers, engineers, or admins can monitor, debug, or audit what happened and when.
What Does It Log?
A log system can record:
•	🕒 When something happened (timestamp)
•	⚙️ What happened (event/message)
•	👤 Who did it (user, process)
•	🧨 How severe it is (error or just info)
What is Appending Logs?
•	Appending logs means adding new log messages to the end of the existing log file without deleting what’s already there
Why It's Useful:
•	Keeps full history in one file
•	Helpful for small apps or short-term scripts
.
What is Cycling Logs (Log Rotation)?
Cycling logs means:
When the log file becomes too big, the system automatically creates a backup (e.g., app.log.1) and starts a fresh new log file.
Why Cycling Is Important:
•	Prevents giant log files from crashing your system
•	Useful for long-running applications
•	Helps you keep logs clean and only save recent logs.

What is a list?

A list is a collection of items stored in a single variable.
It can hold:
•	Numbers: [1, 2, 3]
•	Words (strings): ["apple", "banana"]
•	Mixed data: [1, "yes", True]
•	Even other lists: [1, [2, 3], 4]
✅ Lists are:
•	Ordered: Items have positions (indexes)
•	Changeable: You can add/remove/update items
•	Indexed: You access items by position
   What is a List Index?
•	A list index is the position number of an item inside a list.
•	It tells Python where each item is located, so you can access, change, or remove it.
•	Example List:
fruits = ["apple", "banana", "cherry", "orange"]
Item	apple	banana	cherry	orange
Index	0	1	2	3
Negative	-4	-3	-2	-1
