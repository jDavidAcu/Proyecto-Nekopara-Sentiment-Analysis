# 🎮 Análisis de Sentimientos del Videojuego Nekopara

Este es un proyecto académico desarrollado como parte de la materia **Ciencia de Datos**. Aplica técnicas de minería de texto y aprendizaje automático para analizar los sentimientos de los comentarios del videojuego **Nekopara**, utilizando la metodología **CRISP-DM**.

## 📌 Objetivo

Determinar el modelo de clasificación más adecuado para detectar automáticamente si un comentario es **positivo**, **negativo** o **neutro**, utilizando comentarios reales de Steam sobre el videojuego.

## 🔍 Metodología CRISP-DM

1. **Comprensión del negocio**  
   Se busca evaluar la percepción del público sobre el videojuego Nekopara mediante análisis de sentimientos.

2. **Comprensión de los datos**  
   - Los comentarios se obtienen desde Steam con un script en Python.
   - Se almacenan en un archivo `.txt`.

3. **Preparación de los datos**  
   - Se utiliza `pysentimiento` para etiquetar los comentarios como POS, NEG o NEU.
   - Se generan 3 datasets:
     - Dataset original (desbalanceado)
     - Dataset con **undersampling**
     - Dataset con **oversampling**

4. **Modelado**  
   Se entrenan 3 modelos distintos:
   - Red Neuronal (MLP)
   - Support Vector Machine (SVM)
   - Árbol de Decisión

5. **Evaluación**  
   Se comparan los modelos para ver cuál tiene mejor desempeño según el dataset utilizado.

6. **Despliegue (simulado)**  
   Se deja una función lista para analizar un nuevo comentario (solo en inglés), usando el mejor modelo.

# 🎮 Análisis de Sentimientos del Videojuego Nekopara

Este es un proyecto académico desarrollado como parte de la materia **Ciencia de Datos**. Aplica técnicas de minería de texto y aprendizaje automático para analizar los sentimientos de los comentarios del videojuego **Nekopara**, utilizando la metodología **CRISP-DM**.

## 📌 Objetivo

Determinar el modelo de clasificación más adecuado para detectar automáticamente si un comentario es **positivo**, **negativo** o **neutro**, utilizando comentarios reales de Steam sobre el videojuego.

## 🔍 Metodología CRISP-DM

1. **Comprensión del negocio**  
   Se busca evaluar la percepción del público sobre el videojuego Nekopara mediante análisis de sentimientos.

2. **Comprensión de los datos**  
   - Los comentarios se obtienen desde Steam con un script en Python.
   - Se almacenan en un archivo `.txt`.

3. **Preparación de los datos**  
   - Se utiliza `pysentimiento` para etiquetar los comentarios como POS, NEG o NEU.
   - Se generan 3 datasets:
     - Dataset original (desbalanceado)
     - Dataset con **undersampling**
     - Dataset con **oversampling**

4. **Modelado**  
   Se entrenan 3 modelos distintos:
   - Red Neuronal (MLP)
   - Support Vector Machine (SVM)
   - Árbol de Decisión

5. **Evaluación**  
   Se comparan los modelos para ver cuál tiene mejor desempeño según el dataset utilizado.

6. **Despliegue (simulado)**  
   Se deja una función lista para analizar un nuevo comentario (solo en inglés), usando el mejor modelo.

## ⚠️ Nota importante sobre los archivos de datos

> ⚠️ El archivo `clasificados_nekopara_over.csv` **no se encuentra en el repositorio** porque excedía el límite de tamaño permitido por GitHub (más de 100 MB).  
> Sin embargo, **puede ser generado fácilmente** siguiendo el cuaderno Jupyter del proyecto (`Proyecto_Final_Sentimientos_Jose_Acuña.ipynb`), donde se describe el proceso paso a paso para balancear los datos con oversampling.

## ⚙️ Requisitos

Python 3.10 o superior.  
Instala las dependencias con:

```bash
pip install -r requerimientos



