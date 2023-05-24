# python3 ~/Documents/Programming/RevertPY/revertMe.py


# python3 ~/Documents/Programming/RevertPY/zipTesting.py --path  --directory ~/Documents/Programming/RevertPractice/GitTesting2023/ ~/Documents/Programming/RevertPractice/GitTesting2023/ --output-folder ~/Documents/Programming/RevertPractice/savedZips --zip-name savedMay2023
# ======================

# In the Git helper script, the following flags (command-line options) are available:

# --path: Specifies the path to the local Git repository.
# --message: Provides the commit message to use when committing changes to the repository.
# --list-commits: Lists the last 10 commits in the repository.
# --compare-commit: Allows comparing a specific commit with the current commit. The value should be a number corresponding to the index of the commit in the list of past commits.
# --show-changes: Shows the changes that will occur from a revert to a specific commit. The value should be a number corresponding to the index of the commit in the list of past commits.
# --revert: Reverts the repository to a specific commit. The value should be a number corresponding to the index of the commit in the list of past commits.

# --directory: path to pull for zipping process
# --output-folder: place for the zipped file to be stored, if not made, it will be created
# --zip-name: name of the zip file to be saved


# ======================

# python my_zip_app.py --directory /path/to/directory --zip myfiles


import subprocess
import argparse
import argparse
import os
import zipfile

def zip_directory(directory, output_folder, zip_name):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    zip_file_name = os.path.join(output_folder, zip_name + '.zip')

    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))

def is_git_repo(repo_path):
    try:
        subprocess.check_output(["git", "rev-parse"], cwd=repo_path)
        return True
    except subprocess.CalledProcessError:
        return False

def list_commits(repo_path):
    commit_output = subprocess.check_output(["git", "log", "--pretty=format:%h %ad %s", "--date=short", "-n", "10"], cwd=repo_path).decode().strip().split("\n")

    # Enumerate and print the numbered list of commits
    print("Past Commits:")
    for index, commit in enumerate(commit_output, start=1):
        print(f"{index}. {commit}")

def compare_commit(repo_path, commit_index):
    commit_id = subprocess.check_output(["git", "rev-list", "--max-count=1", "--skip=" + str(commit_index - 1), "HEAD"], cwd=repo_path).decode().strip()
    subprocess.check_call(["git", "diff", commit_id], cwd=repo_path)

def show_changes(repo_path, commit_index):
    commit_id = subprocess.check_output(["git", "rev-list", "--max-count=1", "--skip=" + str(commit_index - 1), "HEAD"], cwd=repo_path).decode().strip()
    subprocess.check_call(["git", "show", commit_id], cwd=repo_path)

def revert_commit(repo_path, commit_index):
    try:
        commit_id = subprocess.check_output(["git", "rev-list", "--max-count=1", "--skip=" + str(commit_index - 1), "HEAD"], cwd=repo_path).decode().strip()

        subprocess.check_call(["git", "revert", commit_id], cwd=repo_path)

        # subprocess.check_call(["git", "push", "origin", "main"])   

    except Exception as e:
        print ("====\nError occured!", "\n\nPossible conflicts found in code\nPossible need to test with other Revert #.")

def push_command():
    subprocess.check_call(['git', 'add', '.'])
    # subprocess.check_call(['git', 'push'])
    subprocess.check_call(["git", "push", "origin", "main"])        
# ======================
def main():
    parser = argparse.ArgumentParser(description="Git Helper Script")
    parser.add_argument("--path", help="Path to the local Git repository")
    parser.add_argument("--message", help="Commit message")
    parser.add_argument("--list-commits", action="store_true", help="List the last 10 commits")
    parser.add_argument("--compare-commit", type=int, choices=range(1, 11), help="Compare a specific commit with the current commit")
    parser.add_argument("--show-changes", type=int, choices=range(1, 11), help="Show the changes that will occur from a revert to a specific commit")
    parser.add_argument("--revert", type=int, choices=range(1, 11), help="Revert the repository to a specific commit")
    parser.add_argument("--push", action="store_true", help="Adds modified files, and pushes them.")

    parser.add_argument('--directory', help='Path to the directory to be zipped')
    parser.add_argument('--output-folder', help='Path to the folder to save the zip file')
    parser.add_argument('--zip-name', help='Name of the zip file')


    args = parser.parse_args()

    # if args.path:
    #     if not is_git_repo(args.path):
    #         print("Error: The specified path is not a valid Git repository.")
    #         return
    # else:
    #     print("Error: Please provide the path to the local Git repository using the --path flag.")
    #     return

    if args.message:
        subprocess.check_call(["git", "add", "."], cwd=args.path)
        subprocess.check_call(["git", "commit", "-m", args.message], cwd=args.path)
        subprocess.check_call(["git", "push"], cwd=args.path)

    if args.list_commits:
        list_commits(args.path)

    if args.compare_commit:
        compare_commit(args.path, args.compare_commit)

    if args.show_changes:
        show_changes(args.path, args.show_changes)

    if args.revert:
        revert_commit(args.path, args.revert)

    if args.push:
        push_command()

    # ======================
    if args.directory and args.output_folder and args.zip_name:
        zip_directory(args.directory, args.output_folder, args.zip_name)
        print(f'Successfully zipped files in {args.directory} to {args.output_folder}/{args.zip_name}.zip')
    else:
        print('Please provide the --directory, --output-folder, and --zip-name flags.')

if __name__ == "__main__":
    main()