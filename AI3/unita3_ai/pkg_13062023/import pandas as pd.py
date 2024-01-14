import pandas as pd
import matplotlib.pyplot as plt

# Creazione di un DataFrame di esempio
data = {
    'colonna1': [10, 15, 7, 12, 20, 5, 8, 16],
    'colonna2': [5, 10, 15, 20, 25, 30, 35, 40],
    'colonna3': [2, 4, 6, 8, 10, 12, 14, 16],
    'colonna4': [1, 3, 5, 7, 9, 11, 13, 15]
}
df = pd.DataFrame(data)

# Creazione dei subplots per i 4 istogrammi
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Disegno degli istogrammi su ciascun subplot
df['colonna1'].plot.hist(ax=axes[0, 0], alpha=0.5)
df['colonna2'].plot.hist(ax=axes[0, 1], alpha=0.5)
df['colonna3'].plot.hist(ax=axes[1, 0], alpha=0.5)
df['colonna4'].plot.hist(ax=axes[1, 1], alpha=0.5)

# Personalizzazione degli assi e dei titoli dei subplot
axes[0, 0].set_title('Colonna 1')
axes[0, 1].set_title('Colonna 2')
axes[1, 0].set_title('Colonna 3')
axes[1, 1].set_title('Colonna 4')

# Personalizzazione dei label degli assi
for ax in axes.flat:
    ax.set_xlabel('Valore')
    ax.set_ylabel('Frequenza')

# Spaziatura tra i subplots
plt.tight_layout()

# Mostra i subplots
plt.show()
