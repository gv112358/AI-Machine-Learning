import matplotlib.pyplot as plt
	
 
	
with open('es02temperatures.txt', 'r') as file:
	
    lines = file.readlines()
	
 
	
celsius_temperatures = [float(line.strip()) for line in lines]
	
fahrenheit_temperatures = [(celsius * 9/5) + 32 for celsius in celsius_temperatures]
	
data = list(zip(celsius_temperatures, fahrenheit_temperatures))
	
 
	
plt.plot(data)
	
plt.xlabel('Time')
	
plt.ylabel('Temperature')
	
plt.title('Temperature Readings')
	
plt.legend(['Celsius', 'Fahrenheit'])
	
plt.show()
	
 
	
"""
	
I dati
	
23.5
24.0
24.5
25.0
25.5
	
"""