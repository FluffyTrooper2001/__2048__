import random as _random;from itertools import product;COLOURS=type('donct',(dict,),{'__missing__':lambda s,k:(lambda x:(lambda*y:(*map(lambda z:int(z,16),y),[0,220][sum(map(lambda z:int(z,16),y))<360]))(x[-6:-4],x[-4:-2],x[-2:-1]))(hex(hash(str(k)))[2:].zfill(6))})({0:(125,125,125,125),2:(220,210,200,0),4:(220,210,160,0),8:(220,160,110,220),16:(230,142,96,220),32:(240,118,90,220),64:(230,90,50,220),128:(220,190,108,0),256:(220,190,96,0),2<<8:(220,188,74,0),4<<8:(220,186,50,0),8<<8:(210,174,60,220),4<<10:(96,220,110,0),8<<10:(50,210,96,220),4<<12:(20,96,20,220),2<<14:(50,210,220,0),4<<14:(20,80,96,220)});__import__('os').system('')
@type.__call__
class rgb:
  def __str__(self):return'\x1b['
  def __format__(self,a='end'):
    if a.lower()=='end':return str(self)+'m'
    rgb=a.split(';');*_,H=rgb+[0]*(4-len(rgb));return f'{str(self)}{38+10*int(H)};2;{";".join(_)}m'
  def __call__(self,r,g,b,H=0>0,end=0>0):return lambda s='',end=end:f'{self:{r};{g};{b};{int(H)}}{s}'+end*f'{self:end}'
class GameOver(RuntimeError):0
class EmptyCell:
  value=0;__index__=__int__=lambda s:int(s.value);__bool__=lambda s:0>0;is_empty=True;__hash__=lambda s:0;__iter__=lambda s:iter(s.coords);colour=lambda s,a:f"{rgb:end}{a}";__format__=lambda s,f='0':s.colour([' '*7,'\x1b[90m_______'][int(f)])+'\x1b[90m';__repr__=lambda s:str(int(s)or' ');__str__=lambda s:str(int(s))
  def __init__(self,*c,v=0):self.move(*c)
  def move(self,*c):self.coords=c;return self
class Cell(EmptyCell):
  def __init__(self,x,y,v=0):self.move(x,y).value=v or 2*_random.randint(1,2)
  __bool__=lambda s:1>0;is_empty=False;__eq__=lambda s,o:not[*{hash(s),hash(o)}][1:];__hash__=lambda s:hash(s.coords);colour=lambda s,T:(lambda r,g,b,t:rgb(r,g,b,1,1)(rgb(t,t,t)(T)))(*COLOURS[int(s)])
class Engine:
  def __init__(self):
    self.matrix=[[EmptyCell(i,j)for i in range(4)]for j in range(4)];r=lambda:(lambda l:(l(),l()))(lambda:_random.randint(0,3));f=lambda:Cell(*r(),2);a=f(),f()
    while-len({*a})+2:a[1].move(*r())
    *map(lambda i:[()for self[i]in[i]],a),
  def __setitem__(self,item,value): 
    for i,j in[item]:self.matrix[j][i]=value
  def __getitem__(self,item):
    for i,j in[item]:return self.matrix[j][i]
  def __iter__(self):return iter(product(range(4),repeat=2))
  def empty(self,i,j):_=self[i,j]=EmptyCell(i,j);return _
  def _swipe(self,i,d):
    m=[[self[i,q]for q in range(4)],[self[i,q-1]for q in range(4,0,-1)],[self[q-1,i]for q in range(4,0,-1)],[self[q,i]for q in range(4)]][d];q=[*map(int,m)]
    for j in range(3):
      y=q[j:]
      while not y[0]and any(y[1:]):q+=[q.pop(j)];y+=[y.pop(0)]
    for j in range(3):
      y=q[j:]
      if not[*{*y[:2]}][1:]:q[j]+=q.pop(j+1);q+=[0]
    for j,n in enumerate(q):
      if n:self[m[j]]=Cell(*m[j],n)
      else:self.empty(*m[j])
    return q!=[*map(int,m)]
  def swipe(self,d:int):
    import sys;assert d in range(4);c=any([self._swipe(i,d)for i in range(4)])
    if c:
      from random import choice;_=[*filter(lambda x:self[x].is_empty,self)]
      if _:a=choice(_);self[a]=Cell(*a)
    if self.gameend:raise GameOver(["Game lost", "Game won"][self.gamewon])
    return["Invalid move ",[f"swiped {['up','down','right','left'][d]: <5s}","Game won.      "][self.gamewon]][c]
  gamewon=property(lambda s:any([int(s[a])>=2<<10 for a in s]));gameend=property(lambda self:not any([not all(self[a]for a in self),any(int(a)==int(b)for row in self.matrix for a,b in(row[:2],row[1:3],row[2:])),any(int(a)==int(b)for col in zip(*self.matrix)for a,b in(col[:2],col[1:3],col[2:]))]));up,down=lambda s:s.swipe(0),lambda s:s.swipe(1);right,left=lambda s:s.swipe(2),lambda s:s.swipe(3);__repr__=__str__=lambda s:'[\n'+',\n'.join([' ['+','.join([f"{str(s[i,j]): ^7s}"for i in range(4)])+']'for j in range(4)])+'\n]';view=lambda s:print(s);__bool__=lambda s:not s.gameend;set=lambda s,i,j,n=0:s.__setitem__((i,j),Cell(i,j,n)if n else EmptyCell(i,j))
