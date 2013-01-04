import sys

__version_info__ = ('0', '1', '2')
__version__ = '.'.join(__version_info__)

VERBOSE=0

class PyblebarReplacer(dict):
   def __init__(self):
      self._t={}
      self._a=[]
   def eval(self,value):
      if type(value)!=type(''):
         return value
      if hasattr(self,value):
         if VERBOSE:
            print 'GETATTR:',value
         return getattr(self,value)
      if self._t.has_key(value):
         if VERBOSE:
            print 'GET:',value
         return self.call(value)
      if sys.modules.has_key(value):
         if VERBOSE:
            print 'MODULE:',value
         return sys.modules[value]
      if VERBOSE:
         print 'GETITEM:',value
      ret=eval(value,self,self)
      return ret
   def __getitem__(self,name):
      return self.eval(name)
   def register(self,atemplatename,atemplattext):
      self._t[atemplatename]=atemplattext
      return ''
   def pushargs(self,*args,**kwargs):
      self._a.append((args,kwargs))
      self.args=args
      self.kwargs=kwargs
   def popargs(self):
      self.args,self.kwargs=self._a.pop()
   def call(self,atemplatename,*args,**kwargs):
      if VERBOSE:
         print '  CALL:',atemplatename,args
      self.pushargs(*args,**kwargs)
      s=self._t[atemplatename]
      ret=s%self
      self.popargs()
      return ret
   def iif(self,condition,vtrue,vfalse=''):
      if VERBOSE:
         print 'IF',condition,vtrue,vfalse
      if condition:
         return vtrue
      return vfalse
   def each(self,atemplatename,args,aseparator='',abefore='',aafter=''):
      if VERBOSE:
         print 'EACH',atemplatename,args,aseparator
      ret=[]
      i=0
      for arg in args:
         ret.append(self.call(atemplatename,arg,index=i))
         i=i+1
      if i:
         return abefore+aseparator.join(ret)+aafter
      return aseparator.join(ret)
