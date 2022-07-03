import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [i**2 for i in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Zdefiniowanie tytułuy wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
ax.axis([0, 1100, 0, 1100000])

plt.show()
