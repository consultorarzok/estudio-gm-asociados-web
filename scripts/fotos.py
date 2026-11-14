"""Procesa las fotos del estudio: recorte, luz/color parejos, nitidez, WebP en 2 tamaños."""
import cv2, numpy as np
from PIL import Image, ImageEnhance, ImageFilter
SRC='/root/gm-placas-nov/fotos/'; OUT='/root/estudio-gm-web/img/'

def grade(im, warm=1.0):
    a=np.asarray(im).astype(np.uint8)
    a=cv2.fastNlMeansDenoisingColored(a,None,2,2,5,13)          # ruido suave de JPG
    lab=cv2.cvtColor(a,cv2.COLOR_RGB2LAB); l,aa,bb=cv2.split(lab)
    l=cv2.createCLAHE(clipLimit=1.05,tileGridSize=(4,4)).apply(l)  # luz pareja
    bb=cv2.add(bb,np.full_like(bb,int(2*warm)))                     # toque cálido uniforme
    a=cv2.cvtColor(cv2.merge([l,aa,bb]),cv2.COLOR_LAB2RGB)
    im=Image.fromarray(a)
    im=ImageEnhance.Color(im).enhance(1.04); im=ImageEnhance.Contrast(im).enhance(1.03)
    return im

def save(im, name, widths):
    for w in widths:
        r=im.resize((w,round(w*im.height/im.width)),Image.LANCZOS)
        r=r.filter(ImageFilter.UnsharpMask(radius=1.2,percent=55 if w>im.width*0.8 else 35,threshold=2))
        r.save(f'{OUT}{name}-{w}.webp',quality=80,method=6)
    print(name, im.size, widths)

def crop45(src, cx, top, wfrac):
    im=Image.open(SRC+src).convert('RGB'); W,H=im.size
    w=int(W*wfrac); h=int(w*5/4)
    if h>H-top: h=H-top; w=int(h*4/5)
    x=max(0,min(W-w,int(cx*W-w/2)))
    return im.crop((x,top,x+w,top+h))

# retratos 4:5
save(grade(crop45('fer3.jpg',0.52,0,0.66)),'dra-tapia',[480,900])
save(grade(crop45('l.jpg',0.52,0,0.63)),'dra-gutierrez',[480,900])
save(grade(crop45('carla3.jpg',0.5,0,0.9)),'dra-morales',[480,900])
# grupo y oficina
g=Image.open(SRC+'w2.jpg').convert('RGB'); save(grade(g),'equipo',[700,1200,1800])
save(grade(Image.open(SRC+'g3.jpg').convert('RGB')),'oficina-roja',[700,1200])
save(grade(Image.open(SRC+'g2.jpg').convert('RGB').crop((0,0,2350,1600))),'reunion',[700,1200])
save(grade(Image.open(SRC+'fer4.jpg').convert('RGB')),'estudio-lectura',[700,1200])
# fondo del hero: las tres trabajando (elegida por Zeta)
save(grade(Image.open(SRC+'g1.jpg').convert('RGB')),'portada-equipo',[900,1600,2400])
# recortes cuadrados centrados en la cara, para los retratos circulares (abogada sola)
def circ(src, box, name):
    im=grade(Image.open(SRC+src).convert('RGB').crop(box))
    save(im, name, [400, 760])
circ('fer3.jpg',(380,0,960,580),'circ-tapia')
circ('l.jpg',(287,0,887,600),'circ-gutierrez')
circ('carla3.jpg',(191,0,1891,1700),'circ-morales')
circ('fer4.jpg',(430,0,1430,1000),'circ-tapia-lectura')
