#!/usr/bin/env python3
"""Genera el sitio estático del Estudio Jurídico GM & Asociados.
Uso: python3 build.py            (usa BASE de abajo)
     BASE=https://www.midominio.com.ar python3 build.py   (cuando haya dominio propio)
"""
import os, json, html, datetime

BASE = os.environ.get("BASE", "https://consultorarzok.github.io/estudio-gm-asociados-web").rstrip("/")
ROOT = os.path.dirname(os.path.abspath(__file__))
WA = "5493884783935"
TEL_VISIBLE = "388 478-3935"
TEL_LINK = "+543884783935"
MAIL = "asociadosestudiogm@gmail.com"
IG = "https://www.instagram.com/estudio.juridicogm/"
FB = "https://www.facebook.com/estudio.gm.jujuy"
HOY = datetime.date.today().isoformat()

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

WA_GENERAL = wa("Hola, quisiera hacer una consulta con el Estudio GM & Asociados.")

EQUIPO = [
    dict(nombre="Dra. Fernanda M. Tapia", corto="Dra. Tapia", mp="3742", img="dra-tapia.jpg", pos="50% 18%",
         frase="Contanos tu situación y te orientamos, con palabras simples.", alt="Dra. Fernanda M. Tapia, abogada en Jujuy, sonriendo en su escritorio"),
    dict(nombre="Dra. M. Luz Gutiérrez", corto="Dra. Gutiérrez", mp="3544", img="dra-gutierrez.jpg", pos="45% 10%",
         frase="Te explicamos cada trámite de forma clara y te acompañamos.", alt="Dra. M. Luz Gutiérrez, abogada en Jujuy, trabajando en su escritorio"),
    dict(nombre="Dra. Carla Morales", corto="Dra. Morales", mp="3769", img="dra-morales.jpg", pos="50% 15%",
         frase="Una consulta clara y cercana: te escuchamos y te orientamos.", alt="Dra. Carla Morales, abogada en Jujuy, frente a su computadora"),
]

AREAS = [
    dict(slug="abogados-penalistas-jujuy", nombre="Derecho penal", h1="Abogados penalistas en Jujuy",
         title="Abogados penalistas en Jujuy | Estudio GM & Asociados",
         desc="Defensa penal en Jujuy y El Carmen: denuncias, detención de un familiar, estafas virtuales y amenazas. Consultá por WhatsApp con el Estudio GM & Asociados.",
         intro="Si te denunciaron, si fuiste víctima de un delito o si un familiar fue detenido, necesitás saber qué pasos seguir y con quién hablar. Te escuchamos, analizamos tu caso y te explicamos las opciones.",
         lista=["Defensa en causas penales", "Denuncias y participación como víctima o querellante", "Detención de un familiar: qué hacer y a quién acudir", "Estafas virtuales y delitos informáticos", "Amenazas e intimidaciones por WhatsApp y redes sociales", "Acuerdos y salidas alternativas del proceso penal"],
         msg="Hola, quisiera consultar por un tema de derecho penal."),
    dict(slug="abogados-laboralistas-jujuy", nombre="Derecho laboral", h1="Abogados laboralistas en Jujuy",
         title="Abogados laboralistas en Jujuy | Estudio GM & Asociados",
         desc="Despidos, trabajo no registrado y reclamos laborales en San Salvador de Jujuy y El Carmen. Estudio GM & Asociados: consultá por WhatsApp.",
         intro="Un despido o un reclamo laboral se resuelve mejor con información clara desde el primer día. Revisamos tu situación, la documentación que tengas y te contamos cómo se puede avanzar.",
         lista=["Despidos y liquidación final", "Trabajo no registrado o mal registrado", "Reclamos de salarios y diferencias", "Accidentes y enfermedades vinculados al trabajo", "Asesoramiento a empleadores y pequeñas empresas"],
         msg="Hola, quisiera consultar por un tema laboral."),
    dict(slug="abogados-de-familia-jujuy", nombre="Familia", h1="Abogados de familia en San Salvador de Jujuy",
         title="Abogados de familia en Jujuy | Estudio GM & Asociados",
         desc="Divorcio, cuota alimentaria, régimen de comunicación y cuidado de hijos en Jujuy. Abogadas de familia en San Salvador de Jujuy y El Carmen.",
         intro="Los temas de familia son delicados. Te acompañamos con respeto y te explicamos cada etapa para que puedas decidir con tranquilidad.",
         lista=["Divorcio", "Cuota alimentaria", "Régimen de comunicación con los hijos", "Cuidado personal de los hijos", "Acuerdos entre las partes y convenios"],
         msg="Hola, quisiera consultar por un tema de familia."),
    dict(slug="abogados-derecho-empresarial-jujuy", nombre="Derecho empresarial", h1="Abogados de derecho empresarial en Jujuy",
         title="Abogados de empresas y marcas en Jujuy | GM & Asociados",
         desc="Registro de marcas y patentes, constitución de sociedades (SAS, SRL, SA) y contratos en Jujuy. Estudio GM & Asociados, especialistas en derecho empresarial.",
         intro="El derecho empresarial es la especialidad que más destaca al Estudio. Acompañamos a emprendedores, comercios y empresas para que su proyecto tenga una base legal ordenada.",
         lista=["Registro de marcas y patentes", "Constitución, transformación y disolución de sociedades", "Contratos comerciales y civiles", "Asesoramiento a emprendedores y pymes", "Relación con clientes y proveedores, de otras provincias o del exterior"],
         msg="Hola, quisiera consultar por un tema de empresas, marcas o sociedades."),
    dict(slug="abogados-sucesiones-escrituras-jujuy", nombre="Sucesiones y escrituras", h1="Abogados de sucesiones y escrituras en Jujuy",
         title="Sucesiones y escrituras en Jujuy | Estudio GM & Asociados",
         desc="Sucesiones, herencias, escrituras y regularización de inmuebles en San Salvador de Jujuy y El Carmen. Consultá con las abogadas del Estudio GM.",
         intro="Una herencia o una casa sin escritura son trámites que conviene ordenar a tiempo. Te explicamos el camino y nos ocupamos de la parte legal.",
         lista=["Sucesiones y declaratorias de herederos", "Escrituración y regularización de inmuebles", "Casas o terrenos sin escritura", "Compraventas y contratos sobre inmuebles", "Asesoramiento a familias que viven fuera de Jujuy"],
         msg="Hola, quisiera consultar por una sucesión o escritura."),
    dict(slug="abogados-accidentes-danos-consumidor-jujuy", nombre="Accidentes, daños y consumidor", h1="Abogados por accidentes, daños y reclamos de consumo en Jujuy",
         title="Abogados por accidentes y daños en Jujuy | GM & Asociados",
         desc="Accidentes con secuelas, reclamos por daños y derechos del consumidor en Jujuy. Estudio GM & Asociados: consultanos por WhatsApp antes de aceptar una oferta.",
         intro="Después de un accidente o de un problema con una compra o un servicio, conviene consultar antes de firmar o aceptar una oferta. Evaluamos tu caso y te contamos qué podés reclamar.",
         lista=["Accidentes de tránsito con lesiones", "Reclamos de daños y perjuicios", "Reclamos a aseguradoras", "Derechos del consumidor", "Revisión de ofertas antes de aceptarlas"],
         msg="Hola, quisiera consultar por un accidente, daño o reclamo de consumo."),
]

