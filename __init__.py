try:from.import _2048
except:from _2048 import Engine, Interface;from _2048_4D import Engine as Engine4D, Interface as Interface4D;from _2048_4D_autosolver import interface as AutoInterface4D,InterruptedGame
else:from._2048 import Engine, Interface;from._2048_4D import Engine as Engine4D, Interface as Interface4D;from._2048_4D_autosolver import interface as AutoInterface4D,InterruptedGame