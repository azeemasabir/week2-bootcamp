import schedule
import time
import subprocess

FOLDER_PATH = r"C:\path\to\images"  # Change this to your folder

def run_bulk_rename():
    print("Running bulk rename job...")
    subprocess.run(["python", "bulk_rename.py", FOLDER_PATH])

# Schedule daily at 09:00 AM
schedule.every().day.at("09:00").do(run_bulk_rename)

print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)
