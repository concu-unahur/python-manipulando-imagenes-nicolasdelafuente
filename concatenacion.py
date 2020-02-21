import numpy as np
from PIL import Image
from archivos import leer_imagen, escribir_imagen
from api import PixabayAPI


def concatenar_horizontal(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.hstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

def concatenar_vertical(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.vstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))






def concatenar(lista_imagenes):
  imagen1 = leer_imagen(lista_imagenes[0])
  imagen2 = leer_imagen(lista_imagenes[1])
  escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([imagen1, imagen2])) 
  
  #lista[i:i+2]}}
  # for i in range(3):
  #   print(i)
  #   escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([lista_imagenes[i], lista_imagenes[i+1]]))    
  #   #escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([lista_imagenes[i], lista_imagenes[i+1]]))    
  #   i = i+1