> ### tesbot
> このbotは１サーバーを想定して作ってます。あと、サーバーidなどは、セキュリティ関係のため全部削除しておきましたなので、main.pyから、自分のサーバーidを入れ直して下さい。


# セットアップ

## インストールするために必要なもの

* タスクマネージャーで実行してください ```pip3 install -r requirements.txt```

* 推奨のpythonのバージョンは `3.9` 以上です。
---
## ステップ 1: discord botの作り方

1. https://discord.com/developers/applications にアクセスします
2. アプリケーションでDiscordボットを作成する
3. ボット設定からトークンをコピー

   ![image](https://user-images.githubusercontent.com/89479282/205949161-4b508c6d-19a7-49b6-b8ed-7525ddbef430.png)
4. `コピーしたトークンを.env`の `DISCORD_BOT_TOKEN`にペースト

   <img height="190" width="390" alt="image" src="https://user-images.githubusercontent.com/89479282/222661803-a7537ca7-88ae-4e66-9bec-384f3e83e6bd.png">

5. discord デベロッパーパネル内の MESSAGE CONTENT INTENT `をonにして下さい`

   ![image](https://user-images.githubusercontent.com/89479282/205949323-4354bd7d-9bb9-4f4b-a87e-deb9933a89b5.png)

6. discord デベロッパーパネル内の OAuth2 URL Generatorでurlを作成その際Application Commandとbotにチェックを入れておいて下さい

   ![image](https://user-images.githubusercontent.com/89479282/205949600-0c7ddb40-7e82-47a0-b59a-b089f929d177.png)
---
## 後は、main.pyのチャンネルidサーバーidを綺麗に変更したら完成
`python3 main.py` か`python main.py` のどちらかを押して起動
※補足　このbotは、サーバー人数を計測したり、メッセージを一括削除などの無駄な機能を兼ね備えています。

## 最後に
### きれいに書いても誰も見てくれないので適当に書いてます。なので、このbotについてもっと知りたい方や苦情を言いたい方は、私の自己紹介欄にあるdiscordサーバーに入って下さい。