CSS = """
:root{--bordo:#841E25;--bordo-p:#682018;--oscuro:#261F1C;--dorado:#C7A254;--dorado-t:#8a6a1f;--crema:#F5F0E7;--crema2:#ECE4D4;--carbon:#3C3630;--blanco:#fff}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:84px}
body{font-family:'Poppins',system-ui,sans-serif;background:var(--crema);color:var(--carbon);line-height:1.65;font-weight:400;font-size:17px;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:var(--bordo)}
.wrap{width:min(1140px,100% - 40px);margin-inline:auto}
:focus-visible{outline:3px solid var(--dorado);outline-offset:3px;border-radius:4px}
.skip{position:absolute;left:-999px;top:8px;background:var(--bordo);color:#fff;padding:10px 16px;z-index:100;border-radius:6px}
.skip:focus{left:8px}
h1,h2,h3{font-weight:700;line-height:1.15;color:var(--bordo);letter-spacing:-.01em;text-wrap:balance}
h1{font-size:clamp(2.1rem,5.4vw,3.9rem)}
h2{font-size:clamp(1.65rem,3.4vw,2.5rem);margin-bottom:.5em}
h3{font-size:1.2rem}
p{max-width:62ch}
.lead{font-weight:300;font-size:1.18rem;color:var(--carbon)}
.rule{display:block;width:64px;height:3px;background:var(--dorado);margin:22px 0}
/* header */
header.top{position:sticky;top:0;z-index:50;background:rgba(245,240,231,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--crema2)}
.bar{display:flex;align-items:center;gap:24px;min-height:72px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--bordo);font-weight:600;line-height:1.2;font-size:.95rem}
.brand img{width:48px;height:48px;object-fit:contain}
nav.main{margin-left:auto;display:flex;gap:22px;align-items:center}
nav.main a{text-decoration:none;color:var(--carbon);font-weight:500;font-size:.92rem}
nav.main a:hover{color:var(--bordo)}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--dorado);color:var(--oscuro);font-weight:600;text-decoration:none;padding:14px 26px;border-radius:999px;border:2px solid var(--dorado);font-size:1rem;transition:background .2s,color .2s;cursor:pointer}
.btn:hover{background:var(--bordo);border-color:var(--bordo);color:#fff}
.btn.sec{background:transparent;color:var(--bordo);border-color:var(--bordo)}
.btn.sec:hover{background:var(--bordo);color:#fff}
.btn.sm{padding:10px 20px;font-size:.9rem}
.btn svg{width:20px;height:20px;flex:none}
.menu-btn{display:none;margin-left:auto;background:none;border:2px solid var(--bordo);color:var(--bordo);border-radius:8px;padding:8px 12px;font:600 .9rem Poppins,sans-serif}
@media(max-width:860px){.menu-btn{display:block}nav.main{display:none;position:absolute;left:0;right:0;top:100%;background:var(--crema);flex-direction:column;align-items:stretch;gap:0;padding:8px 20px 20px;border-bottom:1px solid var(--crema2)}nav.main.open{display:flex}nav.main a{padding:14px 0;border-bottom:1px solid var(--crema2)}nav.main .btn{justify-content:center;margin-top:14px;border-bottom:2px solid var(--dorado)}}
/* hero */
.hero{padding:clamp(32px,6vw,72px) 0 clamp(40px,7vw,88px)}
.hero .grid{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(28px,5vw,72px);align-items:center}
.hero .acts{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}
.hero .meta{margin-top:26px;font-size:.95rem;color:var(--carbon);font-weight:300}
.hero .meta strong{font-weight:600}
@media(max-width:860px){.hero .grid{grid-template-columns:1fr}.hero .arch{order:-1}}
/* arco: eco del doble aro del sello */
.arch{position:relative;border-radius:999px 999px 18px 18px;overflow:hidden;aspect-ratio:4/5;background:var(--crema2)}
.arch img{width:100%;height:100%;object-fit:cover}
.ring{position:relative;padding:10px;border:2px solid var(--dorado);border-radius:999px 999px 28px 28px}
.ring.hero-ring{max-width:520px;margin-left:auto}.hero-ring .arch{aspect-ratio:1/1.04}
@media(max-width:860px){.ring.hero-ring{margin:0 auto;max-width:380px}}
/* secciones */
section{padding:clamp(52px,8vw,96px) 0}
.alt{background:var(--blanco)}
.team{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(24px,4vw,48px);margin-top:44px}
@media(max-width:860px){.team{grid-template-columns:1fr;max-width:420px;margin-inline:auto}}
.mem h3{margin-top:22px;font-size:1.3rem}
.mem .mp{font-weight:500;font-size:.9rem;color:var(--dorado-t);margin:2px 0 10px}
.mem p{font-weight:300;margin-bottom:18px}
.areas{margin-top:36px;border-top:1px solid var(--crema2)}
.areas a{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.4fr) auto;gap:24px;align-items:center;padding:24px 4px;border-bottom:1px solid var(--crema2);text-decoration:none;color:var(--carbon);transition:background .2s}
.areas a:hover{background:var(--crema)}
.areas strong{color:var(--bordo);font-size:1.25rem;font-weight:700;line-height:1.2}
.areas span{font-weight:300}
.areas i{font-style:normal;color:var(--dorado-t);font-weight:600}
@media(max-width:720px){.areas a{grid-template-columns:1fr;gap:6px}}
.band{background:var(--bordo);color:#fff}
.band h2,.band h3{color:#fff}
.band p,.band li{color:#f3e8e0}
.band a{color:#fff}
.sedes{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,64px);margin-top:36px}
@media(max-width:720px){.sedes{grid-template-columns:1fr}}
.sede{border-top:3px solid var(--dorado);padding-top:18px}
.sede address{font-style:normal;font-weight:300;font-size:1.1rem;margin:8px 0 14px}
.sede a{font-weight:600}
.world{background:var(--oscuro);color:#efe7dd}
.world h2{color:#fff}.world p{color:#e6dccf}
.world .cols{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);align-items:center}
@media(max-width:860px){.world .cols{grid-template-columns:1fr}}
.world ul{list-style:none;margin:18px 0 28px}
.world li{padding:12px 0;border-bottom:1px solid rgba(199,162,84,.35);font-weight:300}
.world li strong{font-weight:600;color:var(--dorado)}
.world .btn.sec{color:#fff;border-color:var(--dorado)}
.world .btn.sec:hover{background:var(--dorado);color:var(--oscuro)}
.world figure{border:2px solid var(--dorado);border-radius:18px;padding:10px}
.world figure img{border-radius:10px}
details{border-bottom:1px solid var(--crema2);padding:18px 0}
details summary{cursor:pointer;font-weight:600;color:var(--bordo);font-size:1.08rem;list-style:none;display:flex;justify-content:space-between;gap:16px}
details summary::after{content:"+";color:var(--dorado-t);font-size:1.5rem;line-height:1}
details[open] summary::after{content:"–"}
details p{margin-top:10px;font-weight:300}
.faq{max-width:780px;margin-top:28px;border-top:1px solid var(--crema2)}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,72px);align-items:center}
@media(max-width:860px){.contact{grid-template-columns:1fr}}
.contact dl{margin-top:22px}
.contact dt{font-weight:600;color:var(--bordo);margin-top:14px}
.contact dd{font-weight:300}
.social{display:flex;gap:12px;margin-top:22px;flex-wrap:wrap}
.social a{display:inline-flex;align-items:center;gap:10px;border:2px solid var(--bordo);color:var(--bordo);border-radius:999px;padding:10px 20px;text-decoration:none;font-weight:600;font-size:.95rem}
.social a:hover{background:var(--bordo);color:#fff}
.social svg{width:20px;height:20px}
footer{background:var(--oscuro);color:#d9cfc2;padding:44px 0 90px;font-size:.92rem;font-weight:300}
footer a{color:#fff}
footer .row{display:flex;flex-wrap:wrap;gap:28px;justify-content:space-between;align-items:flex-start}
footer img{width:64px;margin-bottom:10px}
footer p{max-width:46ch}
footer .legal{margin-top:28px;padding-top:20px;border-top:1px solid rgba(255,255,255,.15);font-size:.82rem;opacity:.85}
.fab{position:fixed;right:18px;bottom:18px;z-index:60;background:#25D366;color:#fff;width:60px;height:60px;border-radius:50%;display:grid;place-items:center;box-shadow:0 6px 20px rgba(0,0,0,.28)}
.fab svg{width:32px;height:32px}
.fab:hover{background:var(--bordo)}
/* paginas internas */
.page-head{padding:clamp(36px,6vw,72px) 0 24px}
.crumbs{font-size:.85rem;margin-bottom:18px;font-weight:400}
.crumbs a{text-decoration:none}
.two{display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(28px,5vw,64px);align-items:start}
@media(max-width:860px){.two{grid-template-columns:1fr}}
.check{list-style:none;margin:14px 0}
.check li{padding:12px 0 12px 34px;position:relative;border-bottom:1px solid var(--crema2)}
.check li::before{content:"";position:absolute;left:4px;top:19px;width:14px;height:8px;border-left:3px solid var(--dorado);border-bottom:3px solid var(--dorado);transform:rotate(-45deg)}
.steps{counter-reset:s;list-style:none;margin-top:18px}
.steps li{counter-increment:s;padding:14px 0 14px 52px;position:relative;border-bottom:1px solid var(--crema2)}
.steps li::before{content:counter(s);position:absolute;left:0;top:12px;width:34px;height:34px;border-radius:50%;background:var(--bordo);color:#fff;display:grid;place-items:center;font-weight:600;font-size:.95rem}
.aside{background:var(--bordo);color:#fff;border-radius:18px;padding:28px;position:sticky;top:96px}
.aside h2{color:#fff;font-size:1.4rem}
.aside p{color:#f3e8e0;font-weight:300;margin-bottom:18px}
.aside .btn:hover{background:#fff;color:var(--bordo);border-color:#fff}
.others{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.others a{border:1.5px solid var(--bordo);border-radius:999px;padding:8px 18px;text-decoration:none;font-weight:500;font-size:.92rem}
.others a:hover{background:var(--bordo);color:#fff}
.lang{font-size:.85rem;font-weight:500;text-decoration:none;border:1.5px solid var(--carbon);color:var(--carbon);padding:5px 12px;border-radius:999px}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.hero .grid>*{animation:rise .7s ease both}.hero .grid>*:nth-child(2){animation-delay:.12s}
@media(prefers-reduced-motion:reduce){.hero .grid>*{animation:none}}
"""

