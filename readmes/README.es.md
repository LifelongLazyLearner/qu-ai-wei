# qu-ai-wei

[简体中文](../README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | Español

> ⚠️ **Versión 0.x en desarrollo:** Las reglas, las categorías y las interfaces todavía pueden cambiar. Puedes enviar comentarios mediante [issues](https://github.com/LifelongLazyLearner/qu-ai-wei/issues), [discussions](https://github.com/LifelongLazyLearner/qu-ai-wei/discussions) o pull requests.

qu-ai-wei es un agent skill que revisa borradores generados por IA en **chino simplificado**. Hace que el texto suene más natural sin cambiar los hechos, el significado, el nivel de formalidad ni la voz del original.

El README está disponible en varios idiomas, pero el skill edita textos cuyo idioma principal es el chino simplificado. Conserva los nombres de producto, términos técnicos, abreviaturas y demás expresiones insertadas cuando son necesarias.

## Demostración

![qu-ai-wei elimina fórmulas vacías y conserva los hechos de un borrador en chino simplificado](../assets/demo.gif)

El ejemplo elimina una introducción genérica, una fórmula enfática innecesaria y un eslogan, pero conserva los dos hechos del original. Los límites de edición se explican en [`references/examples.md`](../references/examples.md).

## Instalación

Con Node.js y npm instalados, ejecuta:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

El `skills` CLI externo detectará las herramientas de programación con IA compatibles instaladas en el equipo.

## Uso

Después de instalarlo, inicia una sesión nueva o vuelve a cargar los skills según las instrucciones de tu herramienta. A continuación, escribe:

```text
/qu-ai-wei

[pega aquí un texto en chino simplificado]
```

En el modo normal, qu-ai-wei primero comprueba si conviene editar el texto y después entrega un borrador, una revisión, la versión final y un informe de pulido. No modifica textos que ya parecen escritos de forma natural por una persona y pregunta cuando no puede determinar el contexto o el nivel de formalidad.

## Solo el texto final

Si qu-ai-wei forma parte de un flujo de trabajo más amplio, solicita el embedded mode:

```text
Usa qu-ai-wei para revisar la siguiente descripción de un PR y devuelve únicamente el texto final:

[pega aquí un texto en chino simplificado]
```

El embedded mode ejecuta las mismas comprobaciones internas. Solo devuelve el texto final cuando puede revisarlo de forma segura; si el original ya parece escrito por una persona o falta contexto, conserva el texto, pregunta o explica el bloqueo. No concede permiso para escribir archivos, hacer commits, publicar ni enviar contenido.

## Límites

qu-ai-wei no traduce ni escribe desde cero, no inventa opiniones o detalles ausentes, no sustituye la voz propia de una persona y no ayuda a eludir políticas sobre el uso de IA.

Consulta [SKILL.md](../SKILL.md) para ver todas las reglas de ejecución. El método se inspira en [humanizer](https://github.com/blader/humanizer), y las reglas sobre calcos del inglés en chino toman como referencia [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html). Publicado bajo la [Licencia MIT](../LICENSE).
