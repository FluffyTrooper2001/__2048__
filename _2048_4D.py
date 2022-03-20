from random import randint,shuffle;from _2048 import GameOver,COLOURS,rgb,product,EmptyCell
class BaseCell(EmptyCell):__format__=lambda s,f='0':'\x1b[90m'+7*' _'[f=='2'and s.coords[1]==3]
class Cell(BaseCell):__init__=lambda s,w,x,y,z,v=0:setattr(s.move(w,x,y,z),'value',v or 2*randint(1,2));__bool__=lambda s:1>0;is_empty=0>0;__eq__=lambda s,o:not[*{int(s),int(o)}][1:];__hash__=lambda s:hash(s.coords);colour=lambda s,T:(lambda r,g,b,t:rgb(r,g,b,1,1)(rgb(t,t,t)(T)))(*COLOURS[int(s)]);__str__=lambda s:f"{int(s): ^21d}";__format__=lambda s,f='1':s.colour(str(s)[int(f)*7:7+int(f)*7].__format__(f' {"<^>"[int(f)]}7s').replace(' ',[' ','\x1b[90m_'][f=='2'and s.coords[1]==3]))
class Engine:
  def __init__(self):self.matrix=[[[[BaseCell(i,j,k,l)for i in range(4)]for j in range(4)]for k in range(4)]for l in range(4)];r=lambda a:shuffle(a)or a[:16];a=[Cell(*c,2)for c in r([*self])];[()for x in a for self[x]in[x]]
  def empty(self,*c):x=self[c]=BaseCell(*c);return x
  def load(self,m):return[self[w,x,y,z]for w,x,y,z in self for self[w,x,y,z]in[m[z][y][x][w]]]
  def swipe(self,d):
    def _swipe(i):
      def _s(j):
        def _s_(k):
          r=[*range(4)];m=[[self[i,q,j,k]for q in r],[self[i,q,j,k]for q in r][::-1],[self[q,i,j,k]for q in r][::-1],[self[q,i,j,k]for q in r],[self[i,j,k,q]for q in r],[self[i,j,k,q]for q in r][::-1],[self[i,j,q,k]for q in r][::-1],[self[i,j,q,k]for q in r]][d];q=[*map(int,m)]
          for l in range(3):
            y=q[l:]
            while not y[0]and any(y[1:]):q+=[q.pop(l)];y+=[y.pop(0)]
          for l in range(3):
            if not[*{*q[l:l+2]}][1:]:q[l]+=q.pop(l+1);q+=[0]
          for l,n in enumerate(q):self.__setitem__(m[l],n)if n else self.empty(*m[l])
          return q!=[*map(int,m)]
        return any([_s_(k)for k in range(4)])
      return any([_s(j)for j in range(4)])
    r=any([_swipe(i)for i in range(4)])
    if r:_=[*filter(lambda x:not self[x],self)];shuffle(_);_=_[:16];[self.__setitem__(a,Cell(*a))for a in _]
    if self.gameend:raise GameOver(['Game lost', 'Game won'][self.gamewon])
    return["swiped "+['up','down','right','left','in','out','forward','backward'][d],"Game Won","invalid move"][max(2*(not r),self.gamewon)].__format__(' <18s')
  gameend=property(lambda self:all([self[a]for a in self])and not[0 for a in self for _ in[1,-1]for offset in[(_,0,0,0),(0,_,0,0),(0,0,_,0),(0,0,0,_)]for b in[(*[x+y for x,y in zip(a,offset)],)]if len([*filter(range(4).__contains__,b)])==4 if int(self[a])==int(self[b])]);up,down,right,left,in_,out,forward,backward=[(lambda s:s.swipe(i)+'\n'+str(s))for i in range(8)];set=lambda s,i,j,k,l,n:s.__setitem__((i,j,k,l),[Cell,BaseCell][not n](i,j,k,l,*(n,)*bool(n)))or s;__iter__=lambda s:iter(product(range(4),repeat=4));gamewon=property(lambda s:any([int(s[a])>=2<<30 for a in s]));__bool__=lambda s:not s.gameend;__setitem__=lambda self,item,value:(lambda i,j,k,l:self.matrix[l][k][j].__setitem__(i,[Cell,BaseCell][not value](*item,*[[value],()][not value])if type(value)==int else value))(*item);__str__=__repr__=lambda self:'[\n '+',\n '.join(['[\n  '+',\n  '.join(map(lambda a:str([str(list(map(int,e))).__format__(' <25s')for e in a]),self.matrix[k]))+'\n ]' for k in range(4)]).replace("'",'')+'\n]';__getitem__=lambda self,item:(lambda i,j,k,l:self.matrix[l][k][j][i])(*item)
class Interface:
  input=__import__('msvcrt')if __import__('os').name=='nt'else type('msvcrt',(),{'getch':lambda:'\x1b','kbhit':lambda:True});os=__import__('os')
  def __init__(self):
    try:input("resize window");self.install(Engine());self.run()
    except GameOver as e:self.next_frame('Game Over');print(f'\x1b[H\x1b[2K{str(e): <20}'+'\n'*76)
    except Exception as e:raise type('YouFuckedUp',(Exception,),{'__name__':'YouFuckedUp','__qualname__':'YouFuckedUp'})from e
  def quit(self):raise GameOver(["Game quit","Game won"][self.eng.gamewon])
  def uninstall(self):eng=self.eng;del self.eng;return eng
  def install(self,engine):self.eng=engine
  def next_frame(s,message=''):r=lambda:range(4);print(f"""\x1b[H\x1b[0m{message}\x1b[90m^{"|^=|^".join(['|^~|^'.join(['|^'.join(['@@'.join(['|'.join([f"{s.eng[i,j,k,l]:{m}}"for i in r()])for k in r()])for m in map(str,range(3))])for j in r()])for l in r()])}/\x1b[m\x1b[A""".replace('~','@@'.join(['+'.join(4*['-'*7])]*4)).replace('=','@'*130).replace('@','\x1b[100m \x1b[49m').replace('^','\n\x1b[90m').replace('|','\x1b[90m|'))
  def run(self):
    self.eng and print('\x1b[H',end='\x1bc');self.next_frame("Game Start.")
    while not self.eng.gameend:(c:=self.input.kbhit()and self.input.getch().decode('ANSI')or'')and self.next_frame({c in'wasd':lambda:self.eng.swipe(str.maketrans('wasd','\0\3\1\2')[ord(c)]),c=='\xe0':lambda:(lambda _c:self.eng.swipe(str.maketrans('KHMP','\7\4\6\5')[_c])if chr(_c)in'KHMP'else self.quit())(ord(self.input.getch().decode('ANSI'))),c=='\x1b':self.quit}.get(1>0,lambda:'')())
game_won=__name__=='__main__'and Interface().eng.gamewon # this is five thousand characters