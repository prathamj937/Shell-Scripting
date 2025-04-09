# 🛠️ ShellScript Toolkit: User Creation & Automated Backups

This project contains useful Bash scripts to help automate common system tasks:

- 👤 **User Creation Script (`create_user.sh`)**
- 💾 **Automated Folder Backup Script (`backup.sh`)**

## 🔧 1. `create_user.sh` — System User Creation

### 📝 Description
This script allows you to add a new system user and set a password using the terminal.

### ✅ Works On:
- ✅ **Linux (Ubuntu, Debian, etc.)**
- ❌ **Not supported on Git Bash (Windows)**

### 🛠️ Usage (Linux Only)
```bash
chmod +x create_user.sh
sudo ./create_user.sh

2. This script compresses the backup_me directory into a .tar.gz file and saves it in the backups directory. It also deletes backup files older than 7 days.

✅ Works On:
✅ Linux

✅ Git Bash (Windows)

⚙️ Edit the Script with Your Paths
bash
Copy
Edit
# Use forward slashes and full paths
SOURCE_DIR="/c/Users/YourName/Desktop/backup_me"
BACKUP_DIR="/c/Users/YourName/Desktop/backups"
🛠️ Usage
bash
Copy
Edit
chmod +x backup.sh
./backup.sh
📅 Schedule it Automatically on Linux with Cron
You can automate the backup using cron:

bash
Copy
Edit
crontab -e
Add this to run the script daily at 2 AM:

pgsql
Copy
Edit
0 2 * * * /full/path/to/backup.sh
🧼 Auto-Delete Old Backups
backup.sh includes:

bash
Copy
Edit
find "$BACKUP_DIR" -name "*.tar.gz" -type f -mtime +7 -exec rm {} \;
This line deletes .tar.gz files older than 7 days to keep your backup folder clean.

❗ Common Issues & Fixes
Error	Solution
useradd: command not found	Run only on Linux
tar: Cannot stat: Not a directory	Ensure source and backup folders exist
Permission denied	Use chmod +x script.sh to make scripts executable
tar: Removing leading '/'	Normal warning; tar strips root directory paths
📚 What is a Cron Job?
A cron job is a time-based job scheduler in Unix-like systems. You can schedule tasks like backups, cleanups, etc.

For example:

pgsql
Copy
Edit
0 2 * * * /path/to/backup.sh
Runs the backup at 2:00 AM every day.

👨‍💻 Author
Made by Pratham Jain
A beginner-friendly toolkit to learn and practice Bash scripting & automation.

