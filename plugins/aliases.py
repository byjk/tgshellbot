import os
import json

_cmds = {}
_config = os.path.abspath(__file__)
_config = os.path.join(os.path.dirname(_config ),'aliases.conf')

def plugin_init(mainbot):
    global _cmds
    try:
        with open(_config, 'r') as json_data_file:
            x = json.load(json_data_file)
            if isinstance(x, dict):
                _cmds = x
    except Exception:
        _cmds = {}   

def plugin_ismycmd(txt):
    cmd = txt.split(' ')
    c = cmd[0].lower().strip()
    if c[0] != '/':
        return False
    c = c[1:]
    return (c in ['setalias', 'delalias', 'aliases'] or c in _cmds.keys())

def plugin_handler(msg, mainbot):
    global _cmds
    cmd = msg.split(' ')
    c = cmd[0].lower().strip()[1:]
    if c == 'setalias':
        if len(cmd) > 2:
            _cmds[cmd[1]] = ' '.join(cmd[2:])
            savecmd()
            mainbot.sendMessage('alias {0} saved'.format(cmd[1]))
        else:            
            mainbot.sendMessage('Not much parameters huh?')
    elif c == 'delalias':
        for c in cmd[1:]:
            if c in _cmds.keys():
                _cmds.pop(c)
                mainbot.sendMessage('alias {0} removed'.format(c))
        savecmd()
    elif c == 'aliases':
        for c in _cmds.keys():
            mainbot.sendMessage('{0}={1}'.format(c, _cmds[c]))
    else:
        cmd[0] = _cmds[c]
        mainbot.call_shell(' '.join(cmd))

def savecmd():
    global _cmds
    with open(_config, 'w') as outfile:
        json.dump(_cmds, outfile)
