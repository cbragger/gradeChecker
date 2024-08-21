def run_code(script_name, input_value):
    result = subprocess.run(['python3', script_name, str(input_value)], capture_output=True, text=True)
    return result.stdout.strip()

