import pyblebars

import os
import time

atext01='''
   %(call('atext06',1,2,3,p1=1,p2=2,p3='xxx'))s
   %(atext03)s
   if 1: %(iif('1'=='1',call('atext07'),call('atext05')))s
   if 0: %(iif('1'=='0',call('atext04'),call('atext05')))s
   %(`time.clock()`)s
   %(each('atext08',[1,2,3,4]))s
   %(each('atext08',['a','b','c',1,2,3],'XX','AA','BB'))s
'''

atext01b='''
for i in %(atext02(1,2,"aaa","bbb","sss",{a:1,b:2,c:3},atext05))s:
   %(atext03)s
'''

atext02='''[aa,bb,cc,%(atext05)s]'''

atext03='''
   text02_1
   if %(atext04)s:
      text02_2
'''

atext04='''text04 - %(myfunc01().lower())s'''

atext05='''text05'''

atext06='''text06{%(args[0])s,%(args[1])s,%(args[2])s,%(kwargs['p1'])d,%(kwargs['p2'])d,%(kwargs['p3'])s}'''

atext07='''text07'''

atext08=''' [el: %(args[0])s]'''

class MyReplacer(pyblebars.PyblebarReplacer):
   def myfunc01(self):
      return 'MYFUNC01'
      
atr=MyReplacer()
atr.register('atext01',atext01)
atr.register('atext02',atext02)
atr.register('atext03',atext03)
atr.register('atext04',atext04)
atr.register('atext05',atext05)
atr.register('atext06',atext06)
atr.register('atext07',atext07)
atr.register('atext08',atext08)
s=atr.call('atext01')
print s
