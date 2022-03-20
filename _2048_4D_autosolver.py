from _2048_4D import*;from time import time as t;from random import randint as r
class InterruptedGame(KeyboardInterrupt):
  def __init__(self, data):self.data=data;super().__init__()
@lambda f:setattr(Interface,'run',f)or(Interface()if __name__=='__main__'else Interface)
def interface(self):
  n,c,fps=t(),0,"calculating...";print('\x1bc');T,count=t(),0
  try:
    while not self.eng.gameend:
      if n+1<t():n,fps,c=t(),c,0;count+=1
      else:c+=1;count+=1
      q=[sum([int(self[a])for a in filter(lambda x:3 not in[*x],self.eng)for b in[(*[x+y for x,y in zip(a,offset)],)]if int(self[a])==int(self[b])])for offset in((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))]
      p=q.index(max(q));move=[[r(2,3),r(0,1),r(6,7),r(4,5)][p],r(0,7)][not q[p]]
      self.next_frame(self.eng.swipe(move)+f"highest: %s fps: \x1b[{32+(fps<40)-2*(fps<10)if type(fps)==int else 0:d}m{fps: <14} \x1b[mtime: {(lambda _t:f'{int(_t)//3600:0>2}:{(int(_t)%3600)//60:0>2}:{_t%60: <5.2f}')(t()-T): <14} \x1b[mticks: {count}"%(lambda x:x.colour(f'{str(int(x))+chr(27)+"[m": <21}'))(max([self.eng[a] for a in self.eng],key=int)))
  except KeyboardInterrupt as ki:raise InterruptedGame(self)from ki