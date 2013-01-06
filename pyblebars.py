import sys

__version_info__ = ('0', '1', '4')
__version__ = '.'.join(__version_info__)

VERBOSE=0

class AttrDict(dict):
   def __getattr__(self,value):
      if self.has_key(value):
         v=self.__getitem__(value)
         if type(v)==type({}):
            return AttrDict(v)
         return v

class Pyblebars(dict):
   def __init__(self,**kwargs):
      self._t={}
      self._a=[]
      self._r=[]
      self.args=None
      self.kwargs=None
      for k,v in kwargs.items():
         setattr(self,k,v)
   def eval(self,value):
      if type(value)!=type(''):
         return value
      if hasattr(self,value):
         if VERBOSE:
            print 'GETATTR:',value
         ret=getattr(self,value)
         if type(ret)==type({}):
            return AttrDict(ret)
         return ret
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
   def __setitem__(self,name,value):
      self.register(name,value)
   def register(self,templatename,templattext):
      self._t[templatename]=templattext
      return ''
   def pushargs(self,templatename,*args,**kwargs):
      if VERBOSE:
         print '    PUSHARGS:',args,kwargs
      self._r.append(templatename)
      self._a.append((self.args,self.kwargs))
      self.args=args
      self.kwargs=kwargs
   def popargs(self):
      self.args,self.kwargs=self._a.pop()
      self._r.pop()
      if VERBOSE:
         print '    POPARGS:',self.args,self.kwargs
   def call(self,templatename,*args,**kwargs):
      if VERBOSE:
         print '  CALL:',templatename,args,kwargs
      if templatename in self._r:
         if VERBOSE:
            print '    RECURSION:',templatename
         return ''
      s=self._t[templatename]
      self.pushargs(templatename,*args,**kwargs)
      if VERBOSE:
         print '    TEMPLATE START:'
         print s
         print '    TEMPLATE END:'
      ret=s%self
      self.popargs()
      return ret
   def iif(self,condition,vtrue,vfalse=''):
      if VERBOSE:
         print 'IF',condition,vtrue,vfalse
      if condition:
         return vtrue
      return vfalse
   def each(self,templatename,args,separator='',before='',after=''):
      if VERBOSE:
         print 'EACH',templatename,args,separator
      ret=[]
      i=0
      for arg in args:
         ret.append(self.call(templatename,arg,index=i))
         i=i+1
      if i:
         return before+separator.join(ret)+after
      return separator.join(ret)
   def case(self,value,choices,default=''):
      if VERBOSE:
         print 'CASE',value,choices,default
      return choices.get(value,default)
   def set(self,name,value):
      if VERBOSE:
         print 'SET',name,value
      setattr(self,name,value)
      return ''
   def chain(self,*args,**kwargs):
      if VERBOSE:
         print 'CHAIN',args,kwargs
      return kwargs.get('before','')+kwargs.get('separator','').join(args)+kwargs.get('after','')
