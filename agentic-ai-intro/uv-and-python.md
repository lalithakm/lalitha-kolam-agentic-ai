UV & Python – Notes from Presentation
Date: 06/26/2026 (Session: 7:30PM - 10:30PMSPT)

Overview

This document summarizes key notes on using UV for python development, focusing on the key steps in setting up and using it.

Relevant Resources:
https://bugs-sleep-6uj.craft.me/agentic3 - This project provides some utilities related to UV, potentially useful for future projects or explorations of its capabilities.
(Note: this link is not immediately apparent as relevant based solely on the MD file's content.)
UV Package Manager – Key Instructions
Version: uv venv --python 3.12
Create a virtual environment using Python 3.12. This isolates your project and prevents conflicts from other Python versions in your system. Note: the .venv folder is created automatically by UV during the initial setup process.
Project Setup & Initialization (Using uv init)
Virtual Environment: Initialize a new virtual environment using uv init my-first-project. This provides a clean and reproducible Python development environment. You may require shell access that grants execution of PowerShell or bash, depending on your system's configuration. If you need more advanced shell control (e.g., running commands), configure it accordingly.
Initialization: After the initial setup, launch (activate) the project from the command line within the virtual environment. This steps can take a few minutes; observe any errors during startup if those are present and address them promptly.
Package Management – Dependencies & Installation
Package Acquisition: Use uv add numpy to add essential packages, allowing quick experimentation with common Python libraries.

Installation from requirements.txt: Run uv add -r requirements.txt to automatically install the required packages using the package-management files.

Python Fundamentals – Core Concepts

Covered Topics:
Variables: Holding data values in memory. Represented as strings or numeric types.
Data Types (Basic): Strings, integers, floating-points.
Syntax: Standard Python coding practices - use indentation, semicolons, comments etc.
Project Structure: Organizing files and functions related to your project's requirements. A src folder or a directory structure is often used for separating source code from build tools/tests.
Functions: Blocks of reusable code that perform specific tasks with a specified input and output.
Object-Oriented Concepts (OOP): Collections of variables and methods organizing related elements to create modularity, reuse, and maintainability across an application
API – Introduction to Application Programming Interfaces (APIs)
Introduced Application Programming Interfaces (APIs) offer standardized ways for different software systems to communicate with each other. An example is Frankfurter Currency API, which provides: * https://frankfurter.dev/, * [https://api.frankfurter.dev/v2/rates]

This API lets you retrieve real-time currency exchange rates for various currencies and assets through a streamlined request via HTTP protocol.

Learning Summary:

UV Use (Session: 06/26/2026, 7:30PM - 10:30PMSPT) - UV is now prioritized as a faster replacement for pip and venv, streamlining project setup and isolation. Focus was placed on project creation with uv init, dependency management (uv add), and synchronization.
End of Notes