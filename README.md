README

Este script de Python te permite analizar las publicaciones recientes de un usuario de Instagram. Realiza diversos análisis de los datos obtenidos de las publicaciones, como el análisis desentimientos, el conteo de likes, el análisis de hashtags, la detección de idioma, la extracción de entidades, entre otros. Además, genera visualizaciones gráficas para representar los resultados obtenidos.

Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas antes de ejecutar el script:

    requests
    nltk
    spacy
    pandas
    seaborn
    langdetect
    wordcloud
    sklearn
    matplotlib

Puedes instalar estas bibliotecas usando pip con el siguiente comando:

    pip install requests nltk spacy pandas seaborn langdetect wordcloud scikit-learn matplotlib

Además, necesitarás descargar los datos adicionales requeridos por NLTK y spaCy. Para ello, puedes ejecutar los siguientes comandos en tu entorno de Python:

python

    import nltk
    nltk.download('punkt')

    import spacy
    spacy.download('es_core_news_sm')

Uso

Sigue los pasos a continuación para utilizar el script:

Reemplaza las siguientes variables con tus propios valores en el código:

python

    usuario_id = "TU_USUARIO_ID"  # Reemplaza con tu usuario ID
    access_token = "TU_ACCESS_TOKEN"  # Reemplaza con tu token de acceso

Ejecuta el script en tu entorno de Python.
El script recuperará las publicaciones recientes del usuario de Instagram especificado y realizará análisis en base a esos datos.
Los resultados se imprimirán en la consola y se mostrarán visualizaciones gráficas, como gráficos de barras y nubes de palabras.

Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de enviar tus pull requests. Estoy abierto a mejoras y sugerencias para hacer que el script sea más robusto y útil.
