import sys

sys.path.append('..')
import pyblebars

atext01='''
s1=%(s1)s
i1=%(i1)s
d1=%(d1)s
l1=%(l1)s
d2=%(d2)s
d2.a=%(d2.a)s
d2.d=%(d2.d)s
d2.d.b=%(d2.d.b)s
d2.d.d2=%(d2.d.d2)s
d2.d.d2.c=%(d2.d.d2.c)s
'''

d1={
   'a':1,
   'b':'B'
}

l1=['a','b',1,2]

d2={
   'a':1,
   'd': {
      'b':2,
      'd2': {
         'c':3
      }
   }
}

pb=pyblebars.Pyblebars(s1='S1',i1=11,d1=d1,l1=l1,d2=d2)
pb['atext01']=atext01

print pb['atext01']
