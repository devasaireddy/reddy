1. What is the difference between git and GitHub?
Git is a distributed version control system (DVCS) used for tracking changes in source code
during software development. It allows multiple developers to collaborate on a project by
managing a history of changes to files and coordinating work among team members.
GitHub, on the other hand, is a web-based platform built around Git. It provides hosting for
Git repositories along with additional features such as issue tracking, project management
tools, and collaboration features like pull requests and code reviews. GitHub also offers
social networking features like following other users, starring repositories, and forking
projects.
2. What is git’s feature?
Git features version control, branching and merging, distributed development, collaboration
tools like pull requests, and cryptographic integrity checks.
3. What are the advantages of using git?
Git provides version control, enables collaboration, supports branching and merging, ensures
code integrity, and is highly flexible and widely supported.
4. What are git’s limitation?
Learning Curve
Large File Handling
Merge Conflicts
Lack of GUI for Some Operations
Risk of Data Loss
5. List few git command.
a) git init: Initializes a new Git repository.
b) git add <file>: Adds a file to the staging area.
c) git commit -m "message": Commits staged changes to the repository with a message.
d) git status: Shows the status of the working directory and staging area.
e) git push: Pushes local commits to a remote repository.
f) git pull: Fetches changes from a remote repository and merges them into the local
branch.
g) git branch: Lists existing branches or creates a new one.
h) git checkout <branch>: Switches to a different branch.
i) git merge <branch>: Merges changes from a specified branch into the current branch.
j) git clone <repository URL>: Clones a repository from a remote location to the local
machine.
6. What does git config do?
git config is a command used to set or get configuration options for Git. It can be used to
configure settings such as user name, email, editor, and many others.
For example:
git config --global user.name "Your Name" sets the global user name.
git config --global user.email "your_email@example.com" sets the global email.
git config --list lists all the configurations.
7. What does the git status command do?
git status command displays the current state of the working directory and staging area. It
shows which files have been modified, which files are staged for the next commit, and which
files are untracked.
8. What does the git log command do?
git log command displays a list of commits in the repository. It shows information such as
commit hash, author, date, and commit message for each commit. This command allows you
to review the history of changes in the repository.
9. What is git add?
git add is a command used to add changes in the working directory to the staging area in Git.
When you make changes to files in your project, Git initially doesn't track those changes. By
using git add, you specify which changes you want to include in the next commit.
For example, if you've modified or added new files to your project, you would use git add to
stage those changes before committing them. This prepares the changes to be included in the
next commit.
10. What is the difference between git pull and git fetch?
git fetch: Fetches changes from the remote repository to your local repository, but it doesn't
automatically merge them into your current branch. It updates your remote tracking branches
(like origin/master) to reflect the state of the remote repository. You can then review the
changes using git diff or other commands before merging them manually.
git pull: Fetches changes from the remote repository, just like git fetch, but it also
automatically merges them into your current branch. It's essentially a combination of git fetch
followed by git merge.
11. What are branches, and what command creates a new branch?
Branches in Git are parallel lines of development that diverge from the main line (usually
called the "master" or "main" branch) to work on different features, fixes, or experiments
independently. They allow developers to isolate their work from the main codebase until it's
ready to be merged.
The command git branch <branch_name> creates a new branch in Git.
12. What is git merge?
git merge is a command used to integrate changes from one branch into another branch.
When you merge one branch (called the source branch) into another branch (called the
destination branch), Git combines the changes made in the source branch with the changes in
the destination branch.
13. When should you use git push and git pull?
You should use git push when you want to send your local commits to a remote repository,
typically after making changes and committing them locally. This action updates the remote
repository with your changes.
On the other hand, you should use git pull when you want to retrieve changes from a remote
repository and integrate them into your local repository. This is typically done to update your
local repository with changes made by others in the remote repository.
14. Is Github an Open-Source Software?
GitHub itself is not open-source software, but it hosts millions of open-source projects. The
platform provides proprietary services for managing Git repositories, issue tracking, project
management, and collaboration tools. However, many of the projects hosted on GitHub are
open source, meaning their source code is freely available for anyone to view, modify, and
distribute according to the terms of an open-source license.
15. How Does Github Help In Collaborating With Other Developers?
GitHub greatly facilitates collaboration among developers through its robust set of features.
With pull requests, developers can propose changes, solicit feedback, and discuss
modifications before merging them into the main codebase. Issue tracking allows for efficient
bug reporting and feature requests, while branching and merging capabilities enable parallel
development without conflicts. Code review tools ensure code quality and consistency, while
team management features provide controlled access to repositories. Additionally, GitHub
integrates with various third-party tools, streamlining the development workflow and
enhancing collaboration efficiency. Overall, GitHub serves as a central platform for developers
to collaborate, share code, track issues, and manage projects effectively.
16. What Is Repo?
"Repo" is short for "repository." In the context of Git and GitHub, a repository is a storage
space where your project's files and revision history are stored. It contains all the files for
your project, along with a history of each file's changes. Repositories can be either local
(stored on your computer) or remote (stored on a server, like GitHub).
17. What is GitHub fork?
Forking on GitHub refers to creating a personal copy of someone else's repository. When you
fork a repository, GitHub creates a copy of the original repository in your GitHub account.
You can then freely experiment with changes in your fork without affecting the original
project. Forking is commonly used to propose changes to someone else's project (via pull
requests), to experiment with changes, or to create your own version of an existing project.
18. Can we change our GitHub username?
Yes, you can change your GitHub username.
19. Is it possible in git to merge a branch into the master?
yes, it is possible in Git to merge a branch into the master branch.
20. What language is used in git?
Git itself is primarily written in the C programming language. However, Git also includes
scripts and tools written in various languages, including shell scripting (Bash), Perl, Tcl, and
Python. These scripts and tools contribute to Git's functionality and support its operation
across different platforms and environments.
21. What is the significance of Git version control?
Git version control allows tracking changes, enabling collaboration, managing code history,
facilitating branching and merging, ensuring code integrity, and streamlining deployment.
22. List the Types of version control system.
Centralized Version Control Systems (CVCS): In CVCS, there is a central server that
stores the repository, and developers check out and commit changes directly to this
central repository. Examples include CVS (Concurrent Versions System) and SVN
(Subversion).
Distributed Version Control Systems (DVCS): In DVCS, each developer has their own
local copy of the repository, including the full history of the project. Developers can work
independently and synchronize their changes with remote repositories as needed. Git is
the most popular example of a DVCS.
23. Can we delete the github account.
Yes, you can delete a GitHub account.
24. Name any two git repository hosting services that are common.
Two common Git repository hosting services are Bitbucket and GitLab.
25. What is git clone?
git clone is a Git command used to create a copy of a repository from a remote source, such
as GitHub, Bitbucket, or GitLab, to your local machine. It copies all the files, commit history,
and branches from the remote repository to your local machine, allowing you to work on the
project locally and synchronize changes with the remote repository.
26. What is staging environment?
A staging environment is a pre-production environment that closely resembles the production
environment. It serves as an intermediate step between development and production
environments, allowing developers to test their code in a controlled environment before
deploying it to production.
27. What is github issues?
GitHub Issues is a feature provided by GitHub for tracking tasks, enhancements, bugs, or any
other topics related to a repository. It allows users to create, assign, and track issues within a
project. Each issue can have a title, description, labels, assignees, milestones, and comments.
28. Write the steps to create a github issue.
To create a GitHub issue, follow these steps:
1. Navigate to the Repository: Go to the repository where you want to create the
issue.
2. Click on the "Issues" Tab: In the repository's menu, click on the "Issues" tab.
3. Click on "New Issue": On the right side of the page, click on the green "New
issue" button.
4. Fill in Issue Details:
5. Title: Enter a descriptive title for the issue.
6. Description: Provide a detailed description of the issue, including any relevant
information or steps to reproduce.
7. Labels: Optionally, add labels to categorize the issue (e.g., bug, enhancement,
documentation).
8. Assignees: Optionally, assign the issue to one or more users responsible for
addressing it.
9. Milestone: Optionally, associate the issue with a project milestone.
10. Additional Options: You can add more details, such as attaching files, using
Markdown for formatting, or linking to related issues or pull requests.
11. Submit the Issue: Once you've filled in the necessary details, click on the green
"Submit new issue" button to create the issue.
29. What is a git submodules and git aliases?
Git submodules and Git aliases are two different features of Git:
Git Submodules: Git submodules allow you to include a separate Git repository as a
subdirectory within your own repository. This is useful when you want to include another
project as a dependency in your own project. Git submodules allow you to track the specific
version of the dependent repository that your project relies on, making it easier to manage
dependencies and collaborate with others.
Git Aliases: Git aliases are custom shortcuts or abbreviations for Git commands. They allow
you to create shorter, more memorable names for frequently used Git commands or command
sequences. For example, you could create an alias co for git checkout, ci for git commit, or st
for git status. Git aliases can be defined either globally (for all repositories on your system) or
locally (for a specific repository) in your Git configuration file. They help improve
productivity and streamline your workflow by reducing the need to type out long Git
commands repeatedly.
