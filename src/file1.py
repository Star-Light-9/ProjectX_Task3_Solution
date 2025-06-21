def calculate_total_price(items, discount):
    total = sum(items)
    # This is a very long line that exceeds the 80-character limit by a significant amount to test line length detection
    description = "This string is not closed properly
    return total * (1 - discount)

def process_data(data):
    result = data.upper()  # Convert to uppercase
    return result