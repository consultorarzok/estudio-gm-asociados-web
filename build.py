#!/usr/bin/env python3
"""Genera el sitio estático del Estudio Jurídico GM & Asociados.
Uso: python3 build.py
     BASE=https://www.midominio.com.ar python3 build.py   (cuando haya dominio propio)
Estilos en style.css, comportamiento en main.js, fotos en scripts/fotos.py.
"""
import os, json, html, datetime
from urllib.parse import quote

BASE = os.environ.get("BASE", "https://consultorarzok.github.io/estudio-gm-asociados-web").rstrip("/")
ROOT = os.path.dirname(os.path.abspath(__file__))
VER = datetime.datetime.now().strftime("%Y%m%d%H%M")
WA = "5493884783935"
TEL_VISIBLE = "388 478-3935"
TEL_LINK = "+543884783935"
MAIL = "asociadosestudiogm@gmail.com"
IG = "https://www.instagram.com/estudio.juridicogm/"
FB = "https://www.facebook.com/estudio.gm.jujuy"
HOY = datetime.date.today().isoformat()

def wa(msg): return f"https://wa.me/{WA}?text={quote(msg)}"
def esc(s): return html.escape(s, quote=True)

WA_GENERAL = wa("Hola, quisiera hacer una consulta con el Estudio GM & Asociados.")

EQUIPO = [
    dict(nombre="Dra. Fernanda M. Tapia", corto="Dra. Tapia", mp="3742", img="dra-tapia", pos="50% 20%",
         frase="Contanos tu situación y te orientamos, con palabras simples.",
         alt="Dra. Fernanda M. Tapia, abogada en Jujuy, sonriendo en su escritorio del Estudio"),
    dict(nombre="Dra. M. Luz Gutiérrez", corto="Dra. Gutiérrez", mp="3544", img="dra-gutierrez", pos="50% 12%",
         frase="Te explicamos cada trámite de forma clara y te acompañamos.",
         alt="Dra. M. Luz Gutiérrez, abogada en Jujuy, trabajando en su computadora"),
    dict(nombre="Dra. Carla Morales", corto="Dra. Morales", mp="3769", img="dra-morales", pos="50% 18%",
         frase="Una consulta clara y cercana: te escuchamos y te orientamos.",
         alt="Dra. Carla Morales, abogada en Jujuy, en su escritorio del Estudio"),
]

AREAS = [
    dict(slug="abogados-penalistas-jujuy", nombre="Derecho penal", h1="Abogados penalistas en Jujuy",
         resumen="Defensa, denuncias, detenciones y estafas virtuales.",
         title="Abogados penalistas en Jujuy | Estudio GM & Asociados",
         desc="Defensa penal en San Salvador de Jujuy y El Carmen: denuncias, detención de un familiar, estafas virtuales y amenazas. Consultá por WhatsApp.",
         intro="Si te denunciaron, si fuiste víctima de un delito o si un familiar fue detenido, necesitás saber qué pasos seguir y con quién hablar. Te escuchamos, analizamos tu caso y te explicamos las opciones.",
         lista=["Defensa en causas penales", "Denuncias y participación como víctima o querellante", "Detención de un familiar: qué hacer y a quién acudir", "Estafas virtuales y delitos informáticos", "Amenazas e intimidaciones por WhatsApp y redes sociales", "Acuerdos y salidas alternativas del proceso penal"],
         foto="reunion", msg="Hola, quisiera consultar por un tema de derecho penal."),
    dict(slug="abogados-laboralistas-jujuy", nombre="Derecho laboral", h1="Abogados laboralistas en Jujuy",
         resumen="Despidos, trabajo no registrado y reclamos.",
         title="Abogados laboralistas en Jujuy | Estudio GM & Asociados",
         desc="Despidos, trabajo no registrado y reclamos laborales en San Salvador de Jujuy y El Carmen. Estudio GM & Asociados: consultá por WhatsApp.",
         intro="Un despido o un reclamo laboral se resuelve mejor con información clara desde el primer día. Revisamos tu situación y la documentación que tengas, y te contamos cómo se puede avanzar.",
         lista=["Despidos y liquidación final", "Trabajo no registrado o mal registrado", "Reclamos de salarios y diferencias", "Accidentes y enfermedades vinculados al trabajo", "Asesoramiento a empleadores y pequeñas empresas"],
         foto="oficina-roja", msg="Hola, quisiera consultar por un tema laboral."),
    dict(slug="abogados-de-familia-jujuy", nombre="Familia", h1="Abogados de familia en San Salvador de Jujuy",
         resumen="Divorcio, cuota alimentaria y comunicación con los hijos.",
         title="Abogados de familia en Jujuy | Estudio GM & Asociados",
         desc="Divorcio, cuota alimentaria, régimen de comunicación y cuidado de hijos en Jujuy. Abogadas de familia en San Salvador de Jujuy y El Carmen.",
         intro="Los temas de familia son delicados. Te acompañamos con respeto y te explicamos cada etapa para que puedas decidir con tranquilidad.",
         lista=["Divorcio", "Cuota alimentaria", "Régimen de comunicación con los hijos", "Cuidado personal de los hijos", "Acuerdos entre las partes y convenios"],
         foto="estudio-lectura", msg="Hola, quisiera consultar por un tema de familia."),
    dict(slug="abogados-derecho-empresarial-jujuy", nombre="Derecho empresarial", h1="Abogados de derecho empresarial en Jujuy",
         resumen="Marcas y patentes, sociedades y contratos.",
         title="Abogados de empresas y marcas en Jujuy | GM & Asociados",
         desc="Registro de marcas y patentes, constitución de sociedades (SAS, SRL, SA) y contratos en Jujuy. Estudio GM & Asociados, especialistas en derecho empresarial.",
         intro="El derecho empresarial es la especialidad que distingue al Estudio. Acompañamos a emprendedores, comercios y empresas para que su proyecto tenga una base legal ordenada.",
         lista=["Registro de marcas y patentes", "Constitución, transformación y disolución de sociedades", "Contratos comerciales y civiles", "Asesoramiento a emprendedores y pymes", "Relación con clientes y proveedores de otras provincias o del exterior"],
         foto="portada-equipo", msg="Hola, quisiera consultar por un tema de empresas, marcas o sociedades."),
    dict(slug="abogados-sucesiones-escrituras-jujuy", nombre="Sucesiones y escrituras", h1="Abogados de sucesiones y escrituras en Jujuy",
         resumen="Herencias, escrituras e inmuebles sin regularizar.",
         title="Sucesiones y escrituras en Jujuy | Estudio GM & Asociados",
         desc="Sucesiones, herencias, escrituras y regularización de inmuebles en San Salvador de Jujuy y El Carmen. Consultá con las abogadas del Estudio GM.",
         intro="Una herencia o una casa sin escritura son trámites que conviene ordenar a tiempo. Te explicamos el camino y nos ocupamos de la parte legal.",
         lista=["Sucesiones y declaratorias de herederos", "Escrituración y regularización de inmuebles", "Casas o terrenos sin escritura", "Compraventas y contratos sobre inmuebles", "Asesoramiento a familias que viven fuera de Jujuy"],
         foto="oficina-roja", msg="Hola, quisiera consultar por una sucesión o escritura."),
    dict(slug="abogados-accidentes-danos-consumidor-jujuy", nombre="Accidentes, daños y consumidor", h1="Abogados por accidentes, daños y reclamos de consumo en Jujuy",
         resumen="Accidentes con secuelas, daños y reclamos de consumo.",
         title="Abogados por accidentes y daños en Jujuy | GM & Asociados",
         desc="Accidentes con secuelas, reclamos por daños y derechos del consumidor en Jujuy. Estudio GM & Asociados: consultanos antes de aceptar una oferta.",
         intro="Después de un accidente o de un problema con una compra o un servicio, conviene consultar antes de firmar o aceptar una oferta. Evaluamos tu caso y te contamos qué podés reclamar.",
         lista=["Accidentes de tránsito con lesiones", "Reclamos de daños y perjuicios", "Reclamos a aseguradoras", "Derechos del consumidor", "Revisión de ofertas antes de aceptarlas"],
         foto="reunion", msg="Hola, quisiera consultar por un accidente, daño o reclamo de consumo."),
]

