# poetry-template


使い方や解説はQiitaに書きました。
https://qiita.com/torippy/items/9fb45c2eb8ba1d8fde64

以下Qiita記事の内容を一部抜粋。

# 概要
新しいプロジェクトを作るとき、毎回一から環境構築するのは面倒だし、ミスがあるかもしれないし、そんな反復作業をするより開発に時間を回したい！
ということで、Python用のパッケージ管理ツールの一つである「[Poetry](https://github.com/python-poetry/poetry)」を使ったPythonプロジェクトのテンプレートを作ってみた。
自分用ではあるけど、基本的な構成ではあるため他の人も使えるように公開している。

https://github.com/torippy1024/poetry-template

構成はざっと以下の通り。
* poetry (パッケージ管理ツール)
* flake8 (リンター)
* black (フォーマッター)
* pytest (テスト)
* taskipy (タスク定義)
* pyinstaller (実行ファイル化)
* .vscode/settings.jsonでファイル保存時自動フォーマット


# つかいかた

## clone
GitHubに公開してるので基本的にcloneしてあとは良しなに。
`projectName`は好きなプロジェクト名に置き換えてください。

```shell
git clone https://github.com/torippy1024/poetry-template.git projectName
cd projectName
poetry install
```

## ディレクトリ構成
ディレクトリ構成は以下の通り。

```shell
┣ .vscode/           # vscode用の設定記述
┣ src/               # ソースコードはここに置く
┃   ┗ main.py        # エントリーポイント
┣ tests/             # テストコードはここに置く
┃   ┗ test_main.py
┣ .flake8            # flake8の設定
┣ .gitignore
┣ README.md
┣ poetry.lock
┗ pyproject.toml
```

`src/main.py`の`if __name__ == "__main__":`にメイン処理を書く。
テンプレートは足し算のサンプル。
```python:src/main.py
def addition(num1: float, num2: float):
    return num1 + num2


if __name__ == "__main__":
    print("Please enter two numbers.")

    try:
        num1 = float(input("num1: "))
        num2 = float(input("num2: "))
    except ValueError:
        print("Invalid input. Please enter number.")
        exit()

    result = addition(num1, num2)
    print(f"{num1} + {num2} = {result}")
```

後述するが、`task run`で`src/main.py`を実行できる。
```shell
> task run
Please enter two numbers.
num1: 5
num2: 3
5.0 + 3.0 = 8.0
```

`tests`フォルダにはテストコードを書く。
```tests/test_main.py
from src.main import addition


def test_addition():
    result = addition(2, 3)
    assert result == 5
```

`task test`でpytestによるテストを実行できる。
```shell
> task test
====================== test session starts =======================
platform win32 -- Python 3.10.0, pytest-7.2.1, pluggy-1.0.0        
rootdir: C:\Users\toriy\Downloads\hogehogehoge
collected 1 item

tests\test_main.py .                                        [100%] 

======================= 1 passed in 0.02s ========================
```


## 機能
`poetry shell`で仮想環境に入ったあと、以下のコマンドが使える。
* `task run`: src/main.py を実行
* `task lint`: flake8 で lint
* `task build`: pyinstaller で exe化
* `task build-one`: pyinstaller で exe化 (＋ 1つのファイルにまとめる) 
* `task test`: pytest 実行

また、vscodeでファイル保存時、自動フォーマットが動いてくれる。
