what is git stash?
git stash is a command in Git that temporarily saves changes you’ve made in your working directory and staging area without committing them to the repository.
git stash
git stash apply
git stash pop
what is git index?
In Git, the index (also known as the staging area or cache) is an intermediate area where changes to files are gathered before they are committed to the repository. It acts as a buffer between your working directory (the files you’re actively working on) and your Git repository (where commits are stored).
what is git reset?
git reset is a powerful Git command used to undo changes in your Git repository. It can be used to modify the state of the working directory, the staging area (index), and the commit history.
what is head in git commit?
In Git, HEAD is a reference to the current commit or current branch in your repository. It essentially points to the latest commit on the current branch you're working on. You can think of HEAD as a pointer that tells you where you are in your repository's history.
git fetch vs git pull?
git fetch fetches commits from remote repository into your working directory, its like download those files but wont merge those changes in your working directory.
git pull fetch the changes and merge those changes into your working directory so basically git pull if git fetch + git merge.

what is git cherry-pick?
when you want to apply specific commit, or range of commits of one branch on other branch. when you dont want to merge entire branch but want to merge only one specific commit.
what is git hooks?
Git hooks are scripts that Git executes at various points during its execution lifecycle, such as before or after a commit, push, or merge. These hooks allow you to automate certain actions or enforce policies in your Git workflow.

what is git reset?
git reset will remove the commits from commit history,
let us assume there are 3 commits aa(head, the most recent commit) bb cc
if you want to reset latest commit to bb then you will use
git reset bb this will remove commit aa and head is moved to bb 
git reset has 3 modes mixed soft hard
soft will bring changes in commit aa to staging area
hard will remove all changes completely
mixed is default mode and will bring changes to working area

git reset will take commit you want to reset, all commits which are above that will be removed

what is git revert?
git revert will work on remote repository
this wont delete the commit, but will remove changes and create new commit on top of that 
git revert will take commit and will revert that commit by creating new commit on top of that
