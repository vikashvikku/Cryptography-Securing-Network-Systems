import matplotlib.pyplot as plt

# Years and technology adoption rates
years = [2023, 2024, 2025, 2026, 2027]
ai_security = [30, 50, 65, 80, 90]
blockchain_security = [20, 40, 55, 70, 85]
quantum_crypto = [5, 15, 30, 50, 70]

plt.figure(figsize=(8, 6))
plt.plot(years, ai_security, marker='o', label="AI Security")
plt.plot(years, blockchain_security, marker='s', label="Blockchain Security")
plt.plot(years, quantum_crypto, marker='^', label="Quantum Cryptography")

plt.xlabel("Year")
plt.ylabel("Adoption Rate (%)")
plt.title("Projected Adoption of Cybersecurity Technologies")
plt.legend()
plt.grid(True)
plt.show()
