import sys

sys.path.append('..')
import pyblebars

atext01='''[before]
%(call('atext02',1,2,'abc',p1='a',p2='b',p3=3))s
[after]
'''

atext02='''text02: {%(args[0])s,%(args[1])s,%(args[2])s,%(kwargs['p1'])s,%(kwargs['p2'])s,%(kwargs['p3'])s}'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02

print pb['atext01']