# --- íconos (SVG propios, un solo trazo) ---
I_WA = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.04 3C8.84 3 3 8.83 3 16.02c0 2.3.6 4.54 1.74 6.51L3 29l6.64-1.7a13 13 0 0 0 6.4 1.64h.01C23.23 28.94 29 23.1 29 15.92 29 8.83 23.2 3 16.04 3Zm0 23.7h-.01a10.7 10.7 0 0 1-5.46-1.5l-.39-.23-3.94 1.01 1.05-3.84-.25-.4a10.67 10.67 0 0 1-1.64-5.72c0-5.9 4.8-10.7 10.7-10.7 2.86 0 5.54 1.1 7.56 3.14a10.6 10.6 0 0 1 3.13 7.57c0 5.9-4.8 10.67-10.75 10.67Zm5.87-8c-.32-.16-1.9-.94-2.2-1.05-.3-.1-.5-.16-.73.16-.21.32-.84 1.05-1.03 1.27-.19.21-.38.24-.7.08-.32-.16-1.36-.5-2.59-1.6a9.7 9.7 0 0 1-1.8-2.24c-.19-.32 0-.5.14-.66.14-.14.32-.38.48-.57.16-.19.21-.32.32-.54.1-.21.05-.4-.03-.56-.08-.16-.73-1.76-1-2.4-.26-.63-.53-.54-.73-.55h-.62c-.21 0-.56.08-.85.4-.29.32-1.11 1.08-1.11 2.64 0 1.55 1.14 3.06 1.3 3.27.16.21 2.23 3.4 5.4 4.77.75.33 1.34.52 1.8.67.76.24 1.45.2 2 .12.6-.09 1.9-.78 2.16-1.53.27-.75.27-1.39.19-1.53-.08-.13-.3-.21-.62-.37Z"/></svg>'
I_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".9" fill="currentColor"/></svg>'
I_FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.8c0-.9.3-1.5 1.6-1.5h1.7V3.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1v2.4H7.6V13h2.8v8h3.1Z"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s-7-6.1-7-11.5a7 7 0 0 1 14 0C19 14.9 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
I_FL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
I_MAPA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" width="18" height="18" aria-hidden="true"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Zm0 0v14m6-12v14"/></svg>'

# Marco en arco: semicírculo arriba, base recta (eco del doble aro del sello)
MARCO = '<svg class="marco" viewBox="0 0 100 125" preserveAspectRatio="none" aria-hidden="true"><path d="M1 124 V50 A49 49 0 0 1 99 50 V124 Z"/></svg>'

P = ""  # prefijo relativo de la página que se está generando

