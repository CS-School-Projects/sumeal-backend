from .base import *
try:
    from .local_settings import * 
except ImportError as e:
    pass
