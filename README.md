# AWS + Quantum Platforms Starter

This repo shows:
1) **SageMaker** training & deployment skeleton (PyTorch).
2) Side-by-side **Qiskit / Cirq / Braket** examples.
3) A small **gate-count & depth** comparison across "superconducting-like" (IBM basis), "ion-like" (XX), and "neutral-atom-like" (CZ) settings.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 1) Run local quantum examples
```bash
python qiskit_cirq_braket/qiskit_example.py
python qiskit_cirq_braket/cirq_example.py
python qiskit_cirq_braket/braket_example.py
python report/compare_gatecounts.py
```

### 2) SageMaker (outline)
- Edit `sagemaker/src/train.py`.
- Set your role & bucket in `sagemaker/deploy_stub.py` (or env vars `SM_ROLE_ARN`, `SM_BUCKET`).
- Run from a SageMaker Notebook or a local env with AWS creds.
