import subprocess
import sys

requirements_file = "requirements.txt"


def install_dependencies():
    try:
        subprocess.check_call(["python3", "-m", "pip", "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")
    try:
        # Use pip3 to install the required packages from the requirements file using Python 3
        subprocess.check_call(["pip3", "install", "-r", requirements_file])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


# if __name__ == "__main__":
install_dependencies()
