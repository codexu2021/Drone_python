# Tello EDU 操作用python クラス
## 概要
- Python3 対応
- Tello EDU 向け
- 1 on 1 でインスタンス生成

## 前提
- Tello EDUが操作する PC と同じwi-fiに接続している

## メソッド
- set_ip() -> macaddrからipアドレスをサーチ
- fly_test() -> 命令できるかテスト
- inline_exec() -> インラインでコマンドを打つ

## バグ
- ドローン起動時に再度インスタンスを生成するとコマンドを受け付けない

## 改善予定
- テキストからコマンドを抽出可能に
