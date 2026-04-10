## Setup

### Sitemap Generation Setup using Git Hooks

```bash
touch .git/hooks/pre-commit
```

```py
#!/usr/bin/env python3
import os
import subprocess
import datetime

OUTPUT_FILE = "sitemap.md"
# Add exact folder names to ignore anywhere in the tree
IGNORE_DIR_NAMES = {'.git', 'dump', 'assets', 'Course_Materials'}

def generate_sitemap():
    lines = ["# 🗺️ Repository Sitemap\n"]
    lines.append(f"> Auto-generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for root, dirs, files in os.walk('.'):
        # Modifying 'dirs' in-place tells os.walk to completely skip those directories and their contents
        dirs[:] = sorted([d for d in dirs if not d.startswith('.') and d not in IGNORE_DIR_NAMES])
        
        if root == '.':
            indent_level = 0
        else:
            rel_dir = os.path.relpath(root, '.')
            indent_level = rel_dir.count(os.sep) + 1
            folder_name = os.path.basename(root)
            safe_path = rel_dir.replace('\\', '/')
            lines.append(f"{'  ' * (indent_level - 1)}- 📁 **[{folder_name}](./{safe_path})**")
        
        for f in sorted(files):
            if f.startswith('.') or f == OUTPUT_FILE: 
                continue
            rel_file = os.path.relpath(os.path.join(root, f), '.')
            safe_path = rel_file.replace('\\', '/')
            icon = "📄" if f.endswith('.md') else "🔧"
            lines.append(f"{'  ' * indent_level}- {icon} [{f}](./{safe_path})")
            
    return '\n'.join(lines)

if __name__ == "__main__":
    sitemap_content = generate_sitemap()
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(sitemap_content + '\n')
    subprocess.run(['git', 'add', OUTPUT_FILE])
```

```bash
chmod +x .git/hooks/pre-commit
```


### Wipe Commit History and Start Fresh

```bash
# 1. Create a completely empty, disconnected temporary branch
# Zero connection to previous commits. 
git checkout --orphan temp_branch 

# 2. Stage all your current files (and your auto-generated sitemap!)
git add -A

# 3. Create your shiny new "Initial" commit
git commit -m "chore: fresh start"

# 4. Delete the old local branch (assuming it is named 'main')
git branch -D main

# 5. Rename your temporary branch to 'main'
git branch -m main

# 6. Force push to overwrite the remote repository
git push -f origin main
```


### Common Git Commands

