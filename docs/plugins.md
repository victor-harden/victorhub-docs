# Writing a plugin

```python
from victorhub.plugins import Plugin


class HelloPlugin(Plugin):
    name = "hello"
    version = "1.0.0"

    def activate(self, context):
        print("hello from the plugin")

    def deactivate(self):
        print("bye")
```

Register it with `PluginRegistry().register(HelloPlugin())`.

## Rules

- One responsibility per plugin.
- Fail loudly in `activate` if a dependency is missing.
- Never write to another plugin's storage.