def pic(name, widths, sizes, alt, cls="", eager=False, pos=None, w=None, h=None):
    srcset = ", ".join(f"{P}img/{name}-{x}.webp {x}w" for x in widths)
    extra = ' fetchpriority="high" decoding="async"' if eager else ' loading="lazy" decoding="async"'
    st = f' style="object-position:{pos}"' if pos else ""
    wh = f' width="{w}" height="{h}"' if w else ""
    return f'<img src="{P}img/{name}-{widths[-1]}.webp" srcset="{srcset}" sizes="{sizes}" alt="{esc(alt)}"{wh}{extra}{st}{cls}>'

def cuadro(name, widths, sizes, alt, pos=None, ar="4/5", w=700, h=875, extra=""):
    """Foto de EQUIPO: rectángulo con sombra y marco dorado desplazado."""
    return f'<figure class="cuadro revela {extra}" style="--ar:{ar}"><div class="foto para">{pic(name, widths, sizes, alt, pos=pos, w=w, h=h)}</div></figure>'

def carrusel(items, label):
    """Carrusel infinito de fotos de EQUIPO: altura fija, ancho natural (no se recorta nada)."""
    def fig(n, alt, w, h, dup):
        im = pic(n, [700, 1200], "(max-width:700px) 80vw, 520px", "" if dup else alt, w=w, h=h).replace(' loading="lazy"', '')
        return f'<figure class="slide"{" aria-hidden=\"true\"" if dup else ""}>{im}</figure>'
    uno = "".join(fig(*i, False) for i in items)
    dos = "".join(fig(*i, True) for i in items)
    return f'<div class="carrusel" role="group" aria-label="{esc(label)}"><div class="pista">{uno}{dos}</div></div>'

ARO = '<svg class="aro2" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="49.3"/></svg>'

def retrato(name, alt, chapa=None, extra="", sizes="(max-width:800px) 80vw, 420px"):
    """Foto de UNA abogada: círculo con doble aro dorado (eco del sello del logo)."""
    ch = f'<span class="chapa">{chapa}</span>' if chapa else ""
    return f'<figure class="retrato revela {extra}"><span class="aro"></span>{ARO}<div class="foto">{pic(name, [400, 760], sizes, alt, w=760, h=760)}</div>{ch}</figure>'

def sello(p):
    return f'''<div class="sello" aria-hidden="true"><svg class="texto" viewBox="0 0 120 120"><defs><path id="circ" d="M60 60 m-48 0 a48 48 0 1 1 96 0 a48 48 0 1 1 -96 0"/></defs><text><textPath href="#circ" textLength="296" lengthAdjust="spacing">ESTUDIO JURÍDICO • GM &amp; ASOCIADOS • JUJUY •</textPath></text></svg><img src="{p}img/logo-gm.png" alt="" width="62" height="58"></div>'''

def head(title, desc, path, depth, lang="es", schema=None, alternates=None, preload=None, hero=False):
    p = "../" * depth
    url = f"{BASE}/{path}"
    alt = "".join(f'<link rel="alternate" hreflang="{hl}" href="{BASE}/{hp}">\n' for hl, hp in (alternates or []))
    sch = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n' if schema else ""
    pre = ""
    if preload:
        name, widths = preload
        pre = f'<link rel="preload" as="image" type="image/webp" imagesrcset="{", ".join(f"{p}img/{name}-{x}.webp {x}w" for x in widths)}" imagesizes="100vw" fetchpriority="high">\n'
    intro = "r.classList.add('anim');setTimeout(function(){r.classList.add('listo')},2600);" if hero else ""
    return f"""<!doctype html>
<html lang="{'es-AR' if lang == 'es' else 'en'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
{alt}<meta name="theme-color" content="#841E25">
<meta name="geo.region" content="AR-Y">
<meta name="geo.placename" content="San Salvador de Jujuy">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Estudio Jurídico GM &amp; Asociados">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{'es_AR' if lang == 'es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="preload" href="{p}fonts/poppins-semibold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}fonts/poppins-light.woff2" as="font" type="font/woff2" crossorigin>
{pre}<link rel="stylesheet" href="{p}style.css?v={VER}">
<script>(function(r){{r.classList.add('js');try{{if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&sessionStorage.getItem('gm-intro')!=='1'){{{intro}}}}}catch(e){{}}}})(document.documentElement)</script>
<script src="{p}main.js?v={VER}" defer></script>
<script src="{p}mundo.js?v={VER}" defer></script>
{sch}</head>
<body>
"""

def header(depth, lang="es"):
    p = "../" * depth
    if lang == "es":
        links = [(f"{p}#abogadas", "Abogadas"), (f"{p}#areas", "Áreas"), (f"{p}#sedes", "Sedes"), (f"{p}#exterior", "Desde el exterior"), (f"{p}#preguntas", "Preguntas")]
        cta, skip, menu, home, otro = "Consultanos", "Ir al contenido", "Abrir menú", p or "./", (f"{p}en/", "en", "English")
    else:
        links = [(f"{p}en/#who", "Who we help"), (f"{p}en/#areas", "Practice areas"), (f"{p}en/#team", "Our team"), (f"{p}en/#contact", "Contact")]
        cta, skip, menu, home, otro = "Message us", "Skip to content", "Open menu", f"{p}en/", (p or "./", "es", "Español")
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f"""<a class="skip" href="#main">{skip}</a>
<header class="top"><div class="wrap bar">
<a class="marca" href="{home}" aria-label="Estudio Jurídico GM &amp; Asociados"><span class="logos"><img class="l-blanco" src="{p}img/logo-gm-blanco.png" alt="" width="50" height="50"><img class="l-color" src="{p}img/logo-gm.png" alt="" width="50" height="47"></span></a>
<button class="abrir" type="button" aria-expanded="false" aria-controls="menu"><span></span><b class="sr">{menu}</b></button>
<nav class="menu" id="menu" aria-label="{'Principal' if lang == 'es' else 'Main'}">{nav}<a class="idioma" href="{otro[0]}" hreflang="{otro[1]}" lang="{otro[1]}">{otro[2]}</a><a class="btn sm" href="{WA_GENERAL}" target="_blank" rel="noopener">{I_WA}{cta}</a></nav>
</div></header>
"""

