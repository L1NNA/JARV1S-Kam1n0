# JARV1S-Kam1n0
![Kam1n0 Packaging](https://github.com/L1NNA/JARV1S-Kam1n0/workflows/Kam1n0%20Packaging/badge.svg)

Direct connector for Kam1n0 batch mode. Latest batch-enabled jar will be downloaded automatically (built by GitHub action of this repository). JDK8 will be downloaded if necessary. 

### :fire: Installation:
```
pip install git+https://github.com/L1NNA/JARV1S-Kam1n0@master
```

### 👊 CLI usage:
```
python -m kam1n0
usage: __main__.py [-h] [dir] [{asmclone,asm2vec,asmbin2vec,sym1n0}]

positional arguments:
  dir                   The folder that contians binaries.
  {asmclone,asm2vec,asmbin2vec,sym1n0}
                        The model to be used.

optional arguments:
  -h, --help            show this help message and exit
```

### 🌵 Used in `requirements.txt`:
```
git+https://github.com/L1NNA/JARV1S-Kam1n0@master
```

### 📖 Current Commit Tag of the Distribution
This is used to track which version is built in GitHub Action and used to trigger the build.
```
commit 07b05e2c96b44681a1e6aaf138d772464f47679f
```

### :star: Contributors:
- Steven Ding - Queen's Computing
- Miles Li - McGill University
