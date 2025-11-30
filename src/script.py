# Import packages
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

# Run game
def create_vault_qubit(secret_bit):
    qc = QuantumCircuit(1, 1)
    if secret_bit == 1:
        qc.x(0)  
    qc.measure(0, 0)
    return qc

def run_quantum_scan(qc):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts()
    measured_bit = int(max(counts, key=counts.get))
    return measured_bit

def play_quantum_vault_game():
    print("=== 🔐 Quantum Vault: Crack the Qubit Code ===")
    print("You are a cyber-detective in the future.")
    print("Your mission: breach a quantum-encrypted vault by guessing the correct qubit lock state.")
    print("The quantum lock is either in state |0⟩ or |1⟩. One guess. No second chances.\n")
    
    secret_bit = random.choice([0, 1])
    qc = create_vault_qubit(secret_bit)

    try:
        user_guess = int(input("💡 Enter your qubit guess (0 or 1): "))
        if user_guess not in [0, 1]:
            raise ValueError
    except ValueError:
        print("❌ Invalid input. Mission failed.")
        return

    print("\n🛰️ Scanning quantum lock...")
    measured_bit = run_quantum_scan(qc)

    print(f"\n🔎 Quantum lock result: {measured_bit}")
    print(f"🎯 Your guess: {user_guess}")

    if user_guess == measured_bit:
        print("✅ Access granted! The vault is open. Intel secured.")
    else:
        print("🚫 Access denied. Quantum lock resisted your attempt. Try again next time.")

if __name__ == "__main__":
    play_quantum_vault_game()
