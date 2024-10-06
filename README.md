## KSN: Modelado y simulación de conocimiento mediante aprendizaje automático en redes basadas en NFV/SDN.

Este modelo tiene como objetivo el aprendizaje automático, identificar los errores y aprender de ellos, de manera que en el futuro estos se solucionen.
Implica crear modelos matemáticos y simulaciones que representan la red en diferentes escenarios.
El modelo KSN (Knowledge Simulation Network) se centra en el modelado y la simulación de conocimiento mediante el uso de aprendizaje automático en redes basadas en NFV (Network Functions Virtualization) y SDN (Software-Defined Networking). 

<p>Este enfoque permite la creación de redes más inteligentes y eficientes, aprovechando algoritmos de aprendizaje automático para optimizar la gestión y operación de las redes.</p>

## La ecuación del modelo contiene: 


<p>K: Conocimiento simulado que se pueda obtener.</p>
<p>D: Datos de entrada.</p> 
<p>A: Acciones posibles que el sistema que puede tomar.</p>
<p>M: Modelo de aprendizaje basado en predecir resultados basados en D y A.</p>
<p>e: error o variabilidad en el modelo.</p>


## El modelo KSN puede aplicarse a escenarios de la vida cotidiana de varias maneras:

Gestión del tráfico: Imagina una ciudad inteligente donde los semáforos se ajusten automáticamente según el flujo de tráfico en tiempo real. El modelo KSN utilizaría datos históricos y en tiempo real para optimizar las rutas.

## Se valida utilizando Validación Cruzada (Cross-Validation)
K-Fold Cross-Validation: Divide los datos en k subconjuntos (folds). El modelo se entrena con k-1 subconjuntos y se valida con el subconjunto restante. Este proceso se repite k veces, utilizando cada subconjunto como conjunto de validación una vez.

## Librerias a instalar
En *visual estudio Code* necesitamos las siguientes librerias para que nuestro codigo funcione correctamente:

<p>import numpy as np </p>
<p>import matplotlib.pyplot as plt </p>
<p>from sklearn.model_selection import train_test_split </p>
<p>from sklearn.neighbors import KNeighborsClassifier </p>
<p>from sklearn.metrics import accuracy_score </p>
<p>from sklearn.preprocessing import StandardScaler </p>
