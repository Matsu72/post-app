#「Python 3.11の軽量版」イメージをベースに使う
FROM python:3.11-slim

#作業ディレクトリを /code に設定
WORKDIR /code

#ローカル（ホスト）の requirements.txt を、Docker内のカレントディレクトリにコピー
COPY requirements.txt .

#requirements.txt を使って、必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー（初回は空）
COPY . .