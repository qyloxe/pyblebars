import sys

sys.path.append('..')
import pyblebars

atext01='Hello %(atext02)s'

atext02='World!'

pb=pyblebars.Pyblebars()
pb['atext01']=atext01
pb['atext02']=atext02

print pb['atext01']