WA_SVG = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.04 3C8.84 3 3 8.83 3 16.02c0 2.3.6 4.54 1.74 6.51L3 29l6.64-1.7a13 13 0 0 0 6.4 1.64h.01C23.23 28.94 29 23.1 29 15.92 29 8.83 23.2 3 16.04 3Zm0 23.7h-.01a10.7 10.7 0 0 1-5.46-1.5l-.39-.23-3.94 1.01 1.05-3.84-.25-.4a10.67 10.67 0 0 1-1.64-5.72c0-5.9 4.8-10.7 10.7-10.7 2.86 0 5.54 1.1 7.56 3.14a10.6 10.6 0 0 1 3.13 7.57c0 5.9-4.8 10.67-10.75 10.67Zm5.87-8c-.32-.16-1.9-.94-2.2-1.05-.3-.1-.5-.16-.73.16-.21.32-.84 1.05-1.03 1.27-.19.21-.38.24-.7.08-.32-.16-1.36-.5-2.59-1.6a9.7 9.7 0 0 1-1.8-2.24c-.19-.32 0-.5.14-.66.14-.14.32-.38.48-.57.16-.19.21-.32.32-.54.1-.21.05-.4-.03-.56-.08-.16-.73-1.76-1-2.4-.26-.63-.53-.54-.73-.55h-.62c-.21 0-.56.08-.85.4-.29.32-1.11 1.08-1.11 2.64 0 1.55 1.14 3.06 1.3 3.27.16.21 2.23 3.4 5.4 4.77.75.33 1.34.52 1.8.67.76.24 1.45.2 2 .12.6-.09 1.9-.78 2.16-1.53.27-.75.27-1.39.19-1.53-.08-.13-.3-.21-.62-.37Z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.8c0-.9.3-1.5 1.6-1.5h1.7V3.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1v2.4H7.6V13h2.8v8h3.1Z"/></svg>'

