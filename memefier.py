# Importar dependencias
import random

# Posibles opciones para saber si una letra se debe escribir en mayúsculas
CHOICES = [0, 1]

def memefy(text):
  memefied_text = []

  for letter in text:
    # Elegir si la letra se debe pasar a mayúsculas
    if random.choice(CHOICES) == 1:
      memefied_text.append(letter.upper())
    else:
      memefied_text.append(letter.lower())
    
  return ''.join(memefied_text)