def footer(depth, lang="es"):
    p = "../" * depth
    if lang == "es":
        areas = "".join(f'<li><a href="{p}{a["slug"]}/">{a["nombre"]}</a></li>' for a in AREAS)
        return f"""<footer class="pie"><div class="wrap">
<div class="cols">
<div><img src="{p}img/logo-gm-blanco.png" alt="Estudio Jurídico GM &amp; Asociados" width="72" height="72"><p>Abogados y abogadas en San Salvador de Jujuy y El Carmen. Atendemos en toda la Provincia de Jujuy y a distancia.</p></div>
<div><strong>Áreas</strong><ul>{areas}</ul></div>
<div><strong>Contacto</strong><ul><li><a href="tel:{TEL_LINK}">{TEL_VISIBLE}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{p}en/" hreflang="en" lang="en">English</a></li></ul></div>
</div>
<p class="legal">La información de este sitio es general y orientativa. No constituye asesoramiento legal para un caso particular ni garantiza resultados: cada situación se analiza de forma individual.</p>
</div></footer>
<a class="wa" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{I_WA}<span>Escribinos</span></a>
</body></html>
"""
    return f"""<footer class="pie"><div class="wrap">
<div class="cols">
<div><img src="{p}img/logo-gm-blanco.png" alt="GM &amp; Asociados Law Firm" width="72" height="72"><p>Lawyers in San Salvador de Jujuy and El Carmen, Province of Jujuy, Argentina.</p></div>
<div><strong>Contact</strong><ul><li><a href="https://wa.me/{WA}">+54 9 388 478-3935</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
<div><strong>Follow</strong><ul><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{p}" hreflang="es" lang="es">Español</a></li></ul></div>
</div>
<p class="legal">The information on this site is general and for guidance only. It is not legal advice for a specific case and does not guarantee any result: each situation is assessed individually.</p>
</div></footer>
<a class="wa" href="{wa('Hello, I would like to ask GM & Asociados about a legal matter in Jujuy, Argentina.')}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{I_WA}<span>Message us</span></a>
</body></html>
"""

def schema_org(extra=None):
    addr_ssj = {"@type": "PostalAddress", "streetAddress": "Independencia 658, 1er Piso, Of. 1", "addressLocality": "San Salvador de Jujuy", "addressRegion": "Jujuy", "addressCountry": "AR"}
    g = {"@context": "https://schema.org", "@graph": [
        {"@type": ["LegalService", "LocalBusiness"], "@id": f"{BASE}/#estudio",
         "name": "Estudio Jurídico GM & Asociados", "alternateName": ["GM & Asociados", "Estudio GM Jujuy"],
         "description": "Estudio jurídico en San Salvador de Jujuy y El Carmen, Jujuy, Argentina. Abogadas en derecho empresarial, penal, laboral, familia, sucesiones, daños y consumidor.",
         "url": f"{BASE}/", "logo": f"{BASE}/img/logo-gm.png", "image": [f"{BASE}/img/og.jpg", f"{BASE}/img/portada-equipo-1600.webp"],
         "telephone": TEL_LINK, "email": MAIL, "priceRange": "$$", "address": addr_ssj,
         "areaServed": [{"@type": "AdministrativeArea", "name": "Provincia de Jujuy"}, {"@type": "City", "name": "San Salvador de Jujuy"}, {"@type": "City", "name": "El Carmen"}],
         "knowsAbout": ["Derecho empresarial", "Registro de marcas y patentes", "Sociedades comerciales", "Derecho penal", "Derecho laboral", "Derecho de familia", "Sucesiones", "Escrituras", "Daños y perjuicios", "Derecho del consumidor"],
         "sameAs": [IG, FB],
         "contactPoint": {"@type": "ContactPoint", "telephone": TEL_LINK, "contactType": "customer service", "availableLanguage": ["es"], "areaServed": "AR"},
         "department": [
             {"@type": "LegalService", "name": "Estudio Jurídico GM & Asociados — San Salvador de Jujuy", "address": addr_ssj, "telephone": TEL_LINK},
             {"@type": "LegalService", "name": "Estudio Jurídico GM & Asociados — El Carmen", "address": {"@type": "PostalAddress", "streetAddress": "Sarmiento 520, Barrio Centro", "addressLocality": "El Carmen", "addressRegion": "Jujuy", "addressCountry": "AR"}, "telephone": TEL_LINK}],
         "employee": [{"@type": "Person", "name": e["nombre"], "jobTitle": "Abogada", "image": f"{BASE}/img/{e['img']}-900.webp", "worksFor": {"@id": f"{BASE}/#estudio"}} for e in EQUIPO]},
        {"@type": "WebSite", "@id": f"{BASE}/#web", "url": f"{BASE}/", "name": "Estudio Jurídico GM & Asociados", "inLanguage": "es-AR", "publisher": {"@id": f"{BASE}/#estudio"}},
    ]}
    if extra: g["@graph"].extend(extra)
    return g

