import requests
import subprocess
import os
def update_script():
    url = "https://raw.githubusercontent.com/chickenMuggets/updater-test/main/latest.py"
    try:
        response = requests.get(url, verify=True)
        response.raise_for_status()
        currentFile = open(f"{os.getcwd()}\\asdwasd.py","r").read()
        print(currentFile)
        print(response.text)
        if response.text == currentFile:
            print("equal")
        if currentFile == response.text:
            print("No update available")
            run_payload()
            quit()
        else:
            print("No old file found")
            with open("updated_script.py", "w") as f:
                f.write(response.text)
            print("Script updated successfully!")
            run_updated_script()
    except Exception as e:
        print(f"Failed to update script: {e}")

def run_payload():
    # Add your payload code here
    subprocess.run(["calc.exe"])  # Example payload to open the calculator
def run_updated_script():
    # Add your code to run the updated script
    subprocess.run(["python", "updated_script.py"])
    quit()

if __name__ == "__main__":
    update_script()