def esc(s): return html.escape(s, quote=True)

def head(title, desc, path, depth, lang="es", extra_schema=None, alternates=None, og_title=None):
    pre = "../" * depth
    url = f"{BASE}/{path}"
    alt_links = ""
    if alternates:
        for hl, hp in alternates:
            alt_links += f'<link rel="alternate" hreflang="{hl}" href="{BASE}/{hp}">\n'
    schema = f'<script type="application/ld+json">{json.dumps(extra_schema, ensure_ascii=False)}</script>' if extra_schema else ""
    locale = "es_AR" if lang == "es" else "en_US"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
{alt_links}<meta name="theme-color" content="#841E25">
<meta name="geo.region" content="AR-Y">
<meta name="geo.placename" content="San Salvador de Jujuy">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Estudio Jurídico GM & Asociados">
<meta property="og:title" content="{esc(og_title or title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/og.jpg">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}style.css">
{schema}
</head>
<body>
"""

def header(depth, lang="es", lang_link=None):
    pre = "../" * depth
    if lang == "es":
        links = [(f"{pre}#equipo", "Abogadas"), (f"{pre}#areas", "Áreas"), (f"{pre}#sedes", "Sedes"), (f"{pre}#desde-el-exterior", "Desde el exterior"), (f"{pre}#contacto", "Contacto")]
        cta = "Consultanos"; skip = "Ir al contenido"; menu = "Menú"
    else:
        links = [(f"{pre}en/#how", "How we help"), (f"{pre}en/#areas", "Practice areas"), (f"{pre}en/#team", "Our team"), (f"{pre}en/#contact", "Contact")]
        cta = "Message us"; skip = "Skip to content"; menu = "Menu"
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
    ll = f'<a class="lang" href="{lang_link[0]}" hreflang="{lang_link[1]}" lang="{lang_link[1]}">{lang_link[2]}</a>' if lang_link else ""
    home = f"{pre}" if lang == "es" else f"{pre}en/"
    return f"""<a class="skip" href="#main">{skip}</a>
<header class="top"><div class="wrap bar">
<a class="brand" href="{home or './'}"><img src="{pre}img/logo-gm.png" alt="Logo del Estudio Jurídico GM & Asociados" width="48" height="45"><span>Estudio Jurídico<br>GM &amp; Asociados</span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">{menu}</button>
<nav class="main" id="nav" aria-label="Principal">{nav}{ll}<a class="btn sm" href="{WA_GENERAL}" rel="noopener" target="_blank">{WA_SVG}{cta}</a></nav>
</div></header>
"""

def footer(depth, lang="es"):
    pre = "../" * depth
    if lang == "es":
        areas = "".join(f'<li><a href="{pre}{a["slug"]}/">{a["nombre"]}</a></li>' for a in AREAS)
        return f"""<footer><div class="wrap">
