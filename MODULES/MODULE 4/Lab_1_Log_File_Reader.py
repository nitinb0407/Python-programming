# MODULE 4 - LAB EXERCISE 1
# Log file reader program.
# Create sample.log in the same folder before running.

file_name = input("Enter log file name: ")
try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print("Log file contents:")
    for line in lines:
        print(line.rstrip())
    print("Total lines:", len(lines))
except FileNotFoundError:
    print("File not found.")

# SAMPLE FILE (sample.log)
# INFO: Application started
# WARNING: Low disk space
# ERROR: Unable to connect
# SAMPLE INPUT
# Enter log file name: sample.log
# SAMPLE OUTPUT
# Log file contents:
# INFO: Application started
# WARNING: Low disk space
# ERROR: Unable to connect
# Total lines: 3
