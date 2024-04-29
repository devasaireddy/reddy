Cloning into 'new-one'...
remote: Enumerating objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
PS C:\Users\DELL\Documents\git f> cd new-one
PS C:\Users\DELL\Documents\git f\new-one> git add .
PS C:\Users\DELL\Documents\git f\new-one> git commit -m "added new line"
[main 0f30245] added new line
PS C:\Users\DELL\Documents\git f\new-one> git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 277 bytes | 277.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/URK23CS7053-Eswar/new-one.git
   e5a3c21..0f30245  main -> main
PS C:\Users\DELL\Documents\git f\new-one> git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
From https://github.com/URK23CS7053-Eswar/new-one
Updating 0f30245..1df43ba
Fast-forward
 1 file changed, 2 insertions(+), 1 deletion(-)
PS C:\Users\DELL\Documents\git f\new-one> git checkout -b new-branch
Switched to a new branch 'new-branch'
PS C:\Users\DELL\Documents\git f\new-one> git add .
PS C:\Users\DELL\Documents\git f\new-one> git commit -m "sdf"
[new-branch 6a22e7a] sdf
 1 file changed, 1 insertion(+)
PS C:\Users\DELL\Documents\git f\new-one> git push origin new-branch
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote:      https://github.com/URK23CS7053-Eswar/new-one/pull/new/new-branch
remote:
To https://github.com/URK23CS7053-Eswar/new-one.git
 * [new branch]      new-branch -> new-branch
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\DELL\Documents\git f\new-one> git merge new-branch
 README.md | 1 +
 1 file changed, 1 insertion(+)
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/URK23CS7053-Eswar/new-one.git
   1df43ba..6a22e7a  main -> main
PS C:\Users\DELL\Documents\git f\new-one> git add .
PS C:\Users\DELL\Documents\git f\new-one> git commit -m "Fix #1: iuytfd"
[main 12867d1] Fix #1: iuytfd
 1 file changed, 1 insertion(+)
PS C:\Users\DELL\Documents\git f\new-one> git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 289 bytes | 289.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/URK23CS7053-Eswar/new-one.git
   6a22e7a..12867d1  main -> main
PS C:\Users\DELL\Documents\git f\new-one>
