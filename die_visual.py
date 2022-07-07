from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

# Utworzenie kości typu D6
die = Die()

# Wykonanie pewnej liczby rzutów ii umeiszczenie wyników na liśćie.
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

results = [die.roll() for roll_num in range(1000)]

# Analiza wyników
# frequencies = []
# for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in range (1, die.num_sides+1)]

# Wizualizacja wyników
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik'}    # To kreacja konfiga typu slownik dla osi X
y_axis_config = {'title': 'Częstotliwość występowania wartości'}  # To kreacja konfiga typu slownik dla osi Y
my_layout = Layout(title='Wynik rzucania pojedynczą kością D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)
# ^ Tworzenie layouta czyli wygladu dla danych

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  # Tworzenie grafu

print(frequencies)

