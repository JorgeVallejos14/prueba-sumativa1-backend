from django.shortcuts import render
from django.http import Http404

# Create your views here.
JUEGOS = [
    {"id": 1, "titulo": "Caminos del Norte", "plataforma": "PC", "precio": 24990,
     "horas": 30, "multijugador": False, "oferta": False,
     "descripcion": "Aventura de mundo abierto por el desierto de Atacama, con misiones en pueblos mineros y caletas."},
    {"id": 2, "titulo": "Arena Fantasma", "plataforma": "PlayStation 5", "precio": 44990,
     "horas": 15, "multijugador": True, "oferta": False,
     "descripcion": "Batallas en linea de hasta 8 jugadores en arenas que cambian con la marea."},
    {"id": 3, "titulo": "Salar Kart", "plataforma": "Nintendo Switch", "precio": 39990,
     "horas": 12, "multijugador": True, "oferta": True,
     "descripcion": "Carreras por las rutas del salar con hasta 4 jugadores en pantalla dividida."},
    {"id": 4, "titulo": "Ecos de la Mina", "plataforma": "Xbox Series", "precio": 29990,
     "horas": 25, "multijugador": False, "oferta": True,
     "descripcion": "Terror psicologico en una mina abandonada. Cada decision cambia el final."},
    {"id": 5, "titulo": "Cumbre Andina", "plataforma": "PC", "precio": 19990,
     "horas": 40, "multijugador": False, "oferta": False,
     "descripcion": "Simulador de expediciones de montana con clima dinamico y gestion de recursos."},
    {"id": 6, "titulo": "Liga Pixel", "plataforma": "PlayStation 5", "precio": 34990,
     "horas": 8, "multijugador": True, "oferta": True,
     "descripcion": "Futbol arcade con equipos de barrio y torneos en linea de temporada."},
    {"id": 7, "titulo": "El ultimo faro", "plataforma": "Nintendo Switch", "precio": 14990,
     "horas": 10, "multijugador": False, "oferta": True,
     "descripcion": "Puzzles de luz y sombra dentro de un faro que guarda un secreto."},
    {"id": 8, "titulo": "Fortaleza Costera", "plataforma": "Xbox Series", "precio": 49990,
     "horas": 20, "multijugador": True, "oferta": False,
     "descripcion": "Estrategia cooperativa: defiende el puerto con hasta 4 amigos."},
]

def inicio(request):
    precio_promedio = sum(juego["precio"] for juego in JUEGOS) / len(JUEGOS)
    cantidad_en_oferta = sum(1 for juego in JUEGOS if juego["oferta"])
    contexto = {
        "juegos": JUEGOS,
        "total": len(JUEGOS),
        "precio_promedio": precio_promedio,
        "cantidad_en_oferta": cantidad_en_oferta,
    }
    return render(request, "tienda/inicio.html", contexto)


def detalle(request, id):
    juego = next((juego for juego in JUEGOS if juego["id"] == id), None)
    if juego is None:
        raise Http404("Juego no encontrado")
    descuento = 0.20 if juego["oferta"] else 0
    juego = {
        **juego,
        "precio_descuento": juego["precio"] * (1 - descuento),
        "etiqueta": "Oferta - 20% de descuento" if juego["oferta"] else "Precio normal",
    }
    return render(request, "tienda/detalle.html", {"juego": juego})