
from agents.linguist import Linguist

lyrics = """
Sí, sabes que ya llevo un rato mirándote
Tengo que bailar contigo hoy (DY)
Vi que tu mirada ya estaba llamándome
Muéstrame el camino que yo voy (Oh)
Tú, tú eres el imán y yo soy el metal
Me voy acercando y voy armando el plan
Solo con pensarlo se acelera el pulso (Oh, yeah)
Ya, ya me está gustando más de lo normal
Todos mis sentidos van pidiendo más
Esto hay que tomarlo sin ningún apuro
Despacito
Quiero respirar tu cuello despacito
Deja que te diga cosas al oído
Para que te acuerdes si no estás conmigo
Despacito
Quiero desnudarte a besos despacito
Firmar las paredes de tu laberinto
Y hacer de tu cuerpo todo un manuscrito (Sube, sube, sube)
(Sube, sube)
Quiero ver bailar tu pelo
Quiero ser tu ritmo
Que le enseñes a mi boca
Tus lugares favoritos (Favoritos, favoritos, baby)
Déjame sobrepasar tus zonas de peligro
Hasta provocar tus gritos
Y que olvides tu apellido (Diridiri, dirididi Daddy)
"""

l = Linguist()
analysis = l.analyze_lyrics(lyrics)

print("Found Level 1 Verbs:", list(analysis['verb_sentence_map'].keys()))
print("\nEntries:")
for v, entries in analysis['verb_sentence_map'].items():
    print(f"{v}: {entries}")
