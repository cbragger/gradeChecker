import subprocess
import re
def run_code(file_path):
    """Run the provided Python code file and return its output."""
    try:
        result = subprocess.run(['python', file_path], capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Execution timed out"
    except Exception as e:
        return str(e)

def compare_outputs(prof_output, student_output):
    """Compare the professor's output with the student's output."""
    return prof_output == student_output

def detect_hard_coding(student_code, test_cases):
    """Check if the student's code contains hard-coded answers."""
    for input_val, expected_output in test_cases:
        # Create a temporary file to execute student's code
        with open('student_temp.py', 'w') as temp_file:
            temp_file.write(student_code)
        
        # Run the student's code with the test input
        output = run_code('student_temp.py')
        
        if output != expected_output:
            return False
    
    # Check for static values in student's code
    hard_coded_patterns = re.findall(r'\b\d+\b', student_code)
    for pattern in hard_coded_patterns:
        if pattern.isdigit() and int(pattern) in [55]:  # Example check for known hard-coded answers
            return True
            
    return False

def grade_assignment(prof_file, student_file):
    # Run the professor's code
    prof_output = run_code(prof_file)
    
    # Run the student's code
    student_output = run_code(student_file)
    
    # Compare outputs
    if not compare_outputs(prof_output, student_output):
        return 0, "Output does not match the expected output."
    
    # Read student code
    with open(student_file, 'r') as file:
        student_code = file.read()
    
    # Create temporary test cases for detection (based on known inputs and outputs)
    test_cases = [(10, prof_output)]
    
    if detect_hard_coding(student_code, test_cases):
        return 0, "Hard-coded solution detected."
    
    # If everything checks out
    return 100, "Correct output with acceptable logic."

# Example usage:
professor_file = 'professor_solution.py'
student_file_correct = 'student_submission_correct.py'
student_file_hardcoded = 'student_submission_hardcoded.py'

grade_correct, feedback_correct = grade_assignment(professor_file, student_file_correct)
print(f"Correct Submission -> Grade: {grade_correct}, Feedback: {feedback_correct}")

grade_hardcoded, feedback_hardcoded = grade_assignment(professor_file, student_file_hardcoded)
print(f"Hardcoded Submission -> Grade: {grade_hardcoded}, Feedback: {feedback_hardcoded}")
