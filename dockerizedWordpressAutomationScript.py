import subprocess
import os

# Check if the script is being run as the root user
current_user = subprocess.check_output("whoami", shell=True, text=True).strip()
if current_user != "root":
    print("Please switch to the root user by running 'sudo su -' before executing this script.")
    exit(1)

# Define a list of commands for the first set of actions
commands_set1 = [
    "yum install httpd -y",
    "yum install docker -y",
    "yum install git -y",
    "sudo systemctl start httpd",
    "sudo systemctl start docker",
    "curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose",
    "chmod +x /usr/local/bin/docker-compose",
    "git clone https://gist.github.com/21f213a4d02ee6ab219ee4c2c645b01d.git"
]

# Get the current working directory using the `pwd` command
current_directory = subprocess.check_output("pwd", shell=True, text=True).strip()

# Construct the new directory path
new_directory = os.path.join(current_directory, "21f213a4d02ee6ab219ee4c2c645b01d")

# Execute the first set of commands with exception handling
for cmd in commands_set1:
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print(f"Error message: {e}")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
else:
    print("First set of commands executed successfully.")
    
# Change the current working directory to the new directory
os.chdir(new_directory)

try:
    subprocess.run("docker-compose up -d", shell=True, check=True)
    result = subprocess.run("curl -4 -s icanhazip.com", shell=True, check=True, capture_output=True, text=True)
    output = "Copy & Paste the following Ip address in a new tab:  " + result.stdout.strip() + ":8080"
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed: {cmd}")
    print(f"Error message: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Change the working directory back to the original directory
os.chdir(current_directory)