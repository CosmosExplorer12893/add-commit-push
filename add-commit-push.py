# Ian King
# October 24, 2025

# This program will allow the user to add, commit, and push changes to 
# a repository automatically by running this application. 

import subprocess
import sys

# Implement Variables
Message = "Update files."
force_mode = False

# Analyze Command Line Arguments 
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-m":
        if i + 1 < len(sys.argv):
            Message = sys.argv[i + 1]
            i += 1
        else:
            print("Error: No commit message provided after -m")
            sys.exit(1)
    elif arg == "-f":
        force_mode = True
    i += 1

# Check if the user has a parameter of m for message
if len (sys.argv) > 1 and sys.argv[1] == "-m":
    if len (sys.argv) > 2:
        Message = sys.argv[2]
    else:
        print("Error: No commit message provided after -m")
        sys.exit(1)

#Print and process git status
print("Starting Add-Commit-Push")
print("git status")
subprocess.run(["git", "status"])

#Confirm if the user would like to continue with the program or not
if not force_mode:
    confirm = input("Do you want to continue (y/n): ")
    if confirm.lower() != "y":
        print("Exiting...")
        sys.exit()
else: 
    print("Force mode enabled - skipping confirmation")

print("Continuing with add commit push...")

#Print and process the results of adding, committing, and pushing 
print("git add -A")
subprocess.run(["git", "add", "-A"])

print("git commit -m \"" + Message +"\"" )
subprocess.run(["git", "commit", "-m", Message])

print("git push")
subprocess.run(["git", "push"])

# End of Program
