#Put this inside the automata-lib folder and run
from automata.fa.dfa import DFA
import re

"""
A : whenGreenFlagClicked
B : goToXY
C : show
D : point in direction
E : move steps 
F : forever
G : if
H : touching step
I : switch backdrop to level2
"""
#level1
#Label each opcode with A,B etc.
dfa1 = DFA(
    states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7','q8'},
    input_symbols={'A', 'B','C','D','E','F','G','H','I'},
    transitions={
        'q0': {'A': 'q0', 'B': 'q1','C':'q8','D':'q8','E':'q8','F':'q8','G':'q8','H':'q8','I':'q8'},
        'q1': {'C': 'q2', 'A':'q8','B':'q8','D':'q8','E':'q8','G':'q8','H':'q8','I':'q8','F':'q8'},
        'q2': {'D': 'q3' ,'C':'q8','A':'q8','E':'q8','F':'q8','G':'q8','H':'q8','I':'q8','B':'q8'},
        'q3': {'E':'q4','C':'q8','D':'q8','A':'q8','F':'q8','G':'q8','H':'q8','I':'q8','B':'q8'},
        'q4': {'D':'q3','F':'q5','C':'q8','B':'q8','E':'q8','A':'q8','G':'q8','H':'q8','I':'q8'},
        'q5': {'G':'q6','C':'q8','D':'q8','E':'q8','F':'q8','A':'q8','H':'q8','I':'q8','B':'q8'},
        'q6': {'H':'q7','C':'q8','D':'q8','E':'q8','F':'q8','G':'q8','A':'q8','I':'q8','B':'q8'},
        'q7': {'I':'q7','C':'q8','D':'q8','E':'q8','F':'q8','G':'q8','H':'q8','A':'q8','B':'q8'},
	'q8': {'I':'q8','C':'q8','D':'q8','E':'q8','F':'q8','G':'q8','H':'q8','A':'q8','B':'q8'}
    },
    initial_state='q0',
    final_states={'q7','q8'}
)
'''
stopped_state1 = dfa1.validate_input('ABCDEFGHI')
if(stopped_state1 != 'q8'):
	print("DFA accepted!")
else:
	print("DFA Rejected!")
'''
	
"""
a - when backdrop switches to level2
b - show
c - goto xy
d - forever
1 - [up,down,left,right,stop]
0 - [if any of the above repeat]
"""
#level2
dfa2 = DFA(
    states={'q0', 'q1', 'q2','q3','q4','q5'},
    input_symbols={'a','b','c','d','0', '1'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q1','c':'q5','d':'q5','0':'q5','1':'q5'},
        'q1': {'c': 'q2','a':'q5','b':'q5','0':'q5','1':'q5','d':'q5' },
        'q2': {'d': 'q3', 'c':'q5','a':'q5','0':'q5','1':'q5','b':'q5'},
	'q3': {'1':'q4','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'},
	'q4': {'1':'q4','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'},
	'q5': {'1':'q5','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'}
    },
    initial_state='q0',
    final_states={'q4','q5'}
)
#gives the state at which the dfa stops. With this calculate the distance metric
'''
stopped_state2 = dfa2.validate_input('abcd0') #rejected, with abcd1 gets accepted
if(stopped_state2 != 'q5'):
	print("DFA accepted!")
else:
	print("DFA Rejected!")
'''


opcode = [];
append = 0;
if __name__ == "__main__":
    blockFile = open("blocks_output.txt", "r")
    for line in blockFile.readlines():
        if(re.search("Timestamp",line)):
            print(line);
            append = 0;
            if(len(opcode) > 0):
                print(opcode);
                stopped_state1 = dfa1.validate_input(opcode);
                if(stopped_state1 != 'q8'):
                    print("DFA accepted!");
                else:
                    print("DFA Rejected!");
            opcode = [];

        if(append != 0):
        
            if(re.search("go to x",line)):
                opcode.append("B");

            elif(re.search("show",line)):
                opcode.append("C");

            elif(re.search("point in direction",line)):
                opcode.append("D");

            elif(re.search("move ",line)):
                opcode.append("E");

            elif(re.search("forever",line)):
                opcode.append("F");

            elif(re.search("if",line)):
                opcode.append("G");

                if(re.search("< touching ",line)):
                    opcode.append("H");

            elif(re.search("switch backdrop to ",line)):
                opcode.append("I");

        else:
            if(re.search("when green flag clicked",line)):
                opcode.append("A");
                append = 1;

