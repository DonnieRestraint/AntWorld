# git checkout

- `git checkout next_branch` 切换分支

- `git checkout -b next_branch` 创建并切换分支

- git checkout 时出现error: your local changes .......

  ```
  有3种解决办法
  1` git reset --hard HEAD (如果你不介意失去那些微小变化)
  <<<<<<< HEAD
  2` git checkout -f (丢弃本地更改, )
  3` git checkout -- <file> # 拉取暂存区文件 并将其替换成工作区文件
  	git checkout . # 拉取暂存区所有文件 并将其替换成工作区文件
  4` git stash进行存储
      git stash save
      git checkout branch
      // do something
      git checkout old_branch
      git stash pop # 恢复最近的缓存到当前文件中，同时删除恢复的缓存条目。
      # git stash list  # 指令，查看本地当前的缓存列表
      # git stash apply stash@{id} # 恢复指定id的stash内容，同时不会删除恢复的缓存条目。
  5` git add . && git commit 
  
  ```
  