def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def mapa(q, titulo):
    src = f"https://www.google.com/maps?q={quote(q)}&output=embed"
    return f'<div class="mapa"><button class="cargar" type="button" data-src="{esc(src)}" data-title="{esc(titulo)}"><span>{I_MAPA}Ver mapa</span></button><noscript><iframe src="{esc(src)}" title="{esc(titulo)}" loading="lazy"></iframe></noscript></div>'

def hero_fondo(foto, p, pos="55% 35%", alt=""):
    widths = [900, 1600, 2400] if foto == "portada-equipo" else [700, 1200]
    img = pic(foto, widths, "100vw", alt, eager=True)
    return f'<div class="fondo" style="--pos:{pos}">{img}</div><div class="velo"></div>'

# ---------------- INICIO ----------------
FAQ = [
    ("¿Cómo pido una consulta?", f"Escribinos por WhatsApp al {TEL_VISIBLE} contándonos brevemente tu situación. Te respondemos para coordinar la consulta en cualquiera de las dos sedes o a distancia."),
    ("¿Atienden en El Carmen y en San Salvador de Jujuy?", "Sí. Tenemos dos sedes: San Salvador de Jujuy (Independencia 658, 1er piso, oficina 1) y El Carmen (Sarmiento 520, Barrio Centro). Atendemos en toda la Provincia de Jujuy."),
    ("¿Cuánto cuesta una consulta?", "Depende de cada caso. Escribinos y te informamos cómo trabajamos y cuáles son los honorarios antes de avanzar con cualquier trámite."),
    ("¿Pueden ayudarme si vivo fuera de Jujuy o en otro país?", "Sí. Muchas consultas pueden empezar a distancia, por WhatsApp o por correo. Si necesitás resolver algo legal en Jujuy desde otra provincia o desde el exterior, contanos tu caso y te explicamos cómo hacerlo."),
    ("¿En qué se especializa el Estudio?", "En derecho empresarial: registro de marcas y patentes, sociedades y contratos. También atendemos temas penales, laborales, de familia, sucesiones, escrituras, accidentes y daños, y consumidor."),
]

def home():
    global P
    carrusel_es = carrusel([('equipo','Las tres abogadas del Estudio GM & Asociados, juntas y sonriendo',1200,1074),('oficina-roja','Las abogadas del Estudio trabajando en la oficina de paredes bordó',1200,956),('reunion','Reunión de trabajo de las abogadas en la oficina del Estudio',1200,817)],'Fotos del equipo')
    p = P = ""
    abogadas = "".join(f"""<article class="abogada">
{retrato('circ-' + e['img'][4:], e['alt'], 'M.P. ' + e['mp'])}
<div class="sube"><h3>{e['nombre']}</h3><p class="mp">Abogada · Matrícula profesional {e['mp']}</p>
<blockquote>{e['frase']}</blockquote>
<a class="btn" href="{wa('Hola, quisiera hacer una consulta con la ' + e['corto'] + '.')}" target="_blank" rel="noopener">{I_WA}Escribile a la {e['corto']}</a></div>
</article>""" for e in EQUIPO).replace("{p}", p)
    areas = "".join(f'<li><a href="{a["slug"]}/"><strong>{a["nombre"]}</strong><span>{a["resumen"]}</span><i class="flecha">{I_FL}</i></a></li>' for a in AREAS)
    faq = "".join(f'<details><summary>{q}<span class="mas" aria-hidden="true"></span></summary><p>{r}</p></details>' for q, r in FAQ)
    title = "Abogadas en Jujuy y El Carmen | Estudio GM & Asociados"
    desc = "Estudio jurídico en San Salvador de Jujuy y El Carmen. Abogados y abogadas en derecho empresarial, penal, laboral y familia. Consultá por WhatsApp."
    s = head(title, desc, "", 0, "es", schema_org(), alternates=[("es-AR", ""), ("en", "en/"), ("x-default", "")], preload=("portada-equipo", [900, 1600, 2400]), hero=True)
    s += header(0)
    s += f"""<main id="main">
<section class="hero">
{hero_fondo("portada-equipo", p, "50% 40%", "Las abogadas del Estudio GM & Asociados trabajando juntas en la oficina de San Salvador de Jujuy")}
<div class="wrap"><div class="texto">
<h1 class="display"><span class="ln"><span>Abogados y abogadas</span></span><span class="ln"><span>en San Salvador</span></span><span class="ln"><span>de Jujuy y El Carmen</span></span></h1>
<span class="filete"></span>
<p class="bajada">Somos el Estudio Jurídico GM &amp; Asociados. Tres abogadas que te escuchan, te explican con palabras simples y te acompañan en toda la Provincia de Jujuy.</p>
<div class="acciones"><a class="btn" href="{WA_GENERAL}" target="_blank" rel="noopener">{I_WA}Consultanos por WhatsApp</a><a class="btn linea" href="#areas">Ver en qué te ayudamos</a></div>
<p class="lugares"><span>{I_PIN}Independencia 658, San Salvador de Jujuy</span><span>{I_PIN}Sarmiento 520, El Carmen</span></p>
</div></div>
</section>

<section class="manifiesto"><div class="wrap">
<div class="fila">
<p class="frase">Escuchamos tu situación, te explicamos tus opciones con palabras simples y te acompañamos en cada paso, en San Salvador de Jujuy, en El Carmen y en toda la provincia.</p>
</div>
<dl class="datos">
<div><dt>Especialidad</dt><dd>Derecho empresarial: marcas, patentes, sociedades y contratos.</dd></div>
<div><dt>Dos sedes</dt><dd>San Salvador de Jujuy y El Carmen, con atención en toda la provincia.</dd></div>
<div><dt>También a distancia</dt><dd>Consultas por WhatsApp y correo, desde otra provincia o desde otro país.</dd></div>
</dl>
</div>
<div class="carrusel-caja">{carrusel_es}</div></section>

<section class="papel" id="abogadas"><div class="wrap">
<div class="cab"><h2>Las abogadas del Estudio</h2><p class="bajada">Elegí con quién querés hablar. Todas las consultas llegan al WhatsApp del Estudio y te responde la abogada que elegiste.</p></div>
{abogadas}
</div></section>

<section id="areas"><div class="wrap areas-grid">
<div class="pegada"><h2>En qué podemos ayudarte</h2><p class="bajada" style="margin:18px 0 36px;color:var(--suave)">Cada situación es distinta. Estas son las áreas en las que trabajamos todos los días.</p></div>
<ul class="lista-areas">{areas}</ul>
</div></section>

<section class="papel"><div class="wrap">
<div class="cab"><h2>Cómo trabajamos</h2><p class="bajada">Antes de avanzar con cualquier trámite, sabés qué vamos a hacer y cuánto cuesta.</p></div>
<ol class="pasos">
<li><h3>Te escuchamos</h3><p>Nos contás tu situación por WhatsApp o en una de las sedes, con la documentación que tengas.</p></li>
<li><h3>Analizamos tu caso</h3><p>Revisamos los datos y evaluamos qué caminos existen para tu situación.</p></li>
<li><h3>Te explicamos y te acompañamos</h3><p>Te contamos los pasos, los tiempos estimados y los honorarios, y te acompañamos hasta el final.</p></li>
</ol>
</div></section>

<section class="sedes" id="sedes"><div class="wrap">
<div class="cab"><h2>Dos sedes en Jujuy</h2><p class="bajada">Te atendemos en persona o a distancia, como te resulte más cómodo.</p></div>
<div class="mosaico">
{retrato('circ-tapia-lectura', 'Dra. Fernanda M. Tapia leyendo un expediente en su escritorio', sizes='300px')}
</div>
<div class="dos-sedes">
<div class="sede"><h3>San Salvador de Jujuy</h3><address>Independencia 658, 1er piso, oficina 1<br>San Salvador de Jujuy, Jujuy</address>{mapa('Independencia 658, San Salvador de Jujuy, Jujuy, Argentina', 'Mapa de la sede San Salvador de Jujuy')}<a class="ir" href="https://www.google.com/maps/search/?api=1&amp;query=Independencia+658+San+Salvador+de+Jujuy" target="_blank" rel="noopener">Cómo llegar en Google Maps</a></div>
<div class="sede"><h3>El Carmen</h3><address>Sarmiento 520, Barrio Centro<br>El Carmen, Jujuy</address>{mapa('Sarmiento 520, El Carmen, Jujuy, Argentina', 'Mapa de la sede El Carmen')}<a class="ir" href="https://www.google.com/maps/search/?api=1&amp;query=Sarmiento+520+El+Carmen+Jujuy" target="_blank" rel="noopener">Cómo llegar en Google Maps</a></div>
</div>
</div></section>

<section class="mundo" id="exterior"><div class="wrap">
<div class="sube">
<h2>Tu puerta legal a Jujuy, estés donde estés</h2>
<p class="bajada">Si necesitás resolver algo legal en Jujuy y estás en otra provincia o en otro país, nos ocupamos desde acá y te mantenemos al tanto.</p>
<ul>
<li><strong>Argentinos afuera</strong><span>Herencias, inmuebles y trámites pendientes en Jujuy.</span></li>
<li><strong>Empresas</strong><span>Registro de marcas, sociedades y contratos para operar en Argentina.</span></li>
<li><strong>Familias</strong><span>Una abogada de confianza que lleve tu trámite en Jujuy.</span></li>
</ul>
<div class="acciones"><a class="btn" href="{wa('Hola, te escribo desde otro país y necesito una gestión legal en Jujuy.')}" target="_blank" rel="noopener">{I_WA}Escribinos desde el exterior</a><a class="btn linea" href="en/" hreflang="en">Read in English</a></div>
</div>
{ORBITAS}
</div></section>

<section class="preguntas" id="preguntas"><div class="wrap">
<div class="lado"><h2>Preguntas frecuentes</h2><p>¿No encontrás tu duda? Escribinos y te respondemos.</p></div>
<div class="faq">{faq}</div>
</div></section>

<section class="cierre" id="contacto"><div class="wrap sube">
<h2>Contanos tu caso.</h2>
<p class="bajada">Escribinos por WhatsApp y coordinamos tu consulta con las abogadas del Estudio.</p>
<div class="acciones"><a class="btn xl" href="{WA_GENERAL}" target="_blank" rel="noopener">{I_WA}Abrir WhatsApp del Estudio</a></div>
<p class="contacto-linea"><span>WhatsApp y teléfono <a href="tel:{TEL_LINK}">{TEL_VISIBLE}</a></span><span><a href="mailto:{MAIL}">{MAIL}</a></span><span>Toda la Provincia de Jujuy</span></p>
<div class="redes"><a href="{IG}" target="_blank" rel="noopener">{I_IG}@estudio.juridicogm</a><a href="{FB}" target="_blank" rel="noopener">{I_FB}@estudio.gm.jujuy</a></div>
</div></section>
</main>
"""
    s += footer(0)
    write("index.html", s)

# Órbitas: el doble aro del sello, con rutas que llegan a Jujuy desde afuera
ORBITAS = '''<canvas id="mundo-cv" class="orbitas" role="img" aria-label="Globo digital con rutas desde distintos lugares del mundo que llegan a Jujuy, resaltado en dorado"></canvas>'''

