

06/26/2026

https://bugs-sleep-6uj.craft.me/agentic3 

https://docs.astral.sh/uv/getting-started/installation/#standalone-installer 

https://bugs-sleep-6uj.craft.me/agentic3/b/95865277-617B-43F0-9571-CA736E4CEF7E/Class-1---Python 


https://github.com/mayank953/Live-Class-2026/tree/main 

UV Package Manager

Create venv
uv venv --python 3.12

https://chatgpt.com/c/6a3f4615-8530-83ee-9b1e-fc5a69d2b29c

https://chatgpt.com/share/6a3f49e2-2130-83ee-81f2-d43b6a8a5cf0 

Activate venv on Windows ( best to use git bash INSTEAD OF powershell, can use vscode terminal which uses powershell as well on WINDOWS)

.venv\Scripts\Activate.ps1 


uv init my-first-project
cd my-first-project
Add packages to be installed in pyproject.toml (Ex: numpy)
Run “uv add numpy” to install the package
We could also use requirements.txt as well to list all the packages required
We can then run “uv add requirements.txt”
All packages listed in requirements.txt are installed. (also add the installed packages in pyproject.toml)
Uv.lock -> created using “uv sync” or “uv lock”


UV Video:
youtube.com/watch?v=FL10d0k3GAo&themeRefresh=1 

Python Fundamentals


APIs: 
https://frankfurter.dev/ 
https://api.frankfurter.dev/v2/rates 



For the FEED
Learning Summary – 06/26/2026 (7:30pm to 10:30pm PST)
1. UV Package Manager
Today's focus was on learning UV, a fast Python package and environment manager that can replace pip + venv for most workflows.
Installation
Install UV using the standalone installer.
UV provides a much faster dependency installation experience compared to pip.
Creating a Virtual Environment
uv venv --python 3.12

Activating the Environment (Windows)
Using Git Bash is recommended over PowerShell.
PowerShell:
.venv\Scripts\Activate.ps1

Git Bash Windows OR macOS
source .venv/bin/activate

2. Creating a New Python Project
Initialize a project:
uv init my-first-project

Navigate into it:
cd my-first-project

A pyproject.toml file is created, which serves as the project's configuration and dependency file.

3. Installing Packages
Install packages directly:
uv add numpy

This automatically:
Installs the package
Updates pyproject.toml
Updates the lock file
Using requirements.txt
If a project already has a requirements.txt:
uv add -r requirements.txt

This installs all listed packages while also recording them in pyproject.toml.

4. Dependency Locking
UV maintains reproducible environments using a lock file.
Useful commands:
uv sync

or
uv lock

This generates/updates:
uv.lock

The lock file ensures everyone installs the exact same package versions.

Python Fundamentals
Began reviewing Python basics, including:
Variables
Data types
Basic syntax
Project structure
Function
OOPS concept
APIs
These fundamentals will be built upon in future classes.

APIs
Introduced the concept of APIs (Application Programming Interfaces).
Example API:
Frankfurter Currency API
Endpoints:
https://frankfurter.dev/
https://api.frankfurter.dev/v2/rates
This API can be used to retrieve real-time currency exchange rates and serves as a simple example for learning how Python interacts with web services.

Resources Covered
Course Notes
Agentic AI notes
Python Class 1 notes
Repository
Live Class 2026 GitHub repository
Additional Learning
UV Package Manager documentation
UV YouTube tutorial
ChatGPT discussions on UV setup and usage

Key Takeaways
Learned how to use UV as a modern replacement for traditional Python environment management.
Created isolated Python virtual environments.
Initialized Python projects using uv init.
Managed dependencies using uv add.
Understood the purpose of pyproject.toml and uv.lock.
Started revisiting Python fundamentals.
Got introduced to REST APIs using the Frankfurter Currency API.

Commands Learned
# Create virtual environment
uv venv --python 3.12

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Create project
uv init my-first-project

# Enter project
cd my-first-project

# Install package
uv add numpy

# Install from requirements
uv add -r requirements.txt

# Sync dependencies
uv sync

# Generate/update lock file
uv lock

Overall, today's session established a solid foundation for Python development by setting up a modern development workflow with UV and introducing the basics of package management, project initialization, Python fundamentals, and working with external APIs.



06/27/2026 7:30pm to 10:30pm PST
