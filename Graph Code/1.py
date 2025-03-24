import matplotlib.pyplot as plt

# Data for cybersecurity threats
threats = ['Malware', 'Phishing', 'Ransomware', 'Insider Threats', 'DDoS Attacks']
percentage = [30, 25, 20, 15, 10]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(percentage, labels=threats, autopct='%1.1f%%', startangle=140, colors=['red', 'blue', 'green', 'orange', 'purple'])
plt.title("Cybersecurity Threat Landscape")
plt.show()
