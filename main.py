#from postfix import *
from postfix_v2 import *
from thompson_v3 import *
from afd_direct import *
from subconjunto_afd import *
from simulation import *
from afd_minimization import *

cadena = []
r ="(b|b)*?a?b?b?(a|b)*"
w = "babbaaaaa"
#r = "(a|b)?(a?b?b?a|(a?b)*?b?a)"

for a in w:
    cadena.append(a)

postfix = transform_postfix(r)


afn_recieved = construccion_thompson(postfix)
afn_afd_recieved = afd_construction(afn_recieved[0],r,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved)-1][1])
afd_directo(afn_recieved, postfix)
afn = afn_afd_recieved[0]
afd = afn_afd_recieved[1]

simulacion_afn(afn,cadena,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved)-1][1])
simulacion_afd(afd,cadena,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved)-1][1])

print(afd)
print("==================================================================")
print("==================================================================")
print("==================================================================")
print("==================================================================")
print("==================================================================")
print("==================================================================")
print("==================================================================")

minimizeAfd(afd, afn_afd_recieved, afn_recieved[1][len(afn_recieved)-1][1])
