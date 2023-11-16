# RogueSave
This is a meat Rouge game saver made in Python.  
这是一个Python做的肉鸽游戏保存器。  
これはPythonで作られたルージュ型即時ゲーム保存ソフトです。  

## Question/需求/機能
There exists a type of game in the world, similar to Super Mario and the Devil's Castle from Galaxy Warrior, where there are no save files, and each round is a fresh start. Despite this, every unexpected failure is still disheartening. To address this, I have created a script to tackle the issue.  

世界上存在这么一种游戏，类似于超级马里奥和银河战士恶魔城，但这种游戏不存在存档，每局都是一个新的开始。但即使如此，每次意外失败还是令人很心疼，在此我做了个这个脚本解决这个问题。  

世の中には、マリオや銀河の戦士デビルズキャッスルのようなセーブ機能のないゲームが存在します。各プレイは新しい始まりです。しかし、それでも毎回の意外な失敗は痛ましいものです。そのため、この問題を解決するスクリプトを作成しました。

## Function/功能/機能
You can use this script to save the game progress to another path at regular intervals (every five minutes), allowing you to reload the previous instant save when your game fails.  
您可以用此脚本在一定时间内（每五分钟一次）把游戏存档保存到另一个路径里面，从而在您游戏失败时重新载入把上一次即时存档。  
このスクリプトを使用して、一定の時間ごと（5分ごと）にゲームのセーブデータを別のパスに保存し、ゲームが失敗した場合に前回の即時セーブデータをリロードできます。
  
## Buttons/按钮/ボタン
![image](https://github.com/HAYATE0578/RogueSave/assets/78299959/850cb8d5-2800-44a1-9b06-94ae5891667d)


### US/CN/JP
Change the operating language of this script.  
更改此脚本的操作语言。  
このスクリプトの操作言語を変更してください。  
<hr>

### SAVE_PATH/TEMP_PATH
Click on this text to open the folder at the specified path. The first one is the default save path for the game, and the latter is the temporary path that the user needs to specify.  
点击此文本，可以打开此路径文件夹。前者是游戏的默认保存路径，后者是用户要指定的暂用路径。  
このテキストをクリックして、指定されたパスのフォルダを開きます。前者はゲームのデフォルトの保存パスであり、後者はユーザーが指定する必要がある一時的なパスです。  
<hr>

### Set path1/Set path2
Save the document path and temporary target path separately.  
分别用于保存文档路径和暂定目标路径。  
文書の保存パスと一時的なターゲットパスを別々に保存します。  
<hr>

### Load Archive
Override the original path with the latest save in your specified document save path.  
用于将你暂定的文档保存路径中，选择最新的存档覆盖回原来的路径。  
指定された文書保存パスで最新の保存を使用して元のパスを上書きします。  
<hr>

### Start Saving
Copy your save files instantly (every 5 minutes) and back them up to the specified path. Keep a maximum of 50 backup files.  
用于即时（间隔5分钟）把你的存档拷贝一份，备份到暂定路径中。备份存档最多保存50份。  
存档を即座に（5分ごとに）コピーし、それを指定されたパスにバックアップします。最大50個のバックアップファイルを保持します。  

