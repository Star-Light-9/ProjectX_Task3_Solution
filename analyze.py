import os

def analyze_file(filename) :
  
  # Open file in read mode
  with open (filename, 'r') as reader :

    # Initilations
    c, n, violation = 0, 0, 0
    stack = []
    alreadycounted = False

    # Loop to read one character each time
    while True:

      # Store one character
      char = reader.read(1)

      # If end of file - stop
      if not char :
        break

      # If end of line reinitialise counters
      elif char == '\n' :
        c = 0
        alreadycounted = False

      # Ignore spaces
      elif char == ' ' :
        continue
          
      # Check for string violation
      elif char == '\'' or char == '\"' :
        if stack and stack[-1] == char :
          stack.pop()
        else :
          stack.append(char)

      # Check for length violation
      elif c >= 80 and not alreadycounted :
        violation += 1
        alreadycounted = True
        continue
      else :
        c += 1

    # If stack is not empty, string is not closed with prorper quotations
    if stack :
      violation += 1

    # Bring file pointer to start of file
    reader.seek(0)

    # Read entire file at once
    content = reader.read()

    # Check for risk words
    for risk in ['eval(', 'exec(', 'print'] :
      if risk in content :
        violation +=1
        n += 1

    # Determine the risk assesment of file
    if violation == 0 :
      clean = "CLEAN"
    elif violation <= 5 and n == 0 :
      clean = "LOW"
    elif violation > 5 or n > 0:
      clean = "HIGH"

    # Print riskiness
    print(f"{filename} : {clean}")


def scan_directory(root='src'):
  for dirpath, _, filenames in os.walk(root):
    for file in filenames:

      # Only check files with .py
      if file.endswith('.py'):

        # Path of the file
        filepath = os.path.join(dirpath, file)

        # Call function
        analyze_file(filepath)


if __name__ == "__main__":
    scan_directory()