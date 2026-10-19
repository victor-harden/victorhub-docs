# Architecture

```
CLI  ->  PluginRegistry
     ->  ProfileStore (JSON)
     ->  EventLog (JSONL)
```

## Plugin lifecycle

1. A plugin subclasses `Plugin` and declares `name` and `version`.
2. `register()` validates the instance, stores it and calls `activate(context)`.
3. `unregister()` calls `deactivate()` and removes it.

## Events

Every state change emits an event with `type`, `actor`, `payload` and a UTC
timestamp. The log is append-only; rotation is a separate operational concern.
