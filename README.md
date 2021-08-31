# replace_dollar

Replace the Tex commands `$...$` and `$$...$$` by the LaTeX commands `\(...\)` and `\[...\]` in `.tex` files.

## Requirements

- Python version:

  - Tested on Python 3.9;
  - Might works on previous version of Python but not tested.

- OS:

  - Tested on Linux
  - Might works on Mac and Windows but not tested.

- For development require

  - [isort](https://github.com/PyCQA/isort)
  - [black](https://github.com/psf/black)
  - [mypy](https://github.com/python/mypy)
  - [pytest](https://github.com/pytest-dev/pytest)

## Instructions for use

Download or clone this repository then you can either use it directly or locally installed it via [Flit](https://github.com/takluyver/flit).

### Direct use

Go to the folder in which there is the `.tex` files you want to modify and use

```bash
python3 path_to_folder/replace_dollar/main.py file.tex
```

where `path_to_folder` is replace by the actual path to the folder `replace_dollar` and `file.tex` is the file you want to modify.

### Local installation

First, you need to install it via [Flit](https://github.com/takluyver/flit).
If you want to just use it, do

```bash
flit install --deps none --user
```

If you want to modify it and use it do

```bash
flit install --symlink --user
```

Then to use it do

```bash
python3 -m replace_dollar file.tex
```

where `file.tex` is the file you want to modify.

### How to use

When you call it on the file `file.tex`, it will create a backup file `file.tex.bak` so if the LaTeX compilation fail after the modification you can always go back to the unmodified file.

For more option refer to the help command with the option `-h`

```bash
usage: main.py [-h] [-p] [-c] filename [filename ...]

positional arguments:
  filename      the list of `.tex` files or
                `.` for all the `.tex` files in the current directory

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  add space to \( ... \) and newline to \[\n ... \n\]
                do nothing on \[ ... \] in commented section
```

## Pattern that does not works

- If there is `$` sign that does not correspond to inline math environment `$...$`.

- If there is `$$` sign that does not correspond to display math environment `$$...$$`.

- Nesting with inline math for example `$ \text{$x$} $`.

- Nesting with display math for example `$$ \text{$$x$$} $$`.

## Contact

If you have any questions or suggestions please feel free to create [an issue in this repository](https://github.com/zmoitier/replace_dollar/issues/new).
