# VictorHub

VictorHub is a small platform for personal automation: a plugin registry, a
profile store and an append-only event log behind one CLI.

## The pieces

- **victorhub** — the core package and CLI.
- **victorhub-plugin-sdk** — plugin contracts and a hook bus.
- **victorhub-profile-manager** — profiles as JSON.
- **victorhub-event-log** — JSON Lines events.
- **victorhub-web** — a static dashboard over the exported state.

## Design principles

1. Files over services: JSON and JSONL you can read and copy.
2. No hidden state: every command is explicit.
3. Small modules with tests, not one large application.
