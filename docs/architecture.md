# Architecture

```text
          Inbox
            |
            v

      AI Analysis Layer
   /        |         \
Tasks    Meetings   Documents

            |
            v

      Priority Engine

            |
            v

      Executive Briefs
```

## Design principles

- Public-safe from the beginning
- No personal data required
- Explainable scoring logic
- API-first architecture
- Easy extension to future model providers

## Future AI layer

A future `ai_service.py` module could connect to an approved model provider. The current version keeps logic local and transparent for portfolio review.
