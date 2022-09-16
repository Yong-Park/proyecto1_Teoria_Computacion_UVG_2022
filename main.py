from postfix import *
from thompson_v2 import *
from afd import *
from afd_direct import *

r ="(b|b)*?a?b?b?(a|b)*"

postfix = transform_postfix(r)
afd_directo(postfix)
#afn_recieved = construccion_thompson(postfix)

#afd(afn_recieved,r, "q6")