<div class="row">
<div><img src="{pre}img/logo-gm-blanco.png" alt="" width="64" height="64"><p>Estudio Jurídico GM &amp; Asociados. Abogados y abogadas en San Salvador de Jujuy y El Carmen. Atendemos en toda la Provincia de Jujuy.</p></div>
<div><strong>Áreas</strong><ul style="list-style:none;margin-top:8px;line-height:2">{areas}</ul></div>
<div><strong>Contacto</strong><p style="margin-top:8px">WhatsApp y teléfono: <a href="tel:{TEL_LINK}">{TEL_VISIBLE}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{IG}" rel="noopener" target="_blank">Instagram</a> · <a href="{FB}" rel="noopener" target="_blank">Facebook</a><br><a href="{pre}en/">English</a></p></div>
</div>
<p class="legal">La información de este sitio es general y orientativa, no constituye asesoramiento legal para un caso particular ni garantiza resultados. Cada situación se analiza de forma individual.</p>
</div></footer>
<a class="fab" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{WA_SVG}</a>
</body></html>
"""
    return f"""<footer><div class="wrap">
<div class="row">
<div><img src="{pre}img/logo-gm-blanco.png" alt="" width="64" height="64"><p>GM &amp; Asociados Law Firm. Lawyers in San Salvador de Jujuy and El Carmen, Jujuy, Argentina.</p></div>
<div><strong>Contact</strong><p style="margin-top:8px">WhatsApp: <a href="https://wa.me/{WA}">+54 9 388 478-3935</a><br><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{IG}" rel="noopener" target="_blank">Instagram</a> · <a href="{FB}" rel="noopener" target="_blank">Facebook</a><br><a href="{pre}">Español</a></p></div>
</div>
<p class="legal">The information on this site is general and for guidance only. It is not legal advice for a specific case and does not guarantee any result. Each situation is assessed individually.</p>
</div></footer>
<a class="fab" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{WA_SVG}</a>
</body></html>
"""

def schema_org(extra=None):
    g = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["LegalService", "LocalBusiness"],
                "@id": f"{BASE}/#estudio",
                "name": "Estudio Jurídico GM & Asociados",
                "alternateName": ["GM & Asociados", "Estudio GM Jujuy"],
                "description": "Estudio jurídico en San Salvador de Jujuy y El Carmen, Jujuy, Argentina. Abogados y abogadas en derecho empresarial, penal, laboral, familia, sucesiones, daños y consumidor.",
                "url": f"{BASE}/",
                "logo": f"{BASE}/img/logo-gm.png",
                "image": f"{BASE}/img/og.jpg",
                "telephone": TEL_LINK,
                "email": MAIL,
                "priceRange": "$$",
                "address": {"@type": "PostalAddress", "streetAddress": "Independencia 658, 1er Piso, Of. 1", "addressLocality": "San Salvador de Jujuy", "addressRegion": "Jujuy", "addressCountry": "AR"},
                "areaServed": [{"@type": "AdministrativeArea", "name": "Provincia de Jujuy"}, {"@type": "City", "name": "San Salvador de Jujuy"}, {"@type": "City", "name": "El Carmen"}],
                "knowsAbout": ["Derecho empresarial", "Registro de marcas y patentes", "Sociedades", "Derecho penal", "Derecho laboral", "Derecho de familia", "Sucesiones", "Daños y perjuicios", "Derecho del consumidor"],
                "knowsLanguage": ["es"],
                "sameAs": [IG, FB],
                "contactPoint": {"@type": "ContactPoint", "telephone": TEL_LINK, "contactType": "customer service", "availableLanguage": ["es"], "areaServed": "AR"},
                "location": [
                    {"@type": "Place", "name": "Sede San Salvador de Jujuy", "address": {"@type": "PostalAddress", "streetAddress": "Independencia 658, 1er Piso, Of. 1", "addressLocality": "San Salvador de Jujuy", "addressRegion": "Jujuy", "addressCountry": "AR"}},
                    {"@type": "Place", "name": "Sede El Carmen", "address": {"@type": "PostalAddress", "streetAddress": "Sarmiento 520, Barrio Centro", "addressLocality": "El Carmen", "addressRegion": "Jujuy", "addressCountry": "AR"}},
                ],
                "employee": [
                    {"@type": "Person", "name": e["nombre"], "jobTitle": "Abogada", "worksFor": {"@id": f"{BASE}/#estudio"}, "image": f"{BASE}/img/{e['img']}"} for e in EQUIPO
                ],
            },
            {"@type": "WebSite", "@id": f"{BASE}/#web", "url": f"{BASE}/", "name": "Estudio Jurídico GM & Asociados", "inLanguage": "es-AR", "publisher": {"@id": f"{BASE}/#estudio"}},
        ],
    }
    if extra:
        g["@graph"].extend(extra)
    return g

def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

# ---------------- HOME ----------------
FAQ = [
    ("¿Cómo pido una consulta?", f"Escribinos por WhatsApp al {TEL_VISIBLE} contándonos brevemente tu situación. Te respondemos para coordinar la consulta, en cualquiera de las dos sedes o a distancia."),
    ("¿Atienden en El Carmen y en San Salvador de Jujuy?", "Sí. Tenemos dos sedes: San Salvador de Jujuy (Independencia 658, 1er piso, oficina 1) y El Carmen (Sarmiento 520, Barrio Centro). Atendemos en toda la Provincia de Jujuy."),
    ("¿Cuánto cuesta una consulta?", "Depende de cada caso. Escribinos y te informamos cómo trabajamos y los honorarios antes de avanzar con cualquier trámite."),
    ("¿Pueden ayudarme si vivo fuera de Jujuy o en otro país?", "Sí. Muchas consultas pueden iniciarse a distancia por WhatsApp o mail. Si necesitás resolver algo legal en Jujuy desde otra provincia o desde el exterior, contanos tu caso y te explicamos cómo hacerlo."),
    ("¿Qué especialidades tienen?", "El Estudio se destaca en derecho empresarial (registro de marcas y patentes, sociedades y contratos). También atendemos temas penales, laborales, de familia, sucesiones, escrituras, daños y accidentes, y consumidor."),
]

def home():
    team = ""
    for e in EQUIPO:
        team += f"""<article class="mem">
