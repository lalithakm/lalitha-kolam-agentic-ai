from typing import Callable

# Define a simple function that prints a greeting message
def greet():
    print("Hello! Welcome to the Python AI demonstration.")


# Create a dictionary that maps tool names (strings) to their corresponding functions
# This acts as a registry where "greet" key points to the greet function object
TOOL_REGISTRY1 = {
    "greet": greet
}

# Retrieve the greet function from the registry using the "greet" key
# The trailing () immediately calls/executes the retrieved function
TOOL_REGISTRY1["greet"]()


# Prints the name of the function object stored in the registry. 
# You can automatically get the function's name instead of typing it yourself
print(greet.__name__)

print("----------------------------------------------------------------------")

# Using Decorators to register the Tools
# Empty dictionary to store functions
TOOL_REGISTRY2: dict[str, callable] = {}

def register_tool(func: Callable) -> Callable: 
    TOOL_REGISTRY2[func.__name__] = func # Register the function in the dictionary
    return func  # Return the original function so it can still be called normally

@register_tool
def greet_decorated():
    print("Hello! Welcome to the Python AI demonstration (decorated).")


@register_tool
def add():
     print(1 + 2)

print(TOOL_REGISTRY2)  # Print the dictionary to show registered functions


TOOL_REGISTRY: dict[str, Callable] = {}

def tool(func: Callable) -> Callable:
    TOOL_REGISTRY[func.__name__] = func
    print("What gets printed?")
    print(TOOL_REGISTRY[func.__name__])
    return func

@tool
def add_decorated(a: int, b: int) -> int:
    return a + b

print("Prints: ", TOOL_REGISTRY)  # Print the dictionary to show registered functions

result = TOOL_REGISTRY["add_decorated"](2, 3)
print(result)
