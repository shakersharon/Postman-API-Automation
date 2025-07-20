import subprocess

def run_newman():
    print("Running Newman tests...")
    cmd = [
        "C:/Users/a/AppData/Roaming/npm/newman.cmd",  # Use forward slashes or double backslashes
        "run", "postman/collections/crud_tests.postman_collection.json",
        "-e", "postman/environments/local_env.postman_environment.json",
        "--iteration-data", "postman/data/users.csv",
        "--reporters", "cli,html",
        "--reporter-html-export", "newman/reports/report.html"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    print(result.stdout)
    if result.returncode != 0:
        print("❌ Newman tests failed!")
        print(result.stderr)
    else:
        print("✅ Newman tests completed successfully.")

if __name__ == "__main__":
    run_newman()
