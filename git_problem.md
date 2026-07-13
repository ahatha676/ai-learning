``` bash
(base) PS E:\obsidian\ai\学习内容> git init
Reinitialized existing Git repository in E:/obsidian/ai/学习内容/.git/
(base) PS E:\obsidian\ai\学习内容> echo "# ai-learning" >> README.md
(base) PS E:\obsidian\ai\学习内容> git commit -m "first commit"
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
(base) PS E:\obsidian\ai\学习内容> git add README.md
(base) PS E:\obsidian\ai\学习内容> git commit -m "first commit"
[main f331d80] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
(base) PS E:\obsidian\ai\学习内容> git branch -M main
(base) PS E:\obsidian\ai\学习内容> git remote add origin https://github.com/ahatha676/ai-learning.git
error: remote origin already exists.
(base) PS E:\obsidian\ai\学习内容> git push -u origin main
To https://github.com/ahatha676/ai-learning.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/ahatha676/ai-learning.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(base) PS E:\obsidian\ai\学习内容> git pull origin main --allow-unrelated-histories
From https://github.com/ahatha676/ai-learning
 * branch            main       -> FETCH_HEAD
Auto-merging Git.md
CONFLICT (add/add): Merge conflict in Git.md
warning: Cannot merge binary files: README.md (HEAD vs. 3f600445be012e5064ddb4e8be0a76a164b18195)
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
(base) PS E:\obsidian\ai\学习内容> git push -u origin main
To https://github.com/ahatha676/ai-learning.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/ahatha676/ai-learning.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(base) PS E:\obsidian\ai\学习内容> git pull origin main --allow-unrelated-histories
error: Pulling is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
```