import subprocess
import sys

# Function to execute ADB command
def run_adb_command(command):
    try:
        output = subprocess.check_output(['adb'] + command, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print('Error executing ADB command:', e.output.decode('utf-8'))
        return None

# Check if destination path argument is provided
if len(sys.argv) < 2:
    print('Error: Destination path argument is missing.')
    print('Usage: python script.py <destination_path>')
    sys.exit(1)

# Step 1: Transfer JSON file from Android device to computer
adb_pull_command = ['pull', '/mnt/vendor/persist/sensors/sensor_data.csv', sys.argv[1]]
run_adb_command(adb_pull_command)

# Step 2: Delete data within JSON file on Android device
adb_truncate_command = ['shell', 'truncate', '-s', '0', '/mnt/vendor/persist/sensors/sensor_data.csv']
run_adb_command(adb_truncate_command)

