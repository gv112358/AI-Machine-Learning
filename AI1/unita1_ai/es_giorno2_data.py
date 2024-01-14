import matplotlib.pyplot as plt
	
import pandas as pd
	
 
	
data = pd.read_csv('es01data.csv')
	
plt.scatter(data['x'], data['y'])
	
plt.show()
	
 
	
 
	
"""
	
I dati
	
x,y
	
1,2
	
2,4
	
3,6
	
4,8
	
5,10
	
"""