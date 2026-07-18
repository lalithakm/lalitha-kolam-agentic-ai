## A.Pydantic Overview
Pydantic is a Python data validation system that ensures incoming data is correct before it enters your program, similar to how online forms validate inputs.
If data is wrong (wrong type, missing fields, bad format), it immediately raises a ValidationError instead of letting bad data pass.

## B. Why Pydantic Exists

Pydantic is the data validation library for Python.
In a job application form:
Correct input → accepted and Wrong input → rejected instantly
Pydantic does the following:
Checks types
Ensures required fields exist
Validates formats
Performs Type coercion

## C. Model Types Comparison

BaseModel vs. dataclass vs. a plain class 
### Plain Class
No validation
No type checking
Accepts anything (unsafe)

### Dataclass
@dataclass
class User:
    name: str
    age: int

Auto constructor + utilities
Uses type hints
❌ No validation

### Pydantic BaseModel
class UserModel(BaseModel):
    name: str
    age: int

✅ Validates every field
✅ Auto type conversion
❌ Raises ValidationError on invalid input
Best for APIs, AI apps, data pipelines

## D. Field Validation (Field)
Used to add constraints and rules:
full_name: str = Field(min_length=2, max_length=100)
years_experience: int = Field(ge=0, le=50)
Key idea:
Defines limits like min/max length, range checks, etc.

## E. Field Validator (Single Field Validation)
Used to validate one field at a time:
@field_validator("email")
@classmethod
def reject_disposable_domains(cls, value: str) -> str:

### Meaning:
Runs validation on a single field
Can reject invalid formats or domains
Must return cleaned/validated value

## F. Model Validator (Multiple Fields)
Used when validation depends on multiple fields together:
@model_validator(mode="after")

### Key idea:
Runs after all fields are parsed
Validates relationships between fields (e.g., age vs experience)

## G. Computed Field
@computed_field
@property

### Key idea:
Field is not input
It is derived from other fields
Example: full name, total score, etc.

## H. AI Terms Covered
LLMs → Large Language Models
Tokens → Text chunks processed by models
Vectors (Embeddings) → Numerical representation of data
Context Window → How much text an AI can “remember” at once


## Key Take Aways 
Pydantic is Python's data validation library.
BaseModel helps validate data before object creation.
Field() adds validation rules and metadata.
Field Validators validate individual fields.
Model Validators validate relationships across multiple fields.
Computed Fields automatically derive values.
Nested Models organize and validate complex objects.
Type coercion converts compatible values safely.
AI Terms explained