class Interface:
  input=__import__('msvcrt')if __import__('os').name=='nt' else type('msvcrt',(),{'getch':lambda:'\x1b','kbhit':lambda:True});os=__import__('os');__call__=lambda s,i,j:s.eng[i,j].colour(f"{int(s.eng[i,j])or' ': ^7}")+'\x1b[90m'
  def __init__(self):
    try:self.install(Engine());self.run()
    except GameOver as e:self.next_frame();print(f'\x1b[H\x1b[2K{str(e): <12}'+'\n'*16)
    except Exception as e:print(f"\x1b[2K{e.__class__.__name__}: {e}"+'\n'*18)
  def quit(self):raise GameOver(["Game quit","Game won"][self.eng.gamewon])
  def next_frame(self,message=''):print(f"""\x1b[H\033[m{message}\x1b[90m
._______________________________. 
|{self.eng[0,0]:0}|{self.eng[1,0]:0}|{self.eng[2,0]:0}|{self.eng[3,0]:0}|
|{self(0,0)}|{self(1,0)}|{self(2,0)}|{self(3,0)}|
|{self.eng[0,0]:0}|{self.eng[1,0]:0}|{self.eng[2,0]:0}|{self.eng[3,0]:0}|
+-------+-------+-------+-------+
|{self.eng[0,1]:0}|{self.eng[1,1]:0}|{self.eng[2,1]:0}|{self.eng[3,1]:0}|
|{self(0,1)}|{self(1,1)}|{self(2,1)}|{self(3,1)}|
|{self.eng[0,1]:0}|{self.eng[1,1]:0}|{self.eng[2,1]:0}|{self.eng[3,1]:0}|
+-------+-------+-------+-------+
|{self.eng[0,2]:0}|{self.eng[1,2]:0}|{self.eng[2,2]:0}|{self.eng[3,2]:0}|
|{self(0,2)}|{self(1,2)}|{self(2,2)}|{self(3,2)}|
|{self.eng[0,2]:0}|{self.eng[1,2]:0}|{self.eng[2,2]:0}|{self.eng[3,2]:0}|
+-------+-------+-------+-------+
|{self.eng[0,3]:0}|{self.eng[1,3]:0}|{self.eng[2,3]:0}|{self.eng[3,3]:0}|
|{self(0,3)}|{self(1,3)}|{self(2,3)}|{self(3,3)}|
|{self.eng[0,3]:1}|{self.eng[1,3]:1}|{self.eng[2,3]:1}|{self.eng[3,3]:1}|\x1b[m\x1b[H""")
  def uninstall(self):eng=self.eng;del self.eng;return eng
  def install(self,engine):self.eng=engine
  def run(self):
    self.eng and print('\x1b[H\x1bc')
    while not self.eng.gameend:c=self.input.kbhit()and self.input.getch().decode('ANSI')or'\1';self.next_frame({c in'wasd':lambda:self.eng.swipe(str.maketrans('wasd','\0\3\1\2')[ord(c)]),c=='\xe0':lambda:(lambda _c:self.eng.swipe(str.maketrans('KHMP','\3\0\2\1')[_c])if chr(_c)in'KHMP'else self.quit())(ord(self.input.getch().decode('ANSI'))),c=='\x1b':self.quit}.get(1>0,lambda:'')())
game_won=__name__=='__main__'and Interface().eng.gamewon