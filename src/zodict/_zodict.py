# Copyright BlueDynamics Alliance - http://bluedynamics.com
# Python Software Foundation License

from odict import odict
from zope.interface import implements
from zope.interface.common.mapping import IEnumerableMapping, IFullMapping
from zodict.interfaces import IAttributeAccess

class Zodict(odict):
    """Mark ordered dict with corresponding interface.
    """
    implements(IFullMapping)
    
    def __init__(self, data=()):
        odict.__init__(self, data=data)

zodict = Zodict
from zope.deprecation import deprecated
deprecated('zodict', "'zodict' has been renamed to 'Zodict'. Please modify your"
                     " code and import to use: 'from zodict import Zodict'")

class ReverseMapping(object):
    """Reversed IEnumerableMapping.
    """
    
    implements(IEnumerableMapping)
    
    def __init__(self, context):
        """Object behaves as adapter for dict like object.
        
        ``context``: a dict like object.
        """
        self.context = context
    
    def __getitem__(self, value):
        for key in self.context:
            if self.context[key] == value:
                return key
        raise KeyError(value)
    
    def get(self, value, default=None):
        try:
            return self[value]
        except KeyError:
            return default

    def __contains__(self, value):
        for key in self.context:
            val = self.context[key]
            if val == value:
                return True
        return False
    
    def keys(self):
        return [val for val in self]

    def __iter__(self):
        for key in self.context:
            yield self.context[key]

    def values(self):
        return [key for key in self.context]

    def items(self):
        return [(v, k) for k, v in self.context.items()]

    def __len__(self):
        return len(self.context)

class AttributeAccess(object):
    """If someone really needs to access the original context (which should not 
    happen), she hast to use ``object.__getattr__(attraccess, 'context')``.
    """
    
    implements(IAttributeAccess)
    
    def __init__(self, context):
        object.__setattr__(self, 'context', context)
    
    def __getattr__(self, name):
        context = object.__getattribute__(self, 'context')
        try:
            return context[name]
        except KeyError:
            raise AttributeError(name)
    
    def __setattr__(self, name, value):
        context = object.__getattribute__(self, 'context')
        try:
            context[name] = value
        except KeyError:
            raise AttributeError(name)
    
    def __getitem__(self, name):
        context = object.__getattribute__(self, 'context')
        return context[name]
    
    def __setitem__(self, name, value):
        context = object.__getattribute__(self, 'context')
        context[name] = value
    
    def __delitem__(self, name):
        context = object.__getattribute__(self, 'context')
        del context[name]