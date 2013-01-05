import os
import sys
import time

sys.path.append('..')
import pyblebars

atext01='''
value01: %(time.strftime('%Y:%m:%d',time.localtime()))s
value02: %(os.listdir('.'))s

%(each('atext02',os.listdir('.')))s
'''

atext02='''%(kwargs['index']+1)s: %(args[0])s
'''

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02

print pb['atext01']
