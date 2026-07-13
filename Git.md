<<<<<<< HEAD

```bash
=======
>>>>>>> 3f600445be012e5064ddb4e8be0a76a164b18195
echo "# ai-learning" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ahatha676/ai-learning.git
git push -u origin main
<<<<<<< HEAD
```
=======

>>>>>>> 3f600445be012e5064ddb4e8be0a76a164b18195


### …or push an existing repository from the command line

git remote add origin https://github.com/ahatha676/ai-learning.git
git branch -M main
git push -u origin main



- comimit不是备份，是**一个有意义的快照**。每次 commit 都应该是一个完整的逻辑单元，一个推送

 git status              # 看改了啥（最常用的命令，没有之一）
 git add -A              # 把所有改动加入暂存区
 git commit -m "feat: ..."  # 提交

 git diff               # 看具体改了什么行，防止误提交


`git diff` 的默认行为是：**比较工作目录（working tree）与暂存区（staging area）之间的差异**。

- 当你修改了文件但还没执行 `git add` 时，`git diff` 会显示这些改动。
    
- 当你执行 `git add` 将改动加入暂存区后，工作区和暂存区就变得一致了，此时 `git diff` 就没有输出了。
    

你之前执行了：

bash

git add -A

这会把所有改动（包括 `Git.md`）都放到了暂存区。所以此时工作区和暂存区完全相同，`git diff` 自然为空。