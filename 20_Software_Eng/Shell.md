# Shell Scripting

**Tags:** #tool #shell
**Related:** [[]]

## TL;DR

```sh
#!/bin/bash -- This is called shebang. Tells system which interpreter to use. 

echo "Hello, Captain!"

chmod +x file.sh # By default files are not executable. Change permissions.
./file.sh # Run shell script. 

NAME="Vinay"
AGE=27

echo "My name is $NAME and I am $AGE years old."

CURRENT_DIR=$(pwd)
echo "I am currently in $CURRENT_DIR"

read USER_NAME # Makes script interactive.
```

```sh
read NUM

if [ "$NUM" -gt 10 ]; then # Must have spaces inside brackets. 
    echo ">10"
elif [ "$NUM" -eq 10 ]; then 
    echo "=10"
else
    echo "<10"
fi

# [ -f "file.txt" ]: True if file exists.
# [ -d "directory_name" ]: True if directory exists.
# [ -z "$VAR" ]: True if string is empty.
```

```sh
for NAME in Alice Bob Charlie; do
    echo "Hello, $NAME"
done

for FILE in *.txt; do # Loop through files in directory
    echo "Found text file: $FILE"
done

COUNT=1
while [ $COUNT -le 5 ]; do 
    echo "Count is $COUNT"
    ((COUNT++)) # Double paranthesis allow C-Style math
done

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Total number of arguments: $#"
```

```sh backup.sh
#!/bin/bash

SOURCE_DIR="project_files"
BACKUP_DIR="backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 1. Check if source exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Directory '$SOURCE_DIR' does not exist."
    exit 1  # Exit with error code
fi

# 2. Create backup folder if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory..."
    mkdir "$BACKUP_DIR"
fi

# 3. Create the archive
TAR_NAME="backup_$TIMESTAMP.tar.gz"
tar -czf "$BACKUP_DIR/$TAR_NAME" "$SOURCE_DIR"

echo "Backup of '$SOURCE_DIR' completed successfully at $BACKUP_DIR/$TAR_NAME"
```

## Details

```sh organize.sh
#!/bin/bash

# 1. Set the directory to organize
# defaults to the current folder if no argument is provided
DIR="${1:-.}"

# Check if directory exists
if [ ! -d "$DIR" ]; then
    echo "Error: Directory '$DIR' does not exist."
    exit 1
fi

echo "Organizing files in: $DIR"

# 2. Change into that directory so we don't have to type long paths
cd "$DIR" || exit

# 3. Loop through every file in the directory
# syntax: * matches every file (ignoring hidden files)
for file in *; do
    
    # Skip directories, we only want to move files
    if [ -d "$file" ]; then
        continue
    fi

    # Skip the script itself if it's inside the folder
    if [ "$file" == "organize.sh" ]; then
        continue
    fi

    # 4. Extract the extension
    # ${file##*.} strips everything up to the last dot
    # ,, converts it to lowercase (bash 4.0+)
    ext="${file##*.}"
    ext="${ext,,}" 

    # 5. Decide where to move the file using a CASE statement
    case "$ext" in
        (jpg|jpeg|png|gif|svg|heic)
            SUBFOLDER="Images"
            ;;
        (pdf|doc|docx|txt|md|csv|ppt|pptx)
            SUBFOLDER="Documents"
            ;;
        (zip|tar|gz|rar|7z)
            SUBFOLDER="Archives"
            ;;
        (mp4|mov|avi|mkv)
            SUBFOLDER="Videos"
            ;;
        (mp3|wav|aac)
            SUBFOLDER="Audio"
            ;;
        (dmg|pkg|iso|exe)
            SUBFOLDER="Installers"
            ;;
        (py|js|html|css|cpp|c|sh)
            SUBFOLDER="Code"
            ;;
        (*)
            SUBFOLDER="Others"
            ;;
    esac

    # 6. Create the folder if it doesn't exist
    # -p means "no error if existing, make parent directories as needed"
    mkdir -p "$SUBFOLDER"

    # 7. Move the file
    # -n means "no clobber" (don't overwrite if file already exists)
    mv -n "$file" "$SUBFOLDER/"
    
    echo "Moved: $file -> $SUBFOLDER"

done

echo "✅ Organization Complete!"
```

<br/><br/>

