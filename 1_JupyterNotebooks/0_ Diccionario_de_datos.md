# 📚 Diccionario de datos para el proyecto:

#### **🤵user_reviews.json** :

Contiene comentarios de usuarios sobre juegos, recomendaciones, emoticones de gracioso y estadísticas de utilidad.

* Variables:
  * **user_id** 👤: Identificador único del usuario.
  * **user_url** 🔗: URL del perfil del usuario en Steam Community.
  * **reviews** 📝: Lista de diccionarios con revisiones, cada uno con:
    * ****reviews**_funny** 😄: Indica si contiene emoticones de gracioso.
    * ****reviews**_posted** 📅: Fecha de publicación del comentario.
    * ****reviews**_last_edited** 📅: Fecha de la última edición.
    * ****reviews**_item_id** 🎮: Identificador único del juego.
    * ****reviews**_helpful** 👍: Estadísticas de utilidad del comentario.
    * ****reviews**_recommend** 👍👎: Recomendación del juego por el usuario.
    * ****reviews**_review** 💬: Comentario sobre el juego.

#### **📦 user_items.json** :

* Contiene información sobre los juegos jugados por usuarios y el tiempo acumulado.
* Variables:
  * **user_id** 👤: Identificador único del usuario.
  * **items_count** 📊: Cantidad de juegos consumidos por el usuario.
  * **steam_id** 🔢: Número único de la plataforma.
  * **user_url** 🔗: URL del perfil del usuario.
  * **items** 📦: Lista de diccionarios de los juegos consumidos, cada uno con:
    * **item_id** 🎮: Identificador único del juego.
    * **item_name** 🎮: Nombre del juego.
    * **playtime_forever** ⏰: Tiempo acumulado de juego.
    * **playtime_2weeks** ⏰: Tiempo acumulado en las últimas dos semanas.

#### **🎮 steam_games.json** :

Contiene datos relacionados con los juegos.

* Variables:
  * **publisher** 📤: Empresa publicadora del contenido.
  * **genres** 🎮: Género del juego (lista de géneros).
  * **app_name** 📜: Nombre del juego.
  * **title** 🏆: Título del juego.
  * **url** 🔗: URL del juego.
  * **release_date** 📅: Fecha de lanzamiento (formato: 2018-01-04).
  * **tags** 🏷️: Etiquetas del contenido (lista de etiquetas).
  * **reviews_url** 🔍: URL de reseñas del juego.
  * **specs** 📝: Especificaciones del juego (lista de cadenas de texto).
  * **price** 💰: Precio del juego.
  * **early_access** 🚀: Acceso temprano (True/False).
  * **id** 🔢: Identificador único del contenido.
  * **developer** 👨‍💻: Desarrollador del contenido.
