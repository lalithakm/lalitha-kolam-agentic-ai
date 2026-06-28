# Class 2 Feed – June 27, 2026

## Environment Setup
Windows refresher for Python setup

## Python Refresher
**Video Playlist**:
https://youtube.com/watch?v=zFtseTB05AM&list=PLI2v4rh7YVhdzMPIrK0az-tfd0wSDbjhp&themeRefresh=1
**Class Repository**:
https://github.com/mayank953/Live-Class-2026/tree/main/class2v2
**Running Python Files**
uv run <filename.py>


## Topics Covered
**Python Fundamentals**
Variables
Data Types
f-Strings
Control Flow (if, elif, else)
Loops

**Python Collections**
Lists
Dictionaries
- JSON examples
Tuples

**JSON Practice**
API:
https://catfact.ninja/fact
Notebook:
https://colab.research.google.com/drive/10u_Rae677OnKyOkgAS72gr2gyMNKcqSm?usp=sharing


**Classes & Objects**

Visualizing Classes
Used PythonTutor to understand:
Classes
Objects
Memory visualization
https://pythontutor.com/



**Boilerplate Code**

Traditional Python classes require writing:
__init__()
property assignments
We learned how @dataclass simplifies this.
With @dataclass, Python automatically generates:
__init__()
__repr__()
__eq__()
__hash__() (when applicable)
and other useful methods
This significantly reduces boilerplate code.

**Error Handling**
Covered:
try
except
finally
Used to gracefully handle runtime errors and prevent program crashes.

**Decorators & Wrappers**
Learned how decorators wrap existing functions to add extra behavior.
Examples:
@announce
@timed (measure execution time)
This demonstrated how decorators can extend functionality without modifying the original function.

**API Calls**
Compared:
Fake API calls
ChatGPT API calls
Introduced the concept of Chat Completions and how applications interact with language models programmatically.

## **Pydantic**
Python is dynamically typed, meaning values of different types can often be passed without immediate errors.
Example:


from pydantic import BaseModel
class User(BaseModel):
    name: str
    age: int

** Why Pydantic?**
Enforces type validation
Performs automatic type conversion when possible
Makes code safer and more reliable
Validates incoming data
Essential when building APIs (FastAPI and other backend frameworks)

## Key Takeaways
✅ Makes code more error-safe
✅ Enforces data validation
✅ Reduces bugs caused by invalid input
✅ Will be heavily used when creating API servers in future classes


## Summary
Today's session covered:
Windows environment setup
Python fundamentals
Lists, dictionaries, tuples
JSON APIs
Classes & Objects
@dataclass
Exception handling
Decorators
API calls & Chat Completions
Introduction to Pydantic
