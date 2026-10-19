# victorhub-docs

Documentation set for the VictorHub platform, plus a checker that keeps it honest:
relative links must exist, every page needs a title, and navigation in
`mkdocs.yml` must point to real files.

## Contents

- `docs/index.md`: what VictorHub is and how the pieces fit.
- `docs/getting-started.md`: install and first commands.
- `docs/architecture.md`: modules, plugin lifecycle and event flow.
- `docs/plugins.md`: writing a plugin.
- `mkdocs.yml`: navigation for MkDocs.

## Features

- `check_docs.py` validates links, titles and navigation.
- Runs in CI, so broken docs fail the build.
- Works without MkDocs installed; MkDocs is optional for rendering.

## Installation

```bash
git clone https://github.com/victor-harden/victorhub-docs.git
cd victorhub-docs
```

## Usage

```bash
python3 check_docs.py
python3 check_docs.py --json
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT — see [LICENSE](LICENSE).
