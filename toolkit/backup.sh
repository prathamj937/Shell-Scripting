 
#!/bin/bash

BACKUP_DIR="/c/Users/Pratham Jain/Desktop/backups"
SOURCE_DIR="/c/Users/Pratham Jain/Desktop/backup_me"


DATE=$(date +%F)
FILENAME="backup-$DATE.tar.gz"

# Create the backup
tar -czf "$BACKUP_DIR/$FILENAME" "$SOURCE_DIR"

echo "✅ Backup created at $BACKUP_DIR/$FILENAME"
