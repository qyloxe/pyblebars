import sys

sys.path.append('..')
import pyblebars

atext01='''
test0: %(test0)s
func01a: %(myfunc01())s
func01b: %(myfunc01().lower())s
func02a: %(myfunc02())s
func02b: %(myfunc02()[2])s
set: %(set('test1',myfunc03()))s
test1: %(test1)s
test1.a: %(test1.a)s
test1.d.b: %(test1.d.b)s
test1.d.d.c: %(test1.d.d.c)s
func04a: %(myfunc04(`test1.a`))s
test2: %(test2)s
test3.a: %(test3.a)s
chain: %(chain(set('tv1',1),set('tv2',2),set('tv3',tv1+tv2),`tv3+1`,'*',`myfunc05()`,'=',`4*3`))s
'''

class MyPyblebars(pyblebars.Pyblebars):
   def myfunc01(self):
      return 'MYFUNC01'
   def myfunc02(self):
      return [1,2,3]
   def myfunc03(self):
      return {'a':1,'d':{'b':2,'d':{'c':3}}}
   def myfunc04(self,value):
      self.test2='TEST2'
      self.test3={'a':1,'d':{'b':2,'d':{'c':3}}}
      return 'myfunc04: '+value
   def myfunc05(self):
      return self.tv3

pb=MyPyblebars(test0='abc')
pb['atext01']=atext01

print pb['atext01']
