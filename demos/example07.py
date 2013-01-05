import sys

sys.path.append('..')
import pyblebars

atext01='''
%(each('atext02',[1,2,3,4]))s
'''

atext02='''%(kwargs['index']+1)s: %(args[0])s == %(case(
      args[0],
      {1:'aa',2:'bb',3:'cc'},
      '???'
   )
)s
'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02

print pb['atext01']
