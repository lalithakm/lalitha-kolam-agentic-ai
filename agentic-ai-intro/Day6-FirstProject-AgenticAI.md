# Learning Summary & Key Takeaways for Day 6 

## 🚀 Practical 6: Building a Complete AI Agent

- All agent components are assembled together
- Assembled agent: brain + tool + schema + loop
- Combines the LLM (brain), tool schemas, actual Python tools, and conversation memory into one complete application.
    - Brain - The brain is the LLM. The brain reasons. It does NOT actually execute Python code. LLM could be GPT-4o, Llama, DeepSeek, Qwen etc
        *<span style="color:red;">client.chat.completions.create(...)</span>*

    - Tools - The tools are Python functions.
    *<span style="color:red;"> def get_weather(city)</span>*
    *<span style="color:red;"> def get_currency(...)</span>*
    
    - The LLM cannot execute Python itself. Instead it says
    "Please execute get_weather(city='Tokyo')."
    The Python program executes it.
    
    - TOOLS Schema
    The schema tells the LLM
    "These are the tools you are allowed to use."
    Without this schema, the LLM has no idea the function exists.

    *<span style="color:red;"> TOOL_SCHEMAS = [ { "type": "function", ... } ]</span>*
    
    - TOOLS_BY_NAME
    This maps Tool name to Python Function
    *<span style="color:red;"> TOOLS_BY_NAME = {"get_weather": get_weather}</span>*
    
    - Agent loop
    It lets the LLM repeatedly think, call tools, observe results, and continue reasoning until it's ready to answer. 
    Without this loop, the model can only use one reasoning step.
    Here max_turns=4 is a good safety limit, but if a task requires more tool calls, the agent will stop early with "Reached max_turns without a final answer."

     *<span style="color:red;"> for _ in range(max_turns): </span>*
     
     Think
     ↓
     Need tool?
     ↓
     Call tool
     ↓
     See result
     ↓
     Need another tool?
     ↓
     Call another
     ↓
     Finally answer
     
     - This pattern is the foundation of modern agent frameworks like LangGraph


## 🚀 LangChain Introduction

- Langchain Installation
    - uv init
    - uv add langchain langchain-openai langchain-anthropic
    - uv sync


- Instead of manually building the agentic loop in the previous example, LangChain does all of that for you.
    - Define tools
    - Send request to the LLM
    - Check tool_calls
    - Execute the tool
    - Send tool output back
    - Repeat


- Instead of writing all the additional lines of agent loop, you write the below line of code and LangChain creates an entire agent that automatically handles the reasoning, tool execution, memory, and loop. 
    - *<span style="color:red;"> agent = create_agent(...) </span>*
    - *<span style="color:red;"> @tool </span>* generates tool metadata (similar to Create TOOL_SCHEMAS)
    - *<span style="color:red;"> agent.invoke() </span>* replaces the manual run_agent() function.