```bash
git init

# Tell Git where your remote repository (GitHub/GitLab) lives
git remote add origin https://github.com/yourusername/personal_notes.git

# Rename the default branch to 'main' (modern standard)
git branch -M main

# Push all files to the cloud and permanently link 'main' to 'origin/main' (-u)
git push -u origin main

# Tell Git to keep a clean, linear history by rebasing instead of merging 
# when you pull changes from your other laptop.
git config --global pull.rebase true

# Check which files have been modified, added, or deleted
git status

# Stage ALL changes (readying them to be saved)
git add .

# Save the staged changes to your local history with a message
git commit -m "docs: updated python and rust notes"

# Send the new commit to the cloud
git push

# View your beautiful, clean, linear history
git log --oneline --graph

# See the exact lines of text you changed in unstaged files
git diff

# See the exact lines of text in files you already ran 'git add' on
git diff --staged

# View the text differences of your last 3 commits
git log -p -3

# You made a typo in the last commit message, or forgot to add a file.
# Stage the forgotten file, then run this to merge it into the last commit.
git commit --amend -m "new corrected message"

# You accidentally ran 'git add .' but want to un-stage a specific file.
# Your modifications to the file are perfectly safe.
git restore --staged <file.md>

# ☢️ WARNING: You butchered a file and want to throw away your uncommitted changes.
# This permanently reverts the file to exactly how it was in the last commit.
git restore <file.md>


# Note: HEAD~1 means "Go back exactly 1 commit from where I am right now."
# You can change it to HEAD~3 to go back 3 commits.

# --- SOFT RESET ---
# Use case: You committed too early.
# Action: Deletes the last commit, but keeps all your modified files EXACTLY
# as they are AND keeps them in the staging area (already git add'ed).
git reset --soft HEAD~1

# --- MIXED RESET (The Default) ---
# Use case: You want to completely reorganize your last commit.
# Action: Deletes the last commit, keeps your files modified on your hard drive, 
# but un-stages them (you have to run 'git add' again).
git reset HEAD~1

# --- HARD RESET ☢️ ---
# Use case: You completely ruined everything in the last commit. 
# Action: Deletes the last commit AND DESTROYS all file changes. 
# Your folder goes back to looking exactly like the commit before it.
git reset --hard HEAD~1

# --- THE "NUKE FROM ORBIT" RESET ☢️ ---
# Use case: Your local folder is hopelessly broken, but GitHub is pristine.
# Action: Throw away ALL local commits and uncommitted changes, and make 
# your folder perfectly match the cloud.
git fetch origin
git reset --hard origin/main


# Use case: You are halfway through writing a note, but need to pull from 
# the cloud, or switch branches, and Git won't let you because of uncommitted work.

# Hide all your uncommitted changes in a temporary clipboard.
# Your working directory is now clean.
git stash

# Hide your changes, but give the stash a specific name so you remember what it is.
# (Highly recommended if you stash frequently).
git stash push -m "half-finished kubernetes tutorial"

# View a list of everything you currently have stashed
# Output looks like: stash@{0}: half-finished kubernetes tutorial
# Output looks like: stash@{1}: WIP on main
git stash list

# Take the most recent stash, apply it to your current folder, 
# AND delete it from the stash clipboard.
git stash pop

# Apply a SPECIFIC stash from your list, and delete it from the clipboard.
git stash pop stash@{0}

# Apply a stash to your folder, but KEEP it in the clipboard just in case.
git stash apply stash@{1}

# Delete a specific stash from the clipboard without applying it.
git stash drop stash@{0}

# ☢️ Delete EVERY stash in your clipboard.
git stash clear
```

### Configuration 

```bash
# Note: --global applies to your entire user account on this laptop.
# Note: --local applies ONLY to the specific repository you are currently in.

# Set your name and email globally (Required by Git to make commits)
git config --global user.name "Future Me"
git config --global user.email "future.me@example.com"

# Override your email for ONE specific project (e.g., using a work email here)
git config --local user.email "work@company.com"

# Set 'main' as the default branch name for all future 'git init' commands
git config --global init.defaultBranch main

# Set VS Code as your default Git editor (for merge conflicts or commit messages)
git config --global core.editor "code --wait"
# OR set Nano/Vim if you prefer the terminal
git config --global core.editor "nano"

# Tell Git to cache your GitHub credentials (PAT) so you don't type it every time
# (Mac users: Git usually uses the OSX Keychain automatically)
# (Windows users: Git usually uses the Windows Credential Manager automatically)
# For Linux or basic caching (caches in memory for 15 minutes):
git config --global credential.helper cache

# List all your current configurations and where they are coming from
git config --list --show-origin

# View just your global settings
git config --global --list

# Open your global .gitconfig file in your default text editor to edit manually
git config --global -e

# Delete a specific configuration entirely
git config --global --unset user.name

# Delete an entire section of configurations
git config --global --remove-section user
```

