import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

# Dataset de salud mental de estudiantes
path = kagglehub.dataset_download("shariful07/student-mental-health")
csv_path = path + "/Student Mental health.csv"

df = pd.read_csv(csv_path)
df = df.dropna()

# Agrupar por curso y ansiedad
conteo = df.groupby(['What is your course?', 'Do you have Anxiety?']).size().unstack().fillna(0)

# Crear gráfico
conteo.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Ansiedad por curso")
plt.xlabel("Curso")
plt.ylabel("Cantidad de estudiantes")
plt.xticks(rotation=90)  
plt.tight_layout()
plt.savefig("grafica.png")
print("Gráfico guardado como grafica.png")