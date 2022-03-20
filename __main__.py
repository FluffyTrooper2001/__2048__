try:from.import*
except:from __init__ import*
try:AutoInterface4D()
except InterruptedGame as game:(interface:=game.data).install((engine:=interface.uninstall()))