#from postfix import *
from postfix_v2 import *
from thompson_v3 import *
from afd_directV2 import AFDD
from direct_lector import DirectReader
from direct_parser import Parser
from subconjunto_afd import *
from simulation import *
from minimization import *

cadena = []
#r ="(b|b)*?a?b?b?(a|b)*"
w = "babbaaaaa"
#r = "a?(a|b)*"
#r = "(0|1)*?0?0"
r = "(a|b)?(a?b?b?a|(a?b)*?b?a)"

for a in w:
    cadena.append(a)
#transformacion en postfix
postfix = transform_postfix(r)

#construccion de thompson del postfix
afn_recieved = construccion_thompson(postfix)
# print("==========")
# print(afn_recieved[1][0][0])
# print(afn_recieved[1][len(afn_recieved[1])-1][1])
#convierte el postfix en afn correcto y luego a su correspondiente afd
afn_afd_recieved = afd_construction(afn_recieved[0],r,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved[1])-1][1])
#guarda el afn y afd recivido
afn = afn_afd_recieved[0]
afd = afn_afd_recieved[1]
#minimizacion del afd
print("==================================================================")
minimization(afd, afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved[1])-1][1])

#afd directo
direct_reader = DirectReader(r)
direct_tokens = direct_reader.CreateTokens()
direct_parser = Parser(direct_tokens)
direct_tree = direct_parser.Parse()

ddfa = AFDD(
direct_tree, direct_reader.GetSymbols(), r)
ddfa_regex = ddfa.EvalRegex()
ddfa.GraphDFA()


#simulacion respecto a la cadena
# simulacion_afn(afn,cadena,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved)-1][1])
# simulacion_afd(afd,cadena,afn_recieved[1][0][0],afn_recieved[1][len(afn_recieved)-1][1])
