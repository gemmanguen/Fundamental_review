"""
@FrankNGUEN
@5/9/2022

https://quantumcomputinguk.org/code-repository

"""
#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------
def init_backend(my_api):
    print('Init IBM and backend...')
    IBMQ.enable_account(my_api)                            # Get this from your IBM Q account
    provider = IBMQ.get_provider(hub='ibm-q')
    backend  = provider.get_backend('ibmq_qasm_simulator') # Set device to IBMs quantum simulator
    print('Provider: ',backend)
    return backend
my_api           = 'e3d3e728dadda685b54a00e7d7c16dd79dd86248800ca4341bfc1cce7014e45aaf95636d16c6f43e3d1c43b4aac07bd9efbd0bee62226ae0eac26c2435bb6166'
backend          = init_backend(my_api)
#------------------------------------------------------------------------------
def init_circuits():
    print('Init circuits...')
    q        = QuantumRegister(1,'q')                  # Initialise quantum register
    c        = ClassicalRegister(1,'c')                # Initialise classical register
    circuit  = QuantumCircuit(q,c)                     # Initialise circuit
    circuit.h(q[0])                                    # Put Qubit 0 in to superposition using hadamard gate 
    circuit.measure(q,c)                               # Measure qubit
    print(circuit)
    circuit.draw()                                     # Draw the circuit
    return circuit
#------------------------------------------------------------------------------
def init_jobs(circuit, backend):
    print('Executing Job...')
    job      = execute(circuit, backend, shots=1024)   # Execute job and run program 1024 times 
    result   = job.result()                            # Get result
    counts   = result.get_counts(circuit)              # Count the number of measurements for each state
    print('RESULT: ',counts)                           # Print result 
    # Plot a histogram
    plot_histogram(counts)
#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------
def TOP():
    print('\nHallo-world Program')
    print('--------------------------')
    print('Programmed by FrankNGUEN for Quantum Computing\n')
    circuit          = init_circuits()
    init_jobs(circuit, backend)         
#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------
if __name__=='__main__':
    TOP()
#------------------------------------------------------------------------------
