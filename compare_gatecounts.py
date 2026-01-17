from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import pandas as pd

def base_circuit(n=5):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    return qc

qc = base_circuit(5)
backend = AerSimulator()

t_ibm = transpile(qc, backend, basis_gates=['rz','sx','x','cx'], optimization_level=3,
                  layout_method='sabre', routing_method='sabre')
ops_ibm = t_ibm.count_ops()
cx_ibm = int(ops_ibm.get('cx', 0)); depth_ibm = t_ibm.depth()

# Proxies for ion-like and neutral-atom-like counts (no synthesis here)
cx_ion = qc.count_ops().get('cx', 0)
depth_ion = qc.depth()
cx_na = qc.count_ops().get('cx', 0)
depth_na = qc.depth()

df = pd.DataFrame([
    {"platform":"superconducting(IBM)", "two_qubit": cx_ibm, "depth": depth_ibm},
    {"platform":"ion-like(XX proxy)",  "two_qubit": cx_ion,  "depth": depth_ion},
    {"platform":"neutral-atom(CZ px)", "two_qubit": cx_na,   "depth": depth_na},
])
print(df)
