# n0cli

### simple command line tools

## Starting n0cli

Currently, to run n0cli, execute:

```bash
python main.py
```

You will see the interactive prompt:

```
n0cli CMD >
```

Type `exit` or `quit` to quit.

## Commands

| Command           | Description                                                  |
|-------------------|--------------------------------------------------------------|
| `hello`           | Prints a greeting message including the n0cli version.       |
| `time`            | Shows the current date and time.                             |
| `hash <text>`     | Calculates SHA-256 hash of the provided text.                |
| `gen <length>`    | Generates a random alphanumeric string of given length.      |
| `version`         | Shows the current n0cli version (also displayed at startup). |
| `exit` / `quit`   | Exits the interactive CLI.                                   |

## Notes
- n0cli currently runs interactively via `python main.py`.
- All commands must be entered at the `n0cli CMD >` prompt.
- Version `v1.0.0` introduces the interactive CLI and replaces the old direct-command usage: `python main.py [command] [optional: args]` with the new interactive prompt.

## Contributing
- Feel free to submit bug reports or feature requests via GitHub Issues. Pull requests are welcome too!
- Follow semantic versioning for new commits:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `BREAKING:` for major changes that affect existing usage