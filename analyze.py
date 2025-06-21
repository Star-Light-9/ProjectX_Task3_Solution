import os

def analyze_file(filename) :
  # Open file in read mode
  with open(filename, 'r') as reader :
    # Read line by line
    lines = reader.readlines()

    # Initialization
    n, violation = 0, 0

    # Access each line
    for line in lines :
      # Remove eol and trailing white spaces
      line = line.rstrip()

      # Check line length
      if len(line) > 80 :
        violation += 1

      # Remove comments
      line = line.split('#')[0]

      # Count number of quotes, if odd, invalid
      single_quote = line.count('\'')
      double_quote = line.count('\"')
      if single_quote % 2 != 0 or double_quote % 2 != 0 :
        violation += 1
      
      # Check for risk words
      for risk in ['eval(', 'exec(', 'print'] :
        if risk in line :
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
