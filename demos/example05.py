import sys

sys.path.append('..')
import pyblebars

atext01='''
%(each('atext02',[1,2,3,4]))s
%(each('atext03',['a','b','c',1,2,3],' <separator> '))s
%(each('atext04',['a','b','c',1,2,3],' <separator> ','<before> \\n',atext05))s
'''

atext02='%(args[0])s '

atext03='%(args[0])s'

atext04='''%(kwargs['index']+1)s: %(args[0])s'''

atext05='''
<after>
'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02
pb['atext03']=atext03
pb['atext04']=atext04
pb['atext05']=atext05

print pb['atext01']
