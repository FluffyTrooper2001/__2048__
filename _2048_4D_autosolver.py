from _2048_4D import*;from time import time as t;from random import randint as r
class InterruptedGame(KeyboardInterrupt):
  def __init__(self, data):self.data=data;super().__init__()
@lambda f:setattr(Interface,'run',f)or(Interface()if __name__=='__main__'else Interface)
def interface(self):
  n,c,fps=t(),0,"calculating...";print('\x1bc');T,count=t(),0;e0,e1=Engine(),Engine()
  try:
    while not self.eng.gameend:
      if n+1<t():n,fps,c=t(),c,0;count+=1
      else:c+=1;count+=1
      f=lambda s:(lambda _q:(_q,_q.index(max(_q))))([sum([int(s[a])for a in filter(lambda x:3 not in[*x],s.eng if hasattr(s,'eng')else s)for b in[(*[x+y for x,y in zip(a,offset)],)]if int(s[a])==int(s[b])])for offset in((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))]);q,p=f(self)
      if q[p]:x,y=[(2,3),(0,1),(6,7),(4,5)][p];e0.load(eval(repr(self.eng))),e1.load(eval(repr(self.eng)));g=lambda e,z:[e.swipe(z),sum(f(e)[0])];(X,x),(Y,y)=g(e0,x),g(e1,y);i=[x,y].index(max((x,y)))if[*{x,y}][1:]else r(0,1);move=(X,Y)[i];self.eng.load(eval(repr((e0,e1)[i])))
      else:move=self.eng.swipe(r(0,7))
      self.next_frame(move+f"highest: %s fps: \x1b[{32+(fps<40)-2*(fps<10)if type(fps)==int else 0:d}m{fps: <14} \x1b[mtime: {(lambda _t:f'{int(_t)//3600:0>2}:{(int(_t)%3600)//60:0>2}:{_t%60: <5.2f}')(t()-T): <14} \x1b[mticks: {count: <30}"%(lambda x:x.colour(f'{str(int(x))+chr(27)+"[m": <21}'))(max([self.eng[a] for a in self.eng],key=int)))
  except KeyboardInterrupt as ki:raise InterruptedGame(self)from ki