# ---------------- ÁREAS ----------------
def area_page(a):
    global P
    p = P = "../"
    otros = "".join(f'<a href="../{o["slug"]}/">{o["nombre"]}</a>' for o in AREAS if o["slug"] != a["slug"])
    items = "".join(f"<li>{i}</li>" for i in a["lista"])
    sch = schema_org([breadcrumb([("Inicio", f"{BASE}/"), (a["nombre"], f"{BASE}/{a['slug']}/")]),
                      {"@type": "WebPage", "@id": f"{BASE}/{a['slug']}/#page", "url": f"{BASE}/{a['slug']}/", "name": a["title"], "description": a["desc"], "inLanguage": "es-AR", "isPartOf": {"@id": f"{BASE}/#web"}, "about": {"@id": f"{BASE}/#estudio"}}])
    widths = [900, 1600, 2400] if a["foto"] == "portada-equipo" else [700, 1200]
    s = head(a["title"], a["desc"], a["slug"] + "/", 1, "es", sch, preload=(a["foto"], widths))
    s += header(1)
    s += f"""<main id="main">
<section class="hero interna">
{hero_fondo(a['foto'], p, '50% 40%', '')}
<div class="wrap"><div class="texto">
<p class="migas"><a href="../">Inicio</a> / {a['nombre']}</p>
<h1 class="display">{a['h1']}</h1>
<span class="filete"></span>
<p class="bajada">{a['intro']}</p>
<div class="acciones"><a class="btn" href="{wa(a['msg'])}" target="_blank" rel="noopener">{I_WA}Consultanos por WhatsApp</a></div>
</div></div>
</section>
<section><div class="wrap cuerpo">
<div>
<div class="bloque"><h2>En qué podemos ayudarte</h2><ul class="tilde">{items}</ul></div>
<div class="bloque"><h2>Cómo trabajamos</h2>
<ol class="pasos vertical">
<li><h3>Te escuchamos</h3><p>Nos contás tu situación y la documentación que tengas.</p></li>
<li><h3>Analizamos tu caso</h3><p>Revisamos los datos y evaluamos qué opciones existen.</p></li>
<li><h3>Te explicamos con claridad</h3><p>Te contamos los pasos, los tiempos estimados y los honorarios antes de avanzar.</p></li>
</ol></div>
<div class="bloque"><h2>Dónde atendemos</h2><p class="bajada">En San Salvador de Jujuy (Independencia 658, 1er piso, Of. 1), en El Carmen (Sarmiento 520, Barrio Centro) y a distancia, en toda la Provincia de Jujuy.</p></div>
<div class="bloque"><h2>Otras áreas del Estudio</h2><div class="otras">{otros}</div></div>
</div>
<aside class="caja"><h2>Consultanos</h2><p>Contanos tu caso por WhatsApp y te respondemos para coordinar una consulta con las abogadas del Estudio.</p>
<a class="btn" href="{wa(a['msg'])}" target="_blank" rel="noopener">{I_WA}Escribir por WhatsApp</a>
<small>{TEL_VISIBLE} · Toda la Provincia de Jujuy</small></aside>
</div></section>
<section class="cierre"><div class="wrap sube">
<h2>Contanos tu caso.</h2>
<p class="bajada">Escribinos por WhatsApp y coordinamos tu consulta con las abogadas del Estudio.</p>
<div class="acciones"><a class="btn xl" href="{wa(a['msg'])}" target="_blank" rel="noopener">{I_WA}Abrir WhatsApp del Estudio</a></div>
<div class="redes"><a href="{IG}" target="_blank" rel="noopener">{I_IG}@estudio.juridicogm</a><a href="{FB}" target="_blank" rel="noopener">{I_FB}@estudio.gm.jujuy</a></div>
</div></section>
</main>
"""
    s += footer(1)
    write(f"{a['slug']}/index.html", s)

