from matplotlib_venn import venn2
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
venn = venn2(subsets = (5, 5, 3), set_labels=('Existing Security Measures', 'Unresolved Threats'))
plt.title("Research Gap in Cybersecurity")
plt.show()
