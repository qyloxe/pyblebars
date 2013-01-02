import sys

VERBOSE=0

class PyblebarReplacer(dict):
   def __init__(self):
      self.t={}
      self.a=[]
      self.k=[]
   def eval(self,value):
      if type(value)!=type(''):
         return value
      if hasattr(self,value):
         if VERBOSE:
            print 'GETATTR:',value
         return getattr(self,value)
      if self.t.has_key(value):
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
      self.t[atemplatename]=atemplattext
      return ''
   def pushargs(self,*args,**kwargs):
      self.a.append(args)
      self.args=args
      self.k.append(kwargs)
      self.kwargs=kwargs
   def popargs(self):
      self.a.pop()
      self.k.pop()
   def call(self,atemplatename,*args,**kwargs):
      if VERBOSE:
         print '  CALL:',atemplatename,args
      self.pushargs(*args,**kwargs)
      s=self.t[atemplatename]
      ret=s%self
      self.popargs()
      return ret
   def iif(self,condition,vtrue,vfalse=''):
      if VERBOSE:
         print 'IF',condition,vtrue,vfalse
      if condition:
         return vtrue
      return vfalse
