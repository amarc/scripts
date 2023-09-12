import subprocess

# Define a function to run shell commands and handle errors
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        exit(1)

# Get OS/distribution version and kernel version
try:
    print("Getting OS/distribution version and kernel version...")
    
    # Get OS/distribution version
    os_version = subprocess.check_output("lsb_release -d | cut -f2", shell=True, text=True).strip()
    print(f"OS/Distribution Version: {os_version}")

    # Get kernel version
    kernel_version = subprocess.check_output("uname -r", shell=True, text=True).strip()
    print(f"Kernel Version: {kernel_version}")

    print("\nUpdating package list...")
    run_command("sudo apt update")

    print("Upgrading installed packages...")
    run_command("sudo apt upgrade -y")

    print("Installing required packages...")
    packages = [
        "mariadb-server",
        "php-common",
        "php8.2-bcmath",
        "php8.2-cli",
        "php8.2-common",
        "php8.2-curl",
        "php8.2-fpm",
        "php8.2-gd",
        "php8.2-imagick",
        "php8.2-intl",
        "php8.2-mbstring",
        "php8.2-mysql",
        "php8.2-opcache",
        "php8.2-readline",
        "php8.2-xml",
        "php8.2-xmlrpc",
        "php8.2-zip",
        "nginx-extras",
    ]
    for package in packages:
        run_command(f"sudo apt install -y {package}")

    print("\nServer setup completed successfully!")
except KeyboardInterrupt:
    print("\nServer setup interrupted.")
except Exception as e:
    print(f"An error occurred during server setup: {str(e)}")

