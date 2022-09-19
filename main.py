#from postfix import *
from postfix_v2 import *
from thompson_v3 import *
from afd_direct import *
from subconjunto_afd import *

r ="(b|b)*?a?b?b?(a|b)*"
# r = "(a|b)?(a?b?b?a|(a?b)*?b?a)"


postfix = transform_postfix(r)

afn_recieved = construccion_thompson(postfix)
afd_construction(afn_recieved,r,"q6","q18")
