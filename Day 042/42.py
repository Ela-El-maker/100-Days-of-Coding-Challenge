import os

# Define the device serial number
device_serial = '1234567890ABCDEF'

# Define the command to connect to the device
command = f'adb -s {device_serial} shell'

# Execute the command using the subprocess module
process = os.popen(command)

# Print the output of the command
output = process.read()
print(output)