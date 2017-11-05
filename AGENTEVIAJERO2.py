Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Usuario\Documents\TAREA3NOV.py ==============
MST con peso 4973 : {'f', 'g', 'h', 'j', 'e', 'd', 'b', 'a', 'i', 'c'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
<__main__.Grafo object at 0x000000A52C7CF860>
MST con peso 4973 : {'f', 'g', 'h', 'j', 'e', 'd', 'b', 'a', 'i', 'c'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
('h', 'g') 79
('g', 'h') 79
('j', 'd') 181
('d', 'j') 181
('f', 'c') 192
('c', 'f') 192
('i', 'a') 373
('a', 'i') 373
('b', 'a') 381
('a', 'b') 381
('j', 'f') 594
('f', 'j') 594
('i', 'g') 981
('g', 'i') 981
('j', 'h') 1094
('h', 'j') 1094
('f', 'e') 1098
('e', 'f') 1098
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
j h 1094
h g 79
g i 981
i a 373
a b 381
b f 2818
f c 192
c e 1284
e d 1377
d j 181
costo 8760
b a 381
a i 373
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d b 2131
costo 8486
b a 381
a i 373
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d b 2131
costo 8486
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d i 1753
i a 373
a b 381
b g 1733
costo 8860
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d a 2015
a b 381
b i 753
costo 8750
j h 1094
h g 79
g i 981
i a 373
a b 381
b f 2818
f c 192
c e 1284
e d 1377
d j 181
costo 8760
j h 1094
h g 79
g i 981
i a 373
a b 381
b f 2818
f c 192
c e 1284
e d 1377
d j 181
costo 8760
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d g 1240
g i 981
i a 373
a b 381
b h 1758
costo 9274
c f 192
f j 594
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
e c 1284
costo 8486
b a 381
a i 373
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d b 2131
costo 8486
['j', 'd', 'f', 'c', 'e', 'h', 'g', 'i', 'a', 'b']
j d 181
d f 702
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b j 2275
vmc costo 7800
72.97390175652546
minimo exacto 7477 ['a', 'b', 'd', 'j', 'c', 'f', 'e', 'h', 'g', 'i']
>>> 
============== RESTART: C:\Users\Usuario\Documents\TAREA3NOV.py ==============
MST con peso 4973 : {'j', 'g', 'c', 'f', 'b', 'i', 'a', 'h', 'd', 'e'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
<__main__.Grafo object at 0x0000007E7CFC7C88>
MST con peso 4973 : {'j', 'g', 'c', 'f', 'b', 'i', 'a', 'h', 'd', 'e'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
('h', 'g') 79
('g', 'h') 79
('j', 'd') 181
('d', 'j') 181
('f', 'c') 192
('c', 'f') 192
('i', 'a') 373
('a', 'i') 373
('b', 'a') 381
('a', 'b') 381
('j', 'f') 594
('f', 'j') 594
('i', 'g') 981
('g', 'i') 981
('j', 'h') 1094
('h', 'j') 1094
('f', 'e') 1098
('e', 'f') 1098
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
g h 79
h j 1094
j f 594
f e 1098
e c 1284
c d 789
d i 1753
i a 373
a b 381
b g 1733
costo 9178
d j 181
j h 1094
h g 79
g i 981
i a 373
a b 381
b f 2818
f e 1098
e c 1284
c d 789
costo 9078
e f 1098
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
costo 8415
f e 1098
e c 1284
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d f 702
costo 8832
e f 1098
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
costo 8415
g h 79
h j 1094
j f 594
f e 1098
e c 1284
c d 789
d i 1753
i a 373
a b 381
b g 1733
costo 9178
b a 381
a i 373
i g 981
g h 79
h j 1094
j f 594
f e 1098
e c 1284
c d 789
d b 2131
costo 8804
h g 79
g i 981
i a 373
a b 381
b j 2275
j f 594
f e 1098
e c 1284
c d 789
d h 1161
costo 9015
i a 373
a b 381
b g 1733
g h 79
h j 1094
j f 594
f e 1098
e c 1284
c d 789
d i 1753
costo 9178
c f 192
f e 1098
e j 1197
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d c 789
costo 8315
['e', 'f', 'c', 'j', 'd', 'h', 'g', 'i', 'a', 'b']
e f 1098
f c 192
c j 709
j d 181
d h 1161
h g 79
g i 981
i a 373
a b 381
b e 3113
vmc costo 8268
71.04999652860579
minimo exacto 7477 ['a', 'b', 'd', 'j', 'c', 'f', 'e', 'h', 'g', 'i']
>>> 
============== RESTART: C:\Users\Usuario\Documents\TAREA3NOV.py ==============
MST con peso 4973 : {'g', 'f', 'c', 'e', 'h', 'i', 'a', 'd', 'j', 'b'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
<__main__.Grafo object at 0x0000002A3A1DF898>
MST con peso 4973 : {'g', 'f', 'c', 'e', 'h', 'i', 'a', 'd', 'j', 'b'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
('h', 'g') 79
('g', 'h') 79
('j', 'd') 181
('d', 'j') 181
('f', 'c') 192
('c', 'f') 192
('i', 'a') 373
('a', 'i') 373
('b', 'a') 381
('a', 'b') 381
('j', 'f') 594
('f', 'j') 594
('i', 'g') 981
('g', 'i') 981
('j', 'h') 1094
('h', 'j') 1094
('f', 'e') 1098
('e', 'f') 1098
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
d j 181
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
costo 7548
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
d j 181
costo 7548
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
e f 1098
costo 8415
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
e f 1098
costo 8415
g i 981
i a 373
a b 381
b h 1758
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d g 1240
costo 9274
a b 381
b i 753
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d a 2015
costo 8750
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d a 2015
a b 381
b i 753
costo 8750
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
d j 181
costo 7548
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
e f 1098
costo 8415
f c 192
c j 709
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d e 1377
e f 1098
costo 8415
['i', 'a', 'b', 'g', 'h', 'j', 'd', 'f', 'c', 'e']
i a 373
a b 381
b g 1733
g h 79
h j 1094
j d 181
d f 702
f c 192
c e 1284
e i 2360
vmc costo 8379
69.89774238632694
minimo exacto 7477 ['a', 'b', 'd', 'j', 'c', 'f', 'e', 'h', 'g', 'i']
>>> 
============== RESTART: C:\Users\Usuario\Documents\TAREA3NOV.py ==============
MST con peso 4973 : {'e', 'g', 'h', 'i', 'j', 'b', 'f', 'a', 'd', 'c'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
<__main__.Grafo object at 0x000000253F967C50>
MST con peso 4973 : {'e', 'g', 'h', 'i', 'j', 'b', 'f', 'a', 'd', 'c'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
('h', 'g') 79
('g', 'h') 79
('j', 'd') 181
('d', 'j') 181
('f', 'c') 192
('c', 'f') 192
('i', 'a') 373
('a', 'i') 373
('b', 'a') 381
('a', 'b') 381
('j', 'f') 594
('f', 'j') 594
('i', 'g') 981
('g', 'i') 981
('j', 'h') 1094
('h', 'j') 1094
('f', 'e') 1098
('e', 'f') 1098
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d g 1240
g i 981
i a 373
a b 381
b h 1758
costo 9274
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
d j 181
costo 7548
f j 594
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d c 789
c e 1284
e f 1098
costo 8804
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d g 1240
g i 981
i a 373
a b 381
b h 1758
costo 9274
d j 181
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
costo 7548
a i 373
i g 981
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d b 2131
b a 381
costo 8486
d j 181
j f 594
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b d 2131
costo 7548
i a 373
a b 381
b g 1733
g h 79
h j 1094
j f 594
f c 192
c e 1284
e d 1377
d i 1753
costo 8860
f j 594
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d c 789
c e 1284
e f 1098
costo 8804
e f 1098
f j 594
j h 1094
h g 79
g i 981
i a 373
a b 381
b d 2131
d c 789
c e 1284
costo 8804
['j', 'd', 'f', 'c', 'e', 'h', 'g', 'i', 'a', 'b']
j d 181
d f 702
f c 192
c e 1284
e h 1352
h g 79
g i 981
i a 373
a b 381
b j 2275
vmc costo 7800
76.58000054334865
minimo exacto 7477 ['a', 'b', 'd', 'j', 'c', 'f', 'e', 'h', 'g', 'i']
>>> 
============== RESTART: C:\Users\Usuario\Documents\TAREA3NOV.py ==============
MST con peso 4973 : {'h', 'd', 'g', 'f', 'e', 'b', 'i', 'j', 'c', 'a'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
<__main__.Grafo object at 0x00000070C696F898>
MST con peso 4973 : {'h', 'd', 'g', 'f', 'e', 'b', 'i', 'j', 'c', 'a'} 
 {('h', 'g'): 79, ('g', 'h'): 79, ('j', 'd'): 181, ('d', 'j'): 181, ('f', 'c'): 192, ('c', 'f'): 192, ('i', 'a'): 373, ('a', 'i'): 373, ('b', 'a'): 381, ('a', 'b'): 381, ('j', 'f'): 594, ('f', 'j'): 594, ('i', 'g'): 981, ('g', 'i'): 981, ('j', 'h'): 1094, ('h', 'j'): 1094, ('f', 'e'): 1098, ('e', 'f'): 1098}
('h', 'g') 79
('g', 'h') 79
('j', 'd') 181
('d', 'j') 181
('f', 'c') 192
('c', 'f') 192
('i', 'a') 373
('a', 'i') 373
('b', 'a') 381
('a', 'b') 381
('j', 'f') 594
('f', 'j') 594
('i', 'g') 981
('g', 'i') 981
('j', 'h') 1094
('h', 'j') 1094
('f', 'e') 1098
('e', 'f') 1098
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
h j 1094
j d 181
d f 702
f e 1098
e c 1284
c g 1823
g i 981
i a 373
a b 381
b h 1758
costo 9675
j d 181
d f 702
f e 1098
e c 1284
c h 1743
h g 79
g i 981
i a 373
a b 381
b j 2275
costo 9097
d j 181
j f 594
f e 1098
e c 1284
c h 1743
h g 79
g i 981
i a 373
a b 381
b d 2131
costo 8845
a i 373
i g 981
g h 79
h j 1094
j d 181
d f 702
f e 1098
e c 1284
c b 2905
b a 381
costo 9078
j d 181
d f 702
f e 1098
e c 1284
c h 1743
h g 79
g i 981
i a 373
a b 381
b j 2275
costo 9097
d j 181
j f 594
f e 1098
e c 1284
c h 1743
h g 79
g i 981
i a 373
a b 381
b d 2131
costo 8845
f j 594
j d 181
d h 1161
h g 79
g i 981
i a 373
a b 381
b e 3113
e c 1284
c f 192
costo 8339
i a 373
a b 381
b g 1733
g h 79
h j 1094
j d 181
d f 702
f e 1098
e c 1284
c i 2408
costo 9333
b a 381
a i 373
i g 981
g h 79
h j 1094
j d 181
d f 702
f e 1098
e c 1284
c b 2905
costo 9078
f j 594
j d 181
d h 1161
h g 79
g i 981
i a 373
a b 381
b e 3113
e c 1284
c f 192
costo 8339
['a', 'i', 'b', 'g', 'h', 'j', 'd', 'f', 'c', 'e']
a i 373
i b 753
b g 1733
g h 79
h j 1094
j d 181
d f 702
f c 192
c e 1284
e a 2733
vmc costo 9124
70.99341340682626
minimo exacto 7477 ['a', 'b', 'd', 'j', 'c', 'f', 'e', 'h', 'g', 'i']
>>> 
