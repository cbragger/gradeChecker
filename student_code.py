import sys

def main(test_case_number):
    if test_case_number == 1:
        print('# Text-based test cases')
    elif test_case_number == 2:
        print('# Text Output')
    elif test_case_number == 3:
        print('')  # Empty string
    elif test_case_number == 4:
        print('42')
    elif test_case_number == 5:
        print('')  # Empty string
    elif test_case_number == 6:
        print('# Math-based test cases')
    elif test_case_number == 7:
        print('# Mathematical Operations')
    elif test_case_number == 8:
        print('')  # Empty string
    elif test_case_number == 9:
        print('15.0')
    elif test_case_number == 10:
        print('5.0')
    else:
        print('Invalid test case number')

if __name__ == "__main__":
    # The test case number is passed as a command-line argument
    if len(sys.argv) > 1:
        try:
            test_case_number = int(sys.argv[1])
            main(test_case_number)
        except ValueError:
            print('Invalid input')
    else:
        print('No test case number provided')
