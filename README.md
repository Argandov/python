# python learning
All things python
+ Learning Data structures & algorithms

---

# PYTHON DEBUGGERS

`pip3 install ipdb`

Usage:

`python -m ipdb my_program.py`

Used Like gdb

# LINTERS IN VIM:

ALE tools (Linter, fixer)

Install linters sepparatedly (i.e. apt install flake8)

In .vimrc: `let g:ale_linters = {'python': ['flake8']}`

Activate/deactivate ALE inside vim: `ALEToggle`

# Custom python interactive prompt:

```python
#!/usr/bin/python3

import sys
import sys
sys.ps1 = "\033[1;33m>>>\033[0m "

```

Initialization every time python (interactive) starts:

```bash
export PYTHONSTARTUP=$HOME:this_file.py
```
