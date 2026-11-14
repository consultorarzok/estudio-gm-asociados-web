# DESIGN — Estudio Jurídico GM & Asociados (web)

Mundo visual: **editorial elegante** sobre el manual de marca GM (aprobado por Zeta el 14/11/2026).

## Tokens
| Token | Valor | Uso |
|---|---|---|
| `--bordo` | #841E25 | marca, hero, bandas de impacto, títulos sobre crema |
| `--bordo-p` | #682018 | hover, profundidad, velo sobre fotos |
| `--oscuro` | #261F1C | sección "desde el exterior", pie |
| `--dorado` | #C7A254 | acento: filetes, aros, botones. Nunca masa de texto |
| `--dorado-t` | #7A5C1C | dorado legible sobre crema (texto chico) |
| `--crema` | #F5F0E7 | fondo base |
| `--papel` | #FBF8F2 | fondo alterno claro |
| `--carbon` | #3C3630 | texto sobre crema |

Tipografía: **Poppins** autoalojada (300/400/500/600/700). Display 600 con tracking -0.03em; bajadas en 300.

## Recurso firma
El **doble aro del sello** del logo: marcos en arco para las fotos con un filete dorado que se dibuja, y un sello giratorio con texto circular. Es el único elemento decorativo; todo lo demás es tipografía y foto.

## Movimiento
- Un solo momento coreografiado: apertura del hero (el aro dorado se dibuja, la foto se revela, el título sube).
- Manifiesto con palabras que se encienden al hacer scroll.
- Revelado de fotos de las abogadas al entrar en pantalla.
- Todo respeta `prefers-reduced-motion` y el contenido es visible sin JavaScript.

## Reglas
- Texto sobre foto ⇒ velo parejo (manual). Sin degradés, sin brillos.
- Sin eyebrows/kickers, sin tarjetas iguales en grilla, sin emojis como íconos.
- Copy: voseo, sin "gratis", sin datos legales inventados, sin prometer resultados.