<div class="ring"><div class="arch"><img src="img/{e['img']}" alt="{esc(e['alt'])}" style="object-position:{e['pos']}" loading="lazy" width="640" height="800"></div></div>
<h3>{e['nombre']}</h3><p class="mp">Abogada · M.P. {e['mp']}</p><p>{e['frase']}</p>
<a class="btn sm" href="{wa('Hola, quisiera hacer una consulta con la ' + e['corto'] + '.')}" target="_blank" rel="noopener">{WA_SVG}Escribile a la {e['corto']}</a>
</article>"""
    areas = ""
    resumen = {
        "abogados-penalistas-jujuy": "Defensa, denuncias, detenciones y estafas virtuales.",
        "abogados-laboralistas-jujuy": "Despidos, trabajo no registrado y reclamos.",
        "abogados-de-familia-jujuy": "Divorcio, cuota alimentaria y comunicación con los hijos.",
        "abogados-derecho-empresarial-jujuy": "Marcas y patentes, sociedades y contratos.",
        "abogados-sucesiones-escrituras-jujuy": "Herencias, escrituras e inmuebles sin regularizar.",
        "abogados-accidentes-danos-consumidor-jujuy": "Accidentes con secuelas, daños y reclamos de consumo.",
    }
    for a in AREAS:
        areas += f'<a href="{a["slug"]}/"><strong>{a["nombre"]}</strong><span>{resumen[a["slug"]]}</span><i>Ver más</i></a>'
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    title = "Abogadas en Jujuy y El Carmen | Estudio GM & Asociados"
    desc = "Estudio jurídico en San Salvador de Jujuy y El Carmen. Abogados y abogadas en derecho empresarial, penal, laboral y familia. Consultá por WhatsApp."
    s = head(title, desc, "", 0, "es", schema_org(), alternates=[("es-AR", ""), ("en", "en/"), ("x-default", "")])
    s += header(0, "es", ("en/", "en", "English"))
    s += f"""<main id="main">
<section class="hero"><div class="wrap grid">
<div>
<h1>Abogados y abogadas en San Salvador de Jujuy y El Carmen</h1>
<span class="rule"></span>
<p class="lead">Somos el Estudio Jurídico GM &amp; Asociados: tres abogadas que te escuchan, te explican con palabras simples y te acompañan en toda la Provincia de Jujuy.</p>
<div class="acts">
<a class="btn" href="{WA_GENERAL}" target="_blank" rel="noopener">{WA_SVG}Consultanos por WhatsApp</a>
<a class="btn sec" href="#areas">Ver áreas de trabajo</a>
</div>
<p class="meta"><strong>Derecho empresarial</strong>, penal, laboral, familia, sucesiones, daños y consumidor. Atendemos también a distancia.</p>
</div>
<div class="ring hero-ring"><div class="arch"><img src="img/equipo.jpg" alt="Las tres abogadas del Estudio Jurídico GM & Asociados, Jujuy" width="900" height="805" fetchpriority="high" style="object-position:50% 30%"></div></div>
</div></section>

<section class="alt" id="equipo"><div class="wrap">
<h2>Las abogadas del Estudio</h2>
<p class="lead">Elegí con quién querés hablar. Todas las consultas llegan al WhatsApp del Estudio.</p>
<div class="team">{team}</div>
</div></section>

<section id="areas"><div class="wrap">
<h2>En qué podemos ayudarte</h2>
<p class="lead">Cada situación es distinta. Estas son las áreas en las que trabajamos todos los días.</p>
<div class="areas">{areas}</div>
</div></section>

<section class="band" id="sedes"><div class="wrap">
<h2>Dos sedes en Jujuy</h2>
<p>Te atendemos en persona o a distancia, como te resulte más cómodo.</p>
<div class="sedes">
<div class="sede"><h3>San Salvador de Jujuy</h3><address>Independencia 658, 1er piso, Of. 1<br>San Salvador de Jujuy, Jujuy</address><a href="https://www.google.com/maps/search/?api=1&query=Independencia+658+San+Salvador+de+Jujuy" target="_blank" rel="noopener">Ver en el mapa</a></div>
<div class="sede"><h3>El Carmen</h3><address>Sarmiento 520, Barrio Centro<br>El Carmen, Jujuy</address><a href="https://www.google.com/maps/search/?api=1&query=Sarmiento+520+El+Carmen+Jujuy" target="_blank" rel="noopener">Ver en el mapa</a></div>
</div></div></section>

