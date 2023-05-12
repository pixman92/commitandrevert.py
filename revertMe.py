#!/usr/bin/env python3

import os
import sys

# Get the path to the Git repository from the command-line arguments
if len(sys.argv) < 2:
    print("ERROR: Usage: \"python3 script_name.py\" \"<path_to_git_repo>\"")
    sys.exit(1)
else:
    repo_path = sys.argv[1]

# Make sure sys.args are NOT Less that 3
if len(sys.argv) < 3:
    print("ERROR: Second arg requiered - Repo Name")
    sys.exit(1)
# else:
    

# Check if repo_path is a valid Git repository
try:
    # os.chdir(repo_path)
    os.system("git status")
except:
    print(f"{repo_path} is not a valid Git repository")
    sys.exit(1)

# Print the last 10 commits and their timestamps
print("\nLast 10 commits:\n==========")
os.system("git log --pretty=format:'%h - %s (%ad)' --date=local --max-count=10")


# Add all changes to the Git repository
os.system("git add .")

# Prompt the user to enter a commit message
commit_message = input("Enter a commit message: ")

# Commit the changes to the Git repository
os.system("git commit -m '{}'".format(commit_message))

# Push the changes to the remote Git repository
remote_name = sys.argv[2]
os.system("git push {} master".format(remote_name))


# Prompt the user to revert to a previous commit
revert_choice = input("Do you want to revert to a previous commit? (y/n): ")

if revert_choice.lower() == "y":
    # Prompt the user to enter the number of commits to revert
    num_commits = int(input("Enter the number of commits to revert: "))
    
    # Revert to the previous commit(s)
    os.system("git revert HEAD~{}..HEAD".format(num_commits))

