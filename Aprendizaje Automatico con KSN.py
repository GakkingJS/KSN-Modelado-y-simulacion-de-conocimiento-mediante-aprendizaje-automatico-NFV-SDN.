import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Generar datos entre las clases
ancho_banda_clase_0 = np.random.randint(50, 200, 250)
latencia_clase_0 = np.random.randint(150, 200, 250)

ancho_banda_clase_1 = np.random.randint(200, 500, 250)
latencia_clase_1 = np.random.randint(50, 150, 250)

ancho_banda = np.concatenate([ancho_banda_clase_0, ancho_banda_clase_1])
latencia = np.concatenate([latencia_clase_0, latencia_clase_1])
etiquetas = np.concatenate([np.zeros(250), np.ones(250)])  # Clase 0 y Clase 1

# Combinamos ancho de banda y latencia para usarlo como entrada
X = np.column_stack((ancho_banda, latencia))
y = etiquetas

# Dividimos los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# los datos para que estén en el mismo rango
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definimos el modelo (KNN)
knn = KNeighborsClassifier(n_neighbors=6)

# Entrenamos el modelo con los datos 
knn.fit(X_train, y_train)

# Hacemos predicciones con los datos de prueba
y_pred = knn.predict(X_test)

# Calculamos la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Graficar los datos de entrenamiento
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], color='blue', label='Clase 0 (Tráfico mayor latencia)')
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], color='red', label='Clase 1 (Tráfico menor latencia)')

# Título
plt.title('Clasificación de Tráfico en Red con KNN')
plt.xlabel('Ancho de Banda')
plt.ylabel('Latencia')

plt.legend()
plt.grid(True)

plt.show()
