## [v1.0.0] – 2026-03-27

### Added

- Shows version at startup
- Interactive input loop
- New commands:
  - version → shows current n0cli version
  - exit → closes interactive CLI
  - 
### Changed

- CLI now requires commands to be entered at prompt
- 
### Breaking

- Old direct-command usage (`python main.py [command] [optional: args]`) replaced by interactive prompt

### Note

- To start n0cli, run `python main.py`
- Then enter commands at the prompt: `n0cli CMD >`