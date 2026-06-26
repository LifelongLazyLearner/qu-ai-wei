# qu-ai-wei

[简体中文](../README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | Español

qu-ai-wei es un agent skill para reducir el tono de texto generado por IA en **chino simplificado**. Ayuda a convertir un borrador en chino simplificado que suena claramente a IA en un texto más limpio y natural, sin cambiar los hechos ni la intención original.

La documentación canónica es el [README en chino simplificado](../README.md). Este archivo es solo una orientación breve para lectores en español.

https://github.com/user-attachments/assets/24513c20-968d-437b-8ceb-1ac1f77f6ad6

## Para Qué Sirve

- Limpia rastros visibles de escritura de IA en borradores en chino simplificado: frases genéricas, estructura mecánica, tono demasiado pulido y chino con sabor a traducción.
- Pule de forma ligera la redacción, el ritmo y la concreción cuando la información ya está en el texto fuente.
- Ayuda a escritores, editores, equipos de contenido, product managers, estudiantes y desarrolladores a que su escritura cotidiana en chino simplificado parezca menos un primer borrador de IA.

## Límite Importante

qu-ai-wei **solo admite chino simplificado**.

No humaniza inglés, japonés, coreano, español, chino tradicional ni textos mezclados en varios idiomas. El chino tradicional tiene otros patrones de tono IA, preferencias léxicas y normas tipográficas, por lo que necesita un conjunto de reglas separado.

Tampoco es una herramienta para evadir detectores de IA. Úsala para mejorar textos de los que eres responsable, no para ocultar autoría.

## Qué Puede y Qué No Puede Hacer

Puede:

- Quitar patrones evidentes de chino simplificado que suenan a IA.
- Conservar hechos, intención y registro general.
- Detenerse o actuar con cautela cuando el texto parece ya escrito por una persona, está en chino tradicional, o pertenece a contextos legales, administrativos u otros donde reescribir sería riesgoso.

No puede:

- Inventar ideas originales, entrevistas, detalles o un punto de vista más fuerte.
- Convertir material débil en escritura de nivel revista.
- Reescribir textos que no estén en chino simplificado.

## Instalación

El mismo script de instalación admite Cursor, Claude Code, OpenAI Codex CLI, OpenCode, Kiro, Factory Droid, Slate y Hermes.

Si tienes Node/npm, la ruta recomendada es el `skills` CLI externo. Por defecto detecta los agents disponibles, o te pide elegir uno si no detecta ninguno:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

Este método usa el `skills` CLI externo para traer este repositorio de GitHub. No es un paquete npm de qu-ai-wei.

Para instalarlo en agents concretos, añade `-a`:

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -a codex
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -a codex -a claude-code -a cursor
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -g -a codex -y
```

```bash
git clone https://github.com/LifelongLazyLearner/qu-ai-wei.git ~/qu-ai-wei
cd ~/qu-ai-wei

# Instalar en un agent
bash scripts/install-skill.sh --platform codex

# Instalar en todos los agents compatibles
bash scripts/install-skill.sh --platform all
```

## Uso

Para usuarios que no hablan chino, la opción más segura es llamar el skill de forma explícita y pegar texto en chino simplificado:

```text
/qu-ai-wei

[pega aquí texto en chino simplificado]
```

También puedes pegar el cuerpo de [SKILL.md](../SKILL.md) en las instrucciones personalizadas o el system prompt de un modelo de IA. Omite el YAML frontmatter del principio.

## Más Información

- Documentación completa: [README.md](../README.md)
- Reglas del skill: [SKILL.md](../SKILL.md)
- Referencias: [references/](../references/)
- Cambios: [CHANGELOG.md](../CHANGELOG.md)
- Licencia: [MIT](../LICENSE)
