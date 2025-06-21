def risky_function(data):
    print("Debugging data")  # Forbidden keyword
    # eval is in a comment, should not count
    result = eval(data)  # Forbidden keyword
    very_long_variable_name_to_test_line_length_limit_which_should_trigger_violation = 100
    exec("x = 42")  # Forbidden keyword
    return result

# print("This is a comment") - should not count
def safe_function():
    return "Safe"