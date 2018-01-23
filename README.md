# tgshellbot
Telegram shell bot
==================

Simple Telegram bot for remote shell on python. Works both on Windows and Linux (Mac not tested).

#### Dependencies
* Telepot 
* Telegram bot token

#### Installation and running
```
pip install telepot
git clone https://github.com/byjk/tgshellbot.git
cd tgshellbot
python3 tgsbot.py
```

At first time running you will need enter bot token, then connect to bot in telegram and confirm admin account. That's all.

#### Bot commands
Bot can use commands via plugins. For now there is only one plugin: aliases.py, with two commands: __/setalias__ and __/delalias__.
```
Usage:
/setalias alias_name aliascmd [aliascmd]
For example:
/setalias tsm transmission-remote -n admin:pwd

After that bot can invoke next commands :
/tsm -l  
/tsm -a /home/user/Download/file.torrent

/delalias alias_name1 [alias_name2]
```
This command will remove alias_name1 

#### Bot plugins
Plugin is just a python file with 3 mandatory functions:
* plugin_init(mainbot)
* plugin_ismycmd(cmd)
* plugin_handler(msg)

##### plugin_init
plugin_init called when bot is started, mainbot is variable that can be used for sending messages to user later

##### plugin_ismycmd
plugin_ismycmd called to check support particular command in plugin, if plugin supports that command than this function must return True, else False.
        
##### plugin_handler
plugin_handler called on user command. msg - whole user message text. 
Plugin can reply user with __mainbot.sendMessage__('plugin reply text')

#### Known problems
Some programs output can provide error: 'charmap' codec can't decode byte. I don't know how to fix that, for now. 
