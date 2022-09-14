from postfix import *
from thompson_v2 import *
from afd import *

r ="(b|b)*?a?b?b?(a|b)*"

afn_recieved = transform_postfix(r)
afd(afn_recieved,r, "q6")

