# python learning
All things python
+ Learning Data structures & algorithms

---

# PYTHON DEBUGGERS

PDB: Default python debugger

`pdb my_program.py`
(Works almost exactly like gdb)

IPDB: "Improved python debugger" Super complete python debugger

`pip3 install ipdb`

Usage:
`python -m ipdb my_program.py`
Used Like gdb (For python scripts)

[PWNDBG](https://github.com/pwndbg/pwndbg) (Addition to gdb, for any binary)
- Add to ~/.gdbinit:
`source /path/pwndbg/gdbinit.py`


# LINTERS IN VIM:

ALE tools (Linter, fixer)

Install linters sepparatedly (i.e. apt install flake8)

In .vimrc: `let g:ale_linters = {'python': ['flake8']}`

Activate/deactivate ALE inside vim: `ALEToggle`

# Tracing program stats:

user|real|sys times, and use of resources

Install perf
`apt install perf`


A good script to benchmark and compare is [this one](https://github.com/Argandov/python/blob/main/exercises_lessons/generators_memory_test.py)

Example of use:

```bash
root@ubuntu:~# perf stat python3 shell.py
# sleep 2
# exit

 Performance counter stats for 'python3 shell.py':

             39.02 msec task-clock                #    0.003 CPUs utilized          
                27      context-switches          #    0.692 K/sec                  
                 9      cpu-migrations            #    0.231 K/sec                  
             1,758      page-faults               #    0.045 M/sec                  
        45,658,036      cycles                    #    1.170 GHz                    
        43,580,502      instructions              #    0.95  insn per cycle         
         9,649,258      branches                  #  247.296 M/sec                  
           428,845      branch-misses             #    4.44% of all branches        

      13.585309315 seconds time elapsed

       0.033763000 seconds user
       0.006815000 seconds sys
```

# Custom python interactive prompt:

Generate a file containing:

```python
#!/usr/bin/python3

import sys
import sys
sys.ps1 = "\033[1;33m>>>\033[0m "

```

Initialize it every time python (interactive) starts:

```bash
export PYTHONSTARTUP=$HOME:this_file.py
```
or put it into .bashrc
