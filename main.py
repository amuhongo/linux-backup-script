
- `backup.sh`:
```bash
#!/bin/bash

DIR=$1
DEST="$HOME/backups"

mkdir -p "$DEST"
DATE=$(date +%Y-%m-%d)
tar -czvf "$DEST/backup-$DATE.tar.gz" "$DIR"

echo "Backup realizado com sucesso: $DEST/backup-$DATE.tar.gz"