<section class="world" id="desde-el-exterior"><div class="wrap cols">
<div>
<h2>¿Necesitás resolver algo legal en Jujuy desde otro país?</h2>
<p class="lead" style="color:#e6dccf">Somos la puerta de entrada al sistema legal de Jujuy para quienes están lejos.</p>
<ul>
<li><strong>Argentinos en el exterior</strong> con trámites, herencias o inmuebles pendientes en Jujuy.</li>
<li><strong>Empresas y emprendedores</strong> de otras provincias o países que quieren registrar una marca o constituir una sociedad.</li>
<li><strong>Familias</strong> que necesitan que alguien de confianza lleve un trámite en Jujuy.</li>
</ul>
<a class="btn" href="en/">Read this in English</a> <a class="btn sec" href="{wa('Hola, te escribo desde otro país y necesito una gestión legal en Jujuy.')}" target="_blank" rel="noopener">Escribinos desde el exterior</a>
</div>
<figure><img src="img/oficina.jpg" alt="Oficina del Estudio GM & Asociados en Jujuy" loading="lazy" width="1000" height="562"></figure>
</div></section>

<section class="alt" id="preguntas"><div class="wrap">
<h2>Preguntas frecuentes</h2>
<div class="faq">{faq}</div>
</div></section>

<section id="contacto"><div class="wrap contact">
<div>
<h2>Contanos tu caso</h2>
<p class="lead">Escribinos por WhatsApp y te respondemos para coordinar tu consulta.</p>
<dl>
<dt>WhatsApp y teléfono</dt><dd><a href="tel:{TEL_LINK}">{TEL_VISIBLE}</a></dd>
<dt>Correo</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
<dt>Zona de atención</dt><dd>Toda la Provincia de Jujuy</dd>
</dl>
<div class="social">
<a href="{IG}" target="_blank" rel="noopener">{IG_SVG}Instagram</a>
<a href="{FB}" target="_blank" rel="noopener">{FB_SVG}Facebook</a>
</div>
</div>
<div><a class="btn" href="{WA_GENERAL}" target="_blank" rel="noopener" style="font-size:1.15rem;padding:20px 34px">{WA_SVG}Abrir WhatsApp del Estudio</a>
<p style="margin-top:18px;font-weight:300">Instagram: @estudio.juridicogm<br>Facebook: @estudio.gm.jujuy</p></div>
</div></section>
</main>
"""
    s += footer(0, "es")
    write("index.html", s)

# ---------------- AREAS ----------------
def area_page(a):
    otros = "".join(f'<a href="../{o["slug"]}/">{o["nombre"]}</a>' for o in AREAS if o["slug"] != a["slug"])
    items = "".join(f"<li>{i}</li>" for i in a["lista"])
    sch = schema_org([breadcrumb([("Inicio", f"{BASE}/"), (a["nombre"], f"{BASE}/{a['slug']}/")]),
                      {"@type": "WebPage", "@id": f"{BASE}/{a['slug']}/#page", "url": f"{BASE}/{a['slug']}/", "name": a["title"], "description": a["desc"], "inLanguage": "es-AR", "isPartOf": {"@id": f"{BASE}/#web"}, "about": {"@id": f"{BASE}/#estudio"}}])
    s = head(a["title"], a["desc"], a["slug"] + "/", 1, "es", sch)
    s += header(1, "es", ("../en/", "en", "English"))
    s += f"""<main id="main">
<div class="wrap page-head">
<p class="crumbs"><a href="../">Inicio</a> › {a['nombre']}</p>
<h1>{a['h1']}</h1><span class="rule"></span>
<p class="lead">{a['intro']}</p>
</div>
<section style="padding-top:20px"><div class="wrap two">
<div>
<h2>En qué podemos ayudarte</h2>
<ul class="check">{items}</ul>
<h2 style="margin-top:44px">Cómo trabajamos</h2>
<ol class="steps">
<li><strong>Te escuchamos.</strong> Nos contás tu situación y la documentación que tengas.</li>
<li><strong>Analizamos tu caso.</strong> Revisamos los datos y evaluamos qué opciones existen.</li>
<li><strong>Te explicamos con claridad.</strong> Te contamos los pasos, los tiempos estimados y los honorarios antes de avanzar.</li>
</ol>
<p style="margin-top:28px;font-weight:300">Atendemos en San Salvador de Jujuy, en El Carmen y a distancia, en toda la Provincia de Jujuy.</p>
<h2 style="margin-top:44px;font-size:1.4rem">Otras áreas del Estudio</h2>
<div class="others">{otros}</div>
</div>
<aside class="aside"><h2>Consultanos</h2><p>Contanos tu caso por WhatsApp y te respondemos para coordinar una consulta con las abogadas del Estudio.</p>
<a class="btn" href="{wa(a['msg'])}" target="_blank" rel="noopener">{WA_SVG}Escribir por WhatsApp</a>
<p style="margin:18px 0 0;font-size:.9rem">{TEL_VISIBLE} · Toda la Provincia de Jujuy</p></aside>
</div></section>
</main>
"""
    s += footer(1, "es")
    write(f"{a['slug']}/index.html", s)

# ---------------- ENGLISH ----------------
def english():
    title = "Lawyers in Jujuy, Argentina | Legal help from abroad | GM & Asociados"
    desc = "Law firm in San Salvador de Jujuy and El Carmen, Argentina. Legal help for foreigners, companies and Argentines abroad: trademarks, companies, inheritance, property."
    sch = schema_org([{"@type": "WebPage", "@id": f"{BASE}/en/#page", "url": f"{BASE}/en/", "name": title, "description": desc, "inLanguage": "en", "isPartOf": {"@id": f"{BASE}/#web"}, "about": {"@id": f"{BASE}/#estudio"}},
                      breadcrumb([("Home", f"{BASE}/"), ("English", f"{BASE}/en/")])])
    wa_en = wa("Hello, I am writing from another country and need legal help in Jujuy, Argentina.")
    team = "".join(f"""<article class="mem"><div class="ring"><div class="arch"><img src="../img/{e['img']}" alt="{esc(e['alt'])}" style="object-position:{e['pos']}" loading="lazy" width="640" height="800"></div></div>
