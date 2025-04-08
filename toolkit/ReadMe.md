📝 Description
backup.sh is a simple shell script that automates the process of backing up a specified folder and compresses it into a .tar.gz file. It also includes a cleanup feature to automatically delete old backups (older than 7 days), helping you manage disk space.

📁 Folder Structure
bash
Copy
Edit
project-directory/
│
├── backup.sh                # Your backup script
├── /backups                 # Destination folder where backup files will be stored
└── /backup_me               # Source folder containing files to be backed up
Make sure the backups and backup_me folders exist before running the script (or let the script create backups automatically).

⚙️ How It Works
Takes the contents of backup_me directory.

Compresses it as backup-YYYY-MM-DD.tar.gz.

Saves it into the backups directory.

Deletes backups older than 7 days automatically.

🧰 Requirements
Git Bash or any Bash-compatible terminal

tar and find utilities (included in most Unix-like environments)

Unix-style paths (e.g., /c/Users/YourName/...) if using Git Bash on Windows

🚀 How to Run
Make script executable (first time only):

bash
Copy
Edit
chmod +x backup.sh
Run the script:

bash
Copy
Edit
./backup.sh
🧪 Example Output
bash
Copy
Edit
✅ Backup created at /c/Users/Pratham Jain/Desktop/backups/backup-2025-04-08.tar.gz
🧽 Checking for old backups to delete...
🗑️ Deleted backups older than 7 days.
🔐 Notes
The script will automatically create the backups folder if it doesn't exist.

If the backup_me directory doesn't exist, the script will show an error and exit.

📌 Customization
You can customize the following variables inside the script:

bash
Copy
Edit
BACKUP_DIR="/your/backup/folder"
SOURCE_DIR="/your/source/folder"
