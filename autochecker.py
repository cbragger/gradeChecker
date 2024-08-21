import subprocess
import difflib
import re

def run_code(script_name, input_value):
    try:
        result = subprocess.run(['python3', script_name, str(input_value)], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running code: {e}")
        return ""

def compare_outputs(student_output, expected_output):
    try:
        student_output_num = float(student_output)
        expected_output_num = float(expected_output)
        return student_output_num == expected_output_num
    except ValueError:
        return student_output.strip() == expected_output.strip()

def provide_feedback(student_output, expected_output):
    diff = difflib.ndiff(
        expected_output.splitlines(),
        student_output.splitlines()
    )
    feedback = []
    for line in diff:
        if line.startswith("- "):
            feedback.append(f"Expected: {line[2:]}")
        elif line.startswith("+ "):
            feedback.append(f"Your Output: {line[2:]}")
    return '\n'.join(feedback)

def explain_differences(student_output, expected_output):
    explanations = []

    if student_output.replace(" ", "") == expected_output.replace(" ", ""):
        explanations.append("Your output had extra or missing spaces, which made it incorrect.")
    
    elif student_output.lower() == expected_output.lower():
        explanations.append("Your output had incorrect capitalization.")
    
    elif re.sub(r'\W+', '', student_output) == re.sub(r'\W+', '', expected_output):
        explanations.append("Your output had incorrect or missing punctuation and does not match the expected output.")
    
    else:
        explanations.append("Your output did not match the expected output.")
    
    return explanations

def grade_submission(student_script, expected_output_file):
    with open(expected_output_file, 'r') as file:
        lines = file.readlines()
    
    # Adjust the number of test cases
    text_outputs = [line.strip() for line in lines[:3]]
    math_outputs = [line.strip() for line in lines[4:]]
    
    total_tests = len(text_outputs) + len(math_outputs)
    correct_tests = 0
    
    # Handle text test cases
    for i in range(len(text_outputs)):
        expected_output = text_outputs[i]
        student_output = run_code(student_script, i + 1)
        
        print(f"\nText Test case {i + 1}:")
        print(f"Expected Output:\n'{expected_output}'")
        print(f"Your Output:\n'{student_output}'")
        
        if compare_outputs(student_output, expected_output):
            correct_tests += 1
        else:
            print("Feedback:\n", provide_feedback(student_output, expected_output))
            explanations = explain_differences(student_output, expected_output)
            for explanation in explanations:
                print(f"Reason for point deduction: {explanation}")
    
    # Handle math test cases
    for i in range(len(math_outputs)):
        expected_output = math_outputs[i]
        student_output = run_code(student_script, i + len(text_outputs) + 1)
        
        print(f"\nMath Test case {i + 1}:")
        print(f"Expected Output:\n'{expected_output}'")
        print(f"Your Output:\n'{student_output}'")
        
        if compare_outputs(student_output, expected_output):
            correct_tests += 1
        else:
            print("Feedback:\n", provide_feedback(student_output, expected_output))
            explanations = explain_differences(student_output, expected_output)
            for explanation in explanations:
                print(f"Reason for point deduction: {explanation}")
    
    print("\n\nFinal Grade: {:.1f}%".format((correct_tests / total_tests) * 100))
    print(f"Correct tests: {correct_tests}/{total_tests}\n")

if __name__ == "__main__":
    student_script = 'student_code.py'
    expected_output_file = 'expected_output.txt'
    grade_submission(student_script, expected_output_file)
