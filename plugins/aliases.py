import os
import json

_cmds = {}
_mainBot = None
_config = os.path.abspath(__file__)
_config = os.path.join(os.path.dirname(_config ),'aliases.conf')


def plugin_init(mainbot):
    global _mainBot
    global _cmds
    _mainBot = mainbot
    try:
        with open(_config, 'r') as json_data_file:
            x = json.load(json_data_file)
            if isinstance(x, dict):
                _cmds = x
    except Exception:
        _cmds = {}   

def plugin_ismycmd(cmd):
    return (cmd in ['setalias', 'delalias'] or cmd in _cmds.keys())

def plugin_handler(msg):
    global _mainBot
    global _cmds
    cmd = msg.split(' ')
    c = cmd[0].lower()[1:]
    if c == 'setalias':
        if len(cmd) > 2:
            _cmds[cmd[1]] = ' '.join(cmd[2:])
            savecmd()
            _mainBot.sendMessage('alias {0} saved'.format(cmd[1]))
        else:            
            _mainBot.sendMessage('Not much parameters huh?')
    elif c == 'delalias':
        for c in cmd[1:]:
            if c in _cmds.keys():
                _cmds.pop(c)
                _mainBot.sendMessage('alias {0} removed'.format(c))
        savecmd()
    else:
        cmd[0] = _cmds[c]
        _mainBot.call_shell(' '.join(cmd))

def savecmd():
    global _cmds
    with open(_config, 'w') as outfile:
        json.dump(_cmds, outfile)
