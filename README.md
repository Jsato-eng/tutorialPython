# tutorialPython

- .gitignoreを更新しても反映されないときは「git rm -r --cached .」でキャッシュを削除
```
git rm -r --cached .
git add .
git commit -m 'modify .gitignore'
git push origin main
```