# qu-ai-wei

[简体中文](../README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · [한국어](./README.ko.md) · Español

qu-ai-wei reescribe un texto en su idioma original. Puede reorganizar frases, párrafos, títulos y textos largos, pero conserva los hechos, cifras, citas, grado de certeza, formato y voz del autor.

El chino simplificado y el inglés tienen reglas propias. El chino tradicional, el español, el japonés y los demás idiomas parten de un núcleo común y se ajustan después a la gramática, el contexto de publicación y las muestras del autor.

![qu-ai-wei elimina fórmulas vacías de un texto chino y conserva los hechos](../assets/demo.gif)

## Instalación

Con Node.js y npm instalados, ejecuta:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

Después, abre una sesión nueva o vuelve a cargar los skills según la herramienta que uses.

## Uso

```text
Usa qu-ai-wei para que este texto suene natural en español. Conserva todos los hechos y devuelve solo el texto final:

[pega aquí el texto]
```

Si el trabajo incluye una traducción, traduce primero y usa qu-ai-wei sobre el texto traducido.

## En qué se fija

Primero registra los hechos, las afirmaciones, las personas gramaticales, las citas, el código, las rutas, los enlaces y los datos legibles por máquina que debe conservar. Luego comprueba qué función cumple cada párrafo. La revisión deja el vocabulario y la puntuación para el final.

Las reglas compartidas están en [`cross-language-core.md`](../references/cross-language-core.md). El inglés y el chino simplificado añaden sus propias capas. La narrativa, las notas de versión, los PR, las incidencias y los informes técnicos siguen guías específicas para su contexto.

Las reglas sobre `-ing`, artículos, pasivas y em dashes permanecen en la capa de inglés.

## Revisión estricta

Cuando el encargo pide una limpieza a fondo, o el texto es el README o la documentación de un humanizer, qu-ai-wei revisa uno por uno los adverbios, las pasivas, las rayas y los ritmos enfáticos. El texto final conserva los elementos que aportan tiempo, grado, evidencia, responsabilidad, gramática, ritmo o voz.

## Entrega y alcance

El modo normal devuelve el texto revisado con una nota breve. El modo integrado entrega solo el texto final. El modo archivo edita la prosa autorizada y conserva bloques de código, frontmatter, comandos, identificadores, rutas, destinos de enlaces y datos.

qu-ai-wei se ocupa de revisar textos existentes sin cambiar de idioma. La traducción, la redacción desde cero, la corrección ortográfica aislada y la identificación del autor o del modelo son tareas distintas. Los hechos, opiniones, experiencias y juicios profesionales del resultado proceden del original o de materiales autorizados por el usuario.

Sustituye las credenciales por `[REDACTED]` antes de compartir el texto. En centros educativos, revistas, plataformas y empresas, sigue las normas de divulgación y uso de IA que correspondan.

## Método y licencia

El método usa [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Humanizer](https://github.com/blader/humanizer), [Humanizer-zh](https://github.com/op7418/Humanizer-zh), [Sepia](https://github.com/Nanako0129/sepia), [stop-slop](https://github.com/hardikpandya/stop-slop) y [claudish-to-english](https://github.com/gvzdv/claudish-to-english). qu-ai-wei comprueba cada señal en el texto concreto antes de editar.

Las reglas completas están en [SKILL.md](../SKILL.md). El proyecto usa la [licencia MIT](../LICENSE).
