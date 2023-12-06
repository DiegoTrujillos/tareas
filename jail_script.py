
def execute_command(command, capture_output=True, time_limit=3, halt_on_failure=True):
    "Execute a system command and log its output"
    result = ""
    try:
        if capture_output:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            result, error = process.communicate(timeout=time_limit)
            exit_code = process.returncode
        else:
            exit_code = subprocess.call(command, stderr=subprocess.STDOUT, shell=True, timeout=time_limit)
        if exit_code != 0 and halt_on_failure:
            print(result)
    except subprocess.CalledProcessError as error:
        if halt_on_failure:
            print('Command execution failed: %s' % str(error))
    except Exception as error:
        if halt_on_failure:
            print('Command execution error: %s' % str(error))
    return result

def validate_string(input_str):
    regex_pattern = r'[^\.abcdefgijklmnopqrstuwxz:-\s]'
    if re.search(regex_pattern, input_str):
        print("Unaccepted characters detected")
