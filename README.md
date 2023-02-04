# poetry-template


## 概要
自分用のpoetryプロジェクトのテンプレート。


## つかいかた
cloneしてよしなに。

以下のようなシェルスクリプトを作ってPathを通しておくと、`poetry-template.ps [project-name]` で「templateのclone」・「フォルダのrename」・「vscodeで開く」までできて楽。
```ps1
# poetry-template.ps1
Param ([string]$projectName)

git clone https://github.com/torippy1024/poetry-template
Rename-Item poetry-template $projectName
code $projectName
```

## 機能
* vscodeでファイル保存時、自動フォーマット (black)
* `task run`: src/main.py を実行
* `task lint`: flake8 で lint
* `task build`: pyinstaller で exe化
* `task build-one`: pyinstaller で exe化 (＋ 1つのファイルにまとめる) 
* `task test`: pytest 実行