<h3>{e['nombre']}</h3><p class="mp">Lawyer · Professional reg. M.P. {e['mp']}</p>
<a class="btn sm" href="{wa('Hello, I would like to talk with ' + e['corto'] + '.')}" target="_blank" rel="noopener">{WA_SVG}Message {e['corto']}</a></article>""" for e in EQUIPO)
    areas = [("Companies and trademarks", "Register a trademark or patent, set up or restructure a company (SAS, SRL, SA) and draft contracts in Argentina."),
             ("Inheritance and property", "Successions, deeds and regularization of property in Jujuy for families living abroad."),
             ("Family matters", "Divorce, child support and parenting arrangements when one of the parties is outside Argentina."),
             ("Criminal, labor and accidents", "Criminal defense, labor claims, accident and damage claims in the Province of Jujuy.")]
    arow = "".join(f'<a href="{wa_en}" target="_blank" rel="noopener" style="grid-template-columns:minmax(0,1fr) minmax(0,1.6fr)"><strong>{n}</strong><span>{d}</span></a>' for n, d in areas)
    s = head(title, desc, "en/", 1, "en", sch, alternates=[("es-AR", ""), ("en", "en/"), ("x-default", "")])
    s += header(1, "en", ("../", "es", "Español"))
    s += f"""<main id="main">
<section class="hero"><div class="wrap grid">
<div>
<h1>Lawyers in Jujuy, Argentina: your legal gateway from abroad</h1><span class="rule"></span>
<p class="lead">If you or your company need something legal done in Jujuy and you are in another country, we can help you from first message to final paperwork.</p>
<div class="acts"><a class="btn" href="{wa_en}" target="_blank" rel="noopener">{WA_SVG}Message us on WhatsApp</a><a class="btn sec" href="#areas">See what we do</a></div>
<p class="meta">Offices in <strong>San Salvador de Jujuy</strong> and <strong>El Carmen</strong>, Province of Jujuy, northwest Argentina.</p>
</div>
<div class="ring hero-ring"><div class="arch"><img src="../img/equipo.jpg" alt="The three lawyers of GM &amp; Asociados law firm in Jujuy, Argentina" width="900" height="805" fetchpriority="high" style="object-position:50% 30%"></div></div>
</div></section>

<section class="alt" id="how"><div class="wrap">
<h2>Who we help</h2>
<ul class="check" style="max-width:760px">
<li><strong>Foreigners and foreign companies</strong> that want to register a trademark, open a company or sign contracts in Argentina.</li>
<li><strong>Argentines living abroad</strong> with an inheritance, a property or a procedure pending in Jujuy.</li>
<li><strong>Families</strong> who need a trusted lawyer to handle a matter in Jujuy on their behalf.</li>
</ul>
<h2 style="margin-top:44px">How it works</h2>
<ol class="steps" style="max-width:760px">
<li><strong>Write to us.</strong> Tell us your country and what you need. WhatsApp or email.</li>
<li><strong>We review your case.</strong> We explain the options, the steps and the fees before moving forward.</li>
<li><strong>We handle it in Jujuy.</strong> You stay informed from wherever you are.</li>
</ol>
</div></section>

<section id="areas"><div class="wrap"><h2>Practice areas</h2><p class="lead">Business law is our main specialty. We also cover:</p>
<div class="areas">{arow}</div></div></section>

<section class="alt" id="team"><div class="wrap"><h2>Our team</h2><div class="team">{team}</div></div></section>

<section class="band" id="contact"><div class="wrap">
<h2>Contact</h2>
<p>San Salvador de Jujuy: Independencia 658, 1st floor, Office 1.<br>El Carmen: Sarmiento 520, Barrio Centro.<br>WhatsApp: <a href="https://wa.me/{WA}">+54 9 388 478-3935</a> · <a href="mailto:{MAIL}">{MAIL}</a></p>
<p style="margin-top:22px"><a class="btn" href="{wa_en}" target="_blank" rel="noopener">{WA_SVG}Message us on WhatsApp</a></p>
</div></section>
</main>
"""
    s += footer(1, "en")
    write("en/index.html", s)

def extras():
    urls = [("", "1.0")] + [(a["slug"] + "/", "0.8") for a in AREAS] + [("en/", "0.7")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for u, p in urls:
        sm += f"<url><loc>{BASE}/{u}</loc><lastmod>{HOY}</lastmod><priority>{p}</priority>"
        if u in ("", "en/"):
            sm += f'<xhtml:link rel="alternate" hreflang="es-AR" href="{BASE}/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}/en/"/>'
        sm += "</url>\n"
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write("style.css", CSS.strip() + "\n")
    write(".nojekyll", "")
    nf = head("Página no encontrada | Estudio GM & Asociados", "Página no encontrada.", "404.html", 0, "es").replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">').replace('href="style.css"', f'href="{BASE}/style.css"')
    nf += f'<main id="main" class="wrap" style="padding:90px 0"><h1>No encontramos esa página</h1><span class="rule"></span><p class="lead">Volvé al inicio o escribinos por WhatsApp.</p><p style="margin-top:24px"><a class="btn" href="{BASE}/">Ir al inicio</a></p></main></body></html>'
    write("404.html", nf)

home()
for a in AREAS:
    area_page(a)
english()
extras()
print("OK", BASE)
