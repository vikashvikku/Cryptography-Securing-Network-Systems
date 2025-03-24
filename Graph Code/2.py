import numpy as np
import matplotlib.pyplot as plt

# Data
methods = ["Traditional IDS", "AI-Based IDS"]
efficiency = [65, 92]  # Percentage detection efficiency

# Create bar chart
plt.figure(figsize=(8, 6))
plt.bar(methods, efficiency, color=['gray', 'green'])
plt.xlabel("Detection Method")
plt.ylabel("Detection Efficiency (%)")
plt.title("AI vs Traditional Threat Detection Efficiency")
plt.ylim(0, 100)

# Show values
for i, v in enumerate(efficiency):
    plt.text(i, v + 2, str(v) + "%", ha='center')

plt.show()
