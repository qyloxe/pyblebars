import sys

sys.path.append('..')
import pyblebars

atext01='''
cond01: %(iif(1==1,'condition is true','condition is false'))s
cond02: %(iif(0==1,'condition is true','condition is false'))s
cond03: %(iif(1==1,atext02))s
cond04: %(iif(1==1,call('atext03',1,2)))s
cond05: %(iif('a'=='b',call('atext03',0,0),call('atext03',1,1)))s
'''

atext02='text02'

atext03='''text03: %(args[0])s %(args[1])s'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02
pb['atext03']=atext03

print pb['atext01']
