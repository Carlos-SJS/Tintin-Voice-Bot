# Tintin-Voice-Bot
Este es un script hecho en python que toma un text como input, y una serie de grabaciones, y convierte dicho texto a audio utilizando las grabaciones.

Si quieres usar este script, deberas crear dentro de la carpeta sound las sub carpetas:
  - letters:
    Debe contener la pronunciación/sonido correspondiente a cada letra del abecedario incluyendo la ñ
  - silaba_2l:
    Debe contener las sílabas descritas en el archivo "silabas 2ch.txt" (No es nescesario tener todas pero es recomendable)
  - silaba_3l:
    Debe contener las sílabas descritas en el archivo "silabas 3ch.txt" (No es nescesario tener todas pero es recomendable)
  - silaba_4l:
    Debe contener las sílabas descritas en el archivo "silabas 4ch.txt" (No es nescesario tener todas pero es recomendable)
  - single_letter:
    Debe contener la pronunciación de todas las letras del abecedario, ej: Ñ - "eñe", R - "erre"
  - words:
    Puede contener de forma opcional palabras comunes, entre más palabaras contenga esta carpeta, el audio generado sonará más natural y fluido
 
 !Este script sólo funciona correctamente para texto en español, ya que esta creado con las reglas gramaticales del español en mente, aunque utilizando palabras en la carpeta "sound/words" en inglés, es posible lograr un sonido natural.
