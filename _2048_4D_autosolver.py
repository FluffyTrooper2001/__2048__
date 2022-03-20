from _2048_4D import*;from time import time as t;from random import randint as r
@lambda f:setattr(Interface,'run',f)or Interface()
def interface(self):
  n,c,fps=t(),0,"calculating...";print('\x1bc');T,count=t(),0
  while not self.eng.gameend:
    if n+1<t():n,fps,c=t(),c,0;count+=1
    else:c+=1;count+=1
    self.next_frame(self.eng.swipe(r(0,7))+f"highest: %s fps: \x1b[{32+(fps<40)-2*(fps<10)if type(fps)==int else 0:d}m{fps: <14} \x1b[mtime: {(lambda _t:f'{int(_t)//3600:0>2}:{(int(_t)%3600)//60:0>2}:{_t%60: <5.2f}')(t()-T): <14} \x1b[mticks: {count}"%(lambda x:x.colour(f'{str(int(x))+chr(27)+"[m": <21}'))(max([self.eng[a] for a in self.eng],key=int)))