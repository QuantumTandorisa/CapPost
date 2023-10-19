CapPost es una herramienta que te permite analizar y visualizar datos de tus publicaciones de Instagram. Con esta herramienta, puedes obtener información valiosa sobre tus publicaciones, interacciones con otros usuarios, preferencias de tus seguidores y mucho más.

## Características 

- Análisis de Sentimientos: CapPost utiliza el analizador de sentimientos de NLTK para determinar la polaridad de tus subtítulos.

- Extracción de Hashtags: Extrae y muestra los hashtags utilizados en tus publicaciones.

- Interacciones con Otros Usuarios: Muestra las interacciones con otros usuarios, como menciones y comentarios.

- Análisis de la Actividad por Día y Hora: Visualiza cuándo son más activas tus publicaciones.

- Análisis de la Evolución de Seguidores: Comprende cómo evolucionan tus seguidores con el tiempo.

- Nube de Palabras Clave: Genera una nube de palabras clave basada en tus publicaciones.

## Requisitos

- Python 3
- Bibliotecas Python: nltk, spacy, scikit-learn, matplotlib, wordcloud, pandas, seaborn

## Uso

-  Clona este repositorio o descarga el archivo `CapPost.py`.
-  Ejecuta el programa en tu entorno Python.
-  Proporciona tu User ID y Access Token de Instagram.

## Configuración de API

-  Actualiza todas las bibliotecas en tu entorno virtual ejecutando los siguientes comandos:
    
    `pip install --upgrade pip`
    
    `pip freeze --local | grep -v '^-e' | cut -d = -f 1 | xargs -n1 pip install -U`

-  Limpia archivos pyc ejecutando el siguiente comando:
    
    `find /home/quantum/portfolio/CapPost/CapPost -name '*.pyc' -exec rm -f {} ;`

-  Descarga el modelo en inglés para spaCy ejecutando:

    `python -m spacy download en_core_web_sm`

-  Descarga los recursos necesarios para NLTK. Ejecuta el siguiente código en Python:
    
    `python`
    
    `import nltk`
    
    `nltk.download('punkt')`

-  Ejecuta el programa en tu entorno Python:

    `python3 CapPost.py`

-  Proporciona tu User ID y Access Token de Instagram.

Observa los resultados generados por CapPost, que incluyen tablas, gráficos y visualizaciones.
