# Chapter 1 — Getting Started

## 1. Overview

Chapter 1 focuses on setting up the Python development environment and establishing the development and version-control workflow used throughout this learning project.

The chapter covers:

- Python environment verification
- Python virtual environments
- Terminal navigation
- Project structure
- Git initialization
- Branches
- Git status
- Staging
- Commits
- Git configuration
- GitHub integration
- SSH authentication
- Remote repositories
- Upstream branches
- Basic Git workflow

This chapter is primarily a setup and workflow chapter. The substantive Python programming concepts begin in Chapter 2.

---

## 2. Commands Used

The following table documents the commands used during the setup, including their purpose and examples.

| Command | Description | Example |
|---|---|---|
| `cd <directory>` | Changes the current working directory. | `cd Basics` |
| `cd ..` | Moves to the parent directory. | `cd ..` |
| `ls -la` | Lists files and directories, including hidden files, in detailed format. | `ls -la` |
| `touch <file>` | Creates an empty file if it does not already exist. | `touch README.md` |
| `mkdir -p <directory>` | Creates a directory and any required parent directories. | `mkdir -p chapters/01` |
| `cat <file>` | Displays the contents of a file in the terminal. | `cat ~/.ssh/id_ed25519.pub` |
| `which <command>` | Displays the path of the executable used by the shell. | `which python` |
| `python --version` | Displays the active Python version. | `python --version` |
| `python -c "<code>"` | Executes Python code directly from the command line. | `python -c "import sys; print(sys.executable)"` |
| `git init` | Initializes a Git repository in the current directory. | `git init` |
| `git branch` | Lists local branches. | `git branch` |
| `git branch -m <name>` | Renames the current branch. | `git branch -m main` |
| `git status` | Displays the current state of the working tree and staging area. | `git status` |
| `git add <file>` | Stages a specific file. | `git add README.md` |
| `git add <file1> <file2>` | Stages multiple specific files. | `git add README.md .gitignore` |
| `git add .` | Stages changes in the current directory and its descendants. | `git add .` |
| `git commit -m "<message>"` | Creates a commit from staged changes. | `git commit -m "docs: add chapter 1"` |
| `git log --oneline` | Displays commit history in compact format. | `git log --oneline` |
| `git remote add <name> <url>` | Adds a remote repository. | `git remote add origin <URL>` |
| `git remote -v` | Displays configured remote repositories and their URLs. | `git remote -v` |
| `git remote set-url <name> <url>` | Changes the URL of an existing remote. | `git remote set-url origin git@github.com:pRamosDevs/python-learning.git` |
| `git push` | Pushes local commits to the configured upstream branch. | `git push` |
| `git push -u <remote> <branch>` | Pushes a branch and establishes its upstream branch. | `git push -u origin main` |
| `git branch -vv` | Displays local branches and their upstream tracking information. | `git branch -vv` |
| `git config --global user.name "<name>"` | Configures the Git author name globally. | `git config --global user.name "Pedro Ramos"` |
| `git config --global user.email "<email>"` | Configures the Git author email globally. | `git config --global user.email "email@example.com"` |
| `ssh-keygen` | Generates an SSH key pair. | `ssh-keygen -t ed25519 -C "email@example.com"` |
| `ssh -T git@github.com` | Tests SSH authentication with GitHub. | `ssh -T git@github.com` |

---

## 3. Project Location

The project was created inside the Python learning workspace.

The repository root is:

```text
Basics/