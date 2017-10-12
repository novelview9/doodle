# 깃허브 파일 트래킹
#git

--assume-unchanged assumes that a developer shouldn’t change a file. This flag is meant for improving performance for not-changing folders like SDKs.
--skip-worktree is useful when you instruct git not to touch a specific file ever because developers should change it. For example, if the main repository upstream hosts some production-ready configuration files and you don’t want to accidentally commit changes to those files, --skip-worktree is exactly what you want.

https://stackoverflow.com/questions/13630849/git-difference-between-assume-unchanged-and-skip-worktree

--assume-unchanged



깃 파일 볼때
Git ls-files {path}


Git ls-files -v
status tag 보기

