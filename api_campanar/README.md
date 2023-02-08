# api_campanar

Api creada para gestionar datos aplicacion web de una asociación de vecinos de valencia.

Bases de datos SQL, Api en Django, y puesta en producción a taves de railway.

La api gestiona la conexion a la base de datos y ademas contiene dos modelos de Machine Learning, que clasifican los datos o realizan analisis de sentimiento (NPL).

La base de batos SQL recopila informacion de peticiones, noticias y actividades asociadas al barrio.

Modelo de Machine Leraning que clasifica las noticias en categorias. Modelo compuesto por CountVectorizer() + RandomForst().

Modelo de Machine Leraning que hace un analisis de sentimiento de las peticiones y comentarios recibidos en la app. Modelo compuesto por CountVectorizer() + AdaBoost().