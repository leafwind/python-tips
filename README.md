# python-tips

Some trouble shooting / tips for python.

## Genaral

### `virtualenv --no-site-packages` and pip still finding global packages?

#### root cause

`PYTHONPATH` detected

#### sol

check if your `.bashrc` contains `PYTHONPATH`


### virtualenv got import error after upgrading OS version (e.g. ubuntu 12.04 to 14.04)

#### root cause

system library changed and not match with the virtualenv one

#### sol

remove virtualenv dir and rebuild it.

## nose

### no module named [project dir]

#### sol:
```
cd [project dir]; rm __init__.py
```

### nocapture feature

```
nosetests --nocapture test.py
```