# ---------------- ENGLISH ----------------
def english():
    global P
    p = P = "../"
    carrusel_en = carrusel([('equipo','The three lawyers of GM & Asociados, together and smiling',1200,1074),('oficina-roja','The lawyers working at the GM & Asociados office',1200,956),('reunion','The lawyers in a team meeting at the office',1200,817)],'Team photos')
    title = "Lawyers in Jujuy, Argentina | GM & Asociados Law Firm"
    desc = "Law firm in San Salvador de Jujuy and El Carmen, Argentina. Legal help for foreigners, companies and Argentines abroad: trademarks, companies, inheritance, property."
    sch = schema_org([{"@type": "WebPage", "@id": f"{BASE}/en/#page", "url": f"{BASE}/en/", "name": title, "description": desc, "inLanguage": "en", "isPartOf": {"@id": f"{BASE}/#web"}, "about": {"@id": f"{BASE}/#estudio"}},
                      breadcrumb([("Inicio", f"{BASE}/"), ("English", f"{BASE}/en/")])])
    wa_en = wa("Hello, I am writing from another country and need legal help in Jujuy, Argentina.")
    team = "".join(f"""<article class="abogada">
{retrato('circ-' + e['img'][4:], e['alt'], 'M.P. ' + e['mp'])}
<div class="sube"><h3>{e['nombre']}</h3><p class="mp">Lawyer · Professional registration {e['mp']}</p>
<a class="btn" href="{wa('Hello, I would like to talk with ' + e['corto'] + '.')}" target="_blank" rel="noopener">{I_WA}Message {e['corto']}</a></div>
</article>""" for e in EQUIPO).replace("{p}", p)
    areas = [("Companies and trademarks", "Trademark and patent registration, setting up or restructuring a company (SAS, SRL, SA), contracts."),
             ("Inheritance and property", "Successions, deeds and property regularization in Jujuy for families living abroad."),
             ("Family matters", "Divorce, child support and parenting arrangements when one party lives outside Argentina."),
             ("Criminal, labor and accidents", "Criminal defense, labor claims, accident and damage claims in the Province of Jujuy.")]
    arow = "".join(f'<li><a href="{wa_en}" target="_blank" rel="noopener"><strong>{n}</strong><span>{d}</span><i class="flecha">{I_FL}</i></a></li>' for n, d in areas)
    s = head(title, desc, "en/", 1, "en", sch, alternates=[("es-AR", ""), ("en", "en/"), ("x-default", "")], preload=("portada-equipo", [900, 1600, 2400]))
    s += header(1, "en")
    s += f"""<main id="main">
<section class="hero">
{hero_fondo("portada-equipo", p, "50% 40%", "The lawyers of GM & Asociados working together at their office in San Salvador de Jujuy")}
<div class="wrap"><div class="texto">
<h1 class="display">Lawyers in Jujuy, Argentina. Your legal gateway from abroad.</h1>
<span class="filete"></span>
<p class="bajada">If you or your company need something legal done in Jujuy and you are in another country, we take care of it here and keep you informed.</p>
<div class="acciones"><a class="btn" href="{wa_en}" target="_blank" rel="noopener">{I_WA}Message us on WhatsApp</a><a class="btn linea" href="#areas">What we do</a></div>
<p class="lugares"><span>{I_PIN}San Salvador de Jujuy</span><span>{I_PIN}El Carmen, Jujuy</span></p>
</div></div>
</section>

<section class="papel" id="who"><div class="wrap">
<div class="cab"><h2>Who we help</h2><p class="bajada">Business law is our main specialty.</p></div>
<ul class="tilde" style="max-width:820px">
<li><strong>Foreign companies and entrepreneurs</strong> that want to register a trademark, set up a company or sign contracts in Argentina.</li>
<li><strong>Argentines living abroad</strong> with an inheritance, a property or a pending procedure in Jujuy.</li>
<li><strong>Families</strong> who need a trusted lawyer to handle a matter in Jujuy on their behalf.</li>
</ul>
<h2 style="margin-top:clamp(64px,8vw,110px);margin-bottom:48px">How it works</h2>
<ol class="pasos">
<li><h3>Write to us</h3><p>Tell us your country and what you need, by WhatsApp or email.</p></li>
<li><h3>We review your case</h3><p>We explain the options, the steps and the fees before moving forward.</p></li>
<li><h3>We handle it in Jujuy</h3><p>You stay informed from wherever you are.</p></li>
</ol>
</div></section>

<section id="areas"><div class="wrap areas-grid">
<div class="pegada"><h2>Practice areas</h2></div>
<ul class="lista-areas">{arow}</ul>
</div></section>

<section class="papel" id="team"><div class="wrap">
<div class="cab"><h2>Our team</h2><p class="bajada">Three lawyers registered in the Province of Jujuy.</p></div>
{team}
</div><div class="carrusel-caja">{carrusel_en}</div></section>

<section class="cierre" id="contact"><div class="wrap sube">
<h2>Tell us what you need.</h2>
<p class="bajada">San Salvador de Jujuy: Independencia 658, 1st floor, Office 1. El Carmen: Sarmiento 520, Barrio Centro.</p>
<div class="acciones"><a class="btn xl" href="{wa_en}" target="_blank" rel="noopener">{I_WA}Message us on WhatsApp</a></div>
<p class="contacto-linea"><span>WhatsApp <a href="https://wa.me/{WA}">+54 9 388 478-3935</a></span><span><a href="mailto:{MAIL}">{MAIL}</a></span></p>
<div class="redes"><a href="{IG}" target="_blank" rel="noopener">{I_IG}Instagram</a><a href="{FB}" target="_blank" rel="noopener">{I_FB}Facebook</a></div>
</div></section>
</main>
"""
    s += footer(1, "en")
    write("en/index.html", s)

def extras():
    urls = [("", "1.0")] + [(a["slug"] + "/", "0.8") for a in AREAS] + [("en/", "0.7")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for u, pr in urls:
        sm += f"<url><loc>{BASE}/{u}</loc><lastmod>{HOY}</lastmod><priority>{pr}</priority>"
        if u in ("", "en/"):
            sm += f'<xhtml:link rel="alternate" hreflang="es-AR" href="{BASE}/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}/en/"/><xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>'
        sm += "</url>\n"
    write("sitemap.xml", sm + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write(".nojekyll", "")
    nf = f"""<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Página no encontrada | Estudio GM &amp; Asociados</title><meta name="robots" content="noindex"><link rel="icon" href="{BASE}/favicon.png"><link rel="stylesheet" href="{BASE}/style.css?v={VER}"></head>
<body><main class="hero" style="min-height:100svh"><div class="velo"></div><div class="wrap"><div class="texto"><h1 class="display">No encontramos esa página.</h1><span class="filete"></span><p class="bajada">Volvé al inicio o escribinos por WhatsApp.</p><div class="acciones"><a class="btn" href="{BASE}/">Ir al inicio</a><a class="btn linea" href="{WA_GENERAL}">Escribir por WhatsApp</a></div></div></div></main></body></html>"""
    write("404.html", nf)

home()
for a in AREAS:
    area_page(a)
english()
extras()
print("OK", BASE, VER)
