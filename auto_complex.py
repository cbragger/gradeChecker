import unittest
import importlib.util
import os
import inspect
import block2_ex2_solution

def load_solution_code(block2_ex2_solution):
    """Load the solution code from a Python file."""
    file_path = block2_ex2_solution
    spec = importlib.util.spec_from_file_location("solution", file_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution

def generate_unit_tests(solution, criteria):
    # Create a dictionary to store dynamically generated test cases
    test_cases = {}

    # Criteria for testing
    def test_while_loop():
        code = inspect.getsource(solution.password_check)
        assert "while" in code, "The code must contain a while loop."

    def test_max_attempts_check():
        code = inspect.getsource(solution.password_check)
        assert "attempts == max_attempts" in code or "< max_attempts" in code, "The code must check for maximum attempts."

    def test_success_message():
        code = inspect.getsource(solution.password_check)
        assert "Welcome" in code, "The code must print a welcome message when the password is correct."

    def test_failure_message():
        code = inspect.getsource(solution.password_check)
        assert "Wrong password! You have tried and failed" in code, "The code must inform the user of failed attempts."

    def test_exit_condition():
        code = inspect.getsource(solution.password_check)
        assert "Exiting the application" in code or "break" in code, "The code must exit after 3 failed attempts."

    def test_password_check():
        code = inspect.getsource(solution.password_check)
        assert "user_password == correct_password" in code, "The code must correctly check if the password is correct."

    # Mapping criteria to their respective test functions
    test_functions = {
        "while_loop": test_while_loop,
        "max_attempts_check": test_max_attempts_check,
        "success_message": test_success_message,
        "failure_message": test_failure_message,
        "exit_condition": test_exit_condition,
        "password_check": test_password_check,
    }

    # Dynamically add tests to the test_cases dictionary
    for criterion, test_function in test_functions.items():
        if criterion in criteria:
            test_cases[f"test_{criterion}"] = test_function

    # Create a new TestCase class with the generated test cases
    TestCaseClass = type("GeneratedTestCase", (unittest.TestCase,), test_cases)
    return TestCaseClass

def run_unit_tests(test_case_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    result = unittest.TextTestRunner().run(suite)
    return result

# Path to the solution file
solution_file = block2_ex2_solution

# Load the solution module
solution = load_solution_code(solution_file)

# Criteria to check
criteria = ["while_loop", "max_attempts_check", "success_message", "failure_message", "exit_condition", "password_check"]

# Generate the test case class based on the criteria
GeneratedTestCase = generate_unit_tests(solution, criteria)

# Run the generated unit tests
result = run_unit_tests(GeneratedTestCase)

# Output the results
if result.wasSuccessful():
    print("All tests passed!")
else:
    print("Some tests failed.")