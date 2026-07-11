# Git Commands Reference

A personal Git command reference compiled while learning Git.

---

# Repository Setup

Initialize a new repository:

```bash
git init
```

Rename the default branch to `main`:

```bash
git branch -M main
```

Add a remote repository:

```bash
git remote add origin <repo-url.git>
```

Push the first commit:

```bash
git push -u origin main
```

---

# Creating Files

Create an empty file:

```bash
touch <filename.ext>
```

Examples:

```bash
touch .gitignore
touch main.py config.py utils.py
```

---

# Echo

Print text to the terminal:

```bash
echo Hello
```

Write text to a file (Overwrite):

```bash
echo ".venv/" > .gitignore
```

Append text to a file:

```bash
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

---

# Repository Status

Check repository status:

```bash
git status
```

View commit history:

```bash
git log
```

Compact commit history:

```bash
git log --oneline
```

Last 5 commits:

```bash
git log --oneline -5
```

---

# Staging Files

Stage all files:

```bash
git add .
```

Stage a single file:

```bash
git add README.md
```

Stage multiple files:

```bash
git add file1.py file2.py
```

---

# Committing

Create a commit:

```bash
git commit -m "Your Commit Message"
```

Edit the last commit:

```bash
git commit --amend
```

Change only the commit message:

```bash
git commit --amend -m "New commit message"
```

Amend without editing the message:

```bash
git commit --amend --no-edit
```

---

# Push & Pull

Push commits:

```bash
git push
```

Pull changes:

```bash
git pull
```

Pull using rebase:

```bash
git pull --rebase
```

Pull from a specific branch:

```bash
git pull --rebase origin main
```

Force push safely:

```bash
git push --force-with-lease
```

---

# Remote Repositories

View configured remotes:

```bash
git remote -v
```

Add a remote:

```bash
git remote add origin https://github.com/username/repository.git
```

Change remote URL:

```bash
git remote set-url origin https://github.com/username/new-repo.git
```

---

# Interactive Rebase

Start interactive rebase:

```bash
git rebase -i <commit-hash>
```

Continue rebase:

```bash
git rebase --continue
```

Skip current commit:

```bash
git rebase --skip
```

Edit rebase todo:

```bash
git rebase --edit-todo
```

---

# Inspecting Commits

Show commit details:

```bash
git show <commit-hash>
```

Show a file from a commit:

```bash
git show <commit-hash>:path/to/file
```

---

# Restoring Changes

Unstage a file:

```bash
git restore --staged README.md
```

or

```bash
git reset HEAD file.txt
```

Discard changes:

```bash
git restore README.md
```

Discard all changes:

```bash
git restore .
```

---

# Cloning

Clone a repository:

```bash
git clone <repository-url>
```

---

# Viewing Differences

Unstaged changes:

```bash
git diff
```

Staged changes:

```bash
git diff --staged
git diff --cached
```

Compare commits:

```bash
git diff commit1 commit2
```

Compare branches:

```bash
git diff main feature
```

Compare a file:

```bash
git diff README.md
```

Compare current commit with previous:

```bash
git diff HEAD~1 HEAD
```

---

# Reset

Soft reset:

```bash
git reset --soft HEAD~1
```

Mixed reset:

```bash
git reset HEAD~1
```

Hard reset:

```bash
git reset --hard HEAD~1
```

> **Warning:** `git reset --hard` permanently deletes uncommitted work.

---

# .gitignore

Ignore all files with an extension:

```text
*.ext
```

Ignore a directory:

```text
abc/
```

Exception:

```text
!important.ext
```

Global `.gitignore`:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

Example:

```bash
echo "passwords.txt" >> .gitignore
```

---

# Removing Files

Remove from Git and disk:

```bash
git rm file.txt
git commit -m "Remove file.txt"
```

Stop tracking but keep file:

```bash
git rm --cached file.txt
git commit -m "Stop tracking file.txt"
```

---

# Moving / Renaming Files

Rename using Git:

```bash
git mv oldname.txt newname.txt
git commit -m "Rename oldname.txt to newname.txt"
```

Equivalent:

```bash
mv oldname.txt newname.txt
git rm oldname.txt
git add newname.txt
```

---

# Branches

Current branch:

```bash
git branch
```

All branches:

```bash
git branch -a
```

Remote branches:

```bash
git branch -r
```

Create a branch:

```bash
git branch feature-navbar
```

Switch branches:

```bash
git checkout feature-navbar
```

or

```bash
git switch feature-navbar
```

Create and switch:

```bash
git checkout -b feature-navbar
```

or

```bash
git switch -c feature-navbar
```

Rename current branch:

```bash
git branch -m new-name
```

Rename another branch:

```bash
git branch -m old-name new-name
```

Delete merged branch:

```bash
git branch -d feature-navbar
```

Force delete:

```bash
git branch -D feature-navbar
```

Delete remote branch:

```bash
git push origin --delete branch-name
```

Merged branches:

```bash
git branch --merged
```

Unmerged branches:

```bash
git branch --no-merged
```

---

# Merging

Fast-forward merge:

```bash
git checkout main
git merge feature-navbar
```

Three-way merge:

```bash
git checkout main
git merge feature-login
```

---

# Merge Conflicts

Keep current branch version:

```bash
git checkout --ours index.html
```

Keep incoming branch version:

```bash
git checkout --theirs index.html
```

Launch merge tool:

```bash
git mergetool
```

---

# Branching Workflows

## Feature Branch

```bash
git checkout -b feature-shopping-cart

# Work...

git checkout main
git merge feature-shopping-cart
git branch -d feature-shopping-cart
```

## Hotfix

```bash
git checkout main
git checkout -b hotfix-security

# Fix issue...

git commit -m "Fix security vulnerability"

git checkout main
git merge hotfix-security

git checkout develop
git merge hotfix-security
```

---

# Visualizing History

Branch graph:

```bash
git log --graph --oneline --all
```

Commits in feature branch not in main:

```bash
git log main..feature-branch
```

---

# Fetch

Fetch changes:

```bash
git fetch
```

Fetch all remotes:

```bash
git fetch --all
```

---

# Git Stash

Save stash:

```bash
git stash
```

Save with message:

```bash
git stash save "work in progress on feature X"
```

Include untracked files:

```bash
git stash -u
```

List stashes:

```bash
git stash list
```

Apply latest stash:

```bash
git stash apply
```

Apply specific stash:

```bash
git stash apply stash@{2}
```

Apply and remove:

```bash
git stash pop
```

Drop latest stash:

```bash
git stash drop
```

Drop specific stash:

```bash
git stash drop stash@{1}
```

Clear all stashes:

```bash
git stash clear
```

Show stash summary:

```bash
git stash show
```

Detailed stash diff:

```bash
git stash show -p
```

Specific stash diff:

```bash
git stash show -p stash@{1}
```

Create a branch from stash:

```bash
git stash branch new-feature-branch
```

Interactive stash:

```bash
git stash -p
```

---

# Common Stash Workflows

Switch branches safely:

```bash
git stash
git checkout main

# Fix bug...

git checkout feature-branch
git stash pop
```

Pull without committing:

```bash
git stash
git pull
git stash pop
```

---

## Notes

- `ours` = Current branch
- `theirs` = Incoming branch
- `git pull --rebase` keeps history linear.
- `git push --force-with-lease` is safer than `--force`.
- `git reset --hard` permanently deletes uncommitted work.
- Use `.gitignore` to avoid tracking generated files, virtual environments, secrets, and temporary files.
