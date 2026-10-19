# Getting started

```bash
git clone https://github.com/victor-harden/victorhub.git
cd victorhub
python3 -m victorhub.cli status
```

## First commands

```bash
python3 -m victorhub.cli plugins
python3 -m victorhub.cli profile add --name victor --role admin
python3 -m victorhub.cli emit --type login --actor victor
python3 -m victorhub.cli events
```

Data lives under `~/.victorhub` by default; pass `--data-dir` to keep it
somewhere else.
