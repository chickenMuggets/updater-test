import requests
import subprocess
import os
def update_script():
    url = "https://raw.githubusercontent.com/chickenMuggets/updater-test/main/latest.py"
    try:
        response = requests.get(url, verify=True)
        response.raise_for_status()
        currentFile = open(f"{os.getcwd()}\\asdwasd.py","r").read()
        if currentFile == response.text:
            os.remove("updated_script.py")
            print("Removed old file")
        else:
            print("No old file found")
            with open("updated_script.py", "w") as f:
                f.write(response.text)
            print("Script updated successfully!")
        run_payload()
    except Exception as e:
        print(f"Failed to update script: {e}")

def run_payload():
    # Add your payload code here
    subprocess.run(["calc.exe"])  # Example payload to open the calculator

if __name__ == "__main__":
    update_script()
