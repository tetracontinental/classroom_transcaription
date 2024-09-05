@echo off

REM 仮想環境の作成とアクティベート
python -m venv dev
call .\dev\Scripts\activate.bat

REM 必要なパッケージのインストール
pip install -r requirements.txt

REM 完了メッセージの表示
echo 初期化が完了しました。