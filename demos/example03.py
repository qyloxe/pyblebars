import sys

sys.path.append('..')
import pyblebars

atext01='''[before]
%(call('atext02',1,2,'abc',p1='a',p2='b',p3=3))s
[after]
'''

atext02='''
text02: %(args[0])s,%(args[1])s,%(args[2])s
call03: %(call('atext03','ABC',1,2))s
text02: %(kwargs['p1'])s,%(kwargs['p2'])s,%(kwargs['p3'])s
'''

atext03='''text03: %(args[0])s'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02
pb['atext03']=atext03

print pb['atext01']
