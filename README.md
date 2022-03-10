# pants-cython-minimal-example
Minimal project showcasing Pants' Cython support

## Project Structure

`src/python/app` contains a minimal Python project.
It has a `pex_binary` target.

`src/python/my_extensions` contains minimal Cython sources (the code is from [their example](https://cython.readthedocs.io/en/latest/src/quickstart/build.html#building-a-cython-module-using-setuptools)).

The goal is to use the `hello` wheel as a dependency of `app`.

## Building the Cython package

Running `./pants package src/python/my_extensions:dist` will build the Wheel at `dist/dist-0.0.1-cp38-cp38-linux_x86_64.whl`

`pip install dist/dist-0.0.1.tar.gz` will install the `hello` package in the current environment.

```python
>>> import hello
>>> hello.say_hello_to("Cython")
# if "NOT COMPILED" is printed here, for some reason the code is interpreted
Hello Cython!
```

