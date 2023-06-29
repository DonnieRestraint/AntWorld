# git commit

- `git commit -m ''` 提交到本地仓库

- 修改最后一次提交的日志 且未push

  ```
  git commit --amend
  ```

- 修改最后一次提交且已push到服务器

   ```
   git commit --amend
   git push origin master --force	# 同步修改的日志到服务器
   # 此操作会导致别人本地修改过的代码无法同步, 先协商好
   ```

  

- 修改多次提交 且未push

  ```
  git rebase -i HEAD~n  # n表示是最后几次提交
  此时它会打开编辑器, 显示n条出来
  pick 94fc8fe 添加内容a
  pick 04f0d18 添加内容c
  pick b1b451d 添加内容d
  将要修改的行的pick改为edit后保存
  执行git commit --amend
  完成编辑日志
  git rebase --continue
  执行git commit --amend
  完成编辑日志
  git rebase --continue
  修改了几行就得执行几次
  
  ebase目的是打开提交的历史记录，让您选择要修改的内容。 Git会让你在一个新的分支修改内容。 git rebase --continue则是让你重新回到之前的分支。
  
  ```

- 在IDEA中的日志操作

  [利用git工具修改日志信息](https://img2022.cnblogs.com/blog/2926369/202208/2926369-20220821020219985-1510191278.png)

  [利用git工具强制推送](https://img2022.cnblogs.com/blog/2926369/202208/2926369-20220821020232787-1136230920.png)

