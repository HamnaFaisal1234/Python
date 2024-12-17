def calculate_time_complexity(code_snippet):
    
    if "for" in code_snippet or "while" in code_snippet:
        
        if code_snippet.count("for") > 1 or code_snippet.count("while") > 1:
            complexity = "O(n^2)"  
        else:
            complexity = "O(n)"  
    else:
        complexity = "O(1)"  

    print(f"The estimated time complexity is: {complexity}")



example_code = """
for i in range(n):
    print(i)
"""


calculate_time_complexity(example_code)