```bash
# 🌿 8. BRANCHING (FEATURE DEVELOPMENT)
# Rule of thumb: Never build new features directly on 'main'. 
# Create a branch, build the feature, then merge it back.

# Create a new branch and instantly switch to it
# (Note: 'switch -c' is the modern replacement for 'checkout -b')
git switch -c feature/new-database-schema

# See a list of all local branches (the one with the * is where you are)
git branch

# Switch back to the main branch
git switch main

# Merge your finished feature branch into main 
# (Make sure you are ON main when you run this)
git merge feature/new-database-schema

# Delete the feature branch locally now that it's merged
git branch -d feature/new-database-schema


# 🧬 9. ADVANCED SURGERY (CHERRY-PICK & REBASE)

# --- CHERRY PICKING ---
# Use case: You fixed a bug on a test branch and want to pull EXACTLY 
# that single commit into main, without merging the whole test branch.
# Action: Finds the commit and duplicates it onto your current branch.
git cherry-pick <commit-hash>

# --- INTERACTIVE REBASE ---
# Use case: You made 5 messy "WIP" commits while trying to get a script to work.
# You want to squash them into 1 beautiful commit before pushing.
# Action: Opens a text editor letting you squash, reword, or drop the last 3 commits.
git rebase -i HEAD~3

# 🕵️ 10. DEBUGGING & SLEUTHING 
# --- GIT BLAME ---
# Use case: You found a terrible line of code and want to know who wrote it 
# and in which commit so you can understand WHY they did it.
git blame path/to/broken_script.py

# --- GIT BISECT ---
# Use case: The app is broken. It worked yesterday. There are 50 commits between 
# yesterday and today. You need to find EXACTLY which commit broke it.
# Action: Git performs a binary search, checking out commits halfway between 
# 'good' and 'bad' and asking you "Is it broken here?" until it isolates the bug.
git bisect start
git bisect bad                 # Tell Git the current commit is broken
git bisect good <commit-hash>  # Tell Git a past commit where it worked
# Git will checkout a commit. You test the app, then type either:
# git bisect good OR git bisect bad. 
# Repeat until Git tells you the culprit. Type 'git bisect reset' to end.


# 🧹 11. HOUSEKEEPING & RELEASES

# --- GIT CLEAN ---
# Use case: You ran a script that generated 100 temporary files not tracked by Git.
# Action: Forcibly deletes all untracked files and directories in your repo.
# ☢️ Run 'git clean -n' first to do a dry-run and see what it WILL delete.
git clean -fd

# --- PRUNING ---
# Use case: Your coworkers merged and deleted 20 branches on GitHub, 
# but your local Git still thinks they exist. 
# Action: Cleans up your local list of remote branches.
git fetch --prune

# --- TAGGING ---
# Use case: You hit version 1.0 of your project and want to mark it forever.
# Action: Creates a release tag. You must push tags separately!
git tag -a v1.0.0 -m "Initial Stable Release"
git push origin v1.0.0
```


### 🛠️ Git & Package Management

#### 🌳 Git Core Concepts
* **Distributed VCS**: Every contributor has a *local copy* of the entire project history.
* **The Three States**: 
    1.  **Working Directory**: Modified files not yet staged.
    2.  **Staging Area (Index)**: Files marked to be included in the next snapshot.
    3.  **Repository (.git)**: Permanently stored snapshots.
* **SHA-1 Hashing**: Git identifies everything by a unique 40-character checksum.

#### ⌨️ Essential Git Commands
* `git init`: Transform a directory into a Git repository.
* `git add`: Move changes from *Working Directory* to *Staging*.
* `git commit`: Create a permanent snapshot of the staged changes.
* `git push/pull`: Synchronize local changes with a *remote* server.
* `git rm --cached`: Remove a file from tracking *without* deleting it from the disk.
* `git checkout -b`: Create and switch to a new **pointer** (branch).

#### 📦 Package Managers
* **apt-get (Debian/Ubuntu)**: Standard for Linux servers.
* **yum / dnf (RHEL/CentOS)**: Common in enterprise Linux environments.
* **Homebrew (macOS/Linux)**: The "missing package manager" for Mac users.

> **💡 Pro-Tip:** Use `git rebase` for a cleaner, linear history, but *never* rebase commits that have already been pushed to a shared public repository.