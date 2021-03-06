from distutils.core import setup, Extension

qubit_hash_module = Extension(
    'qubit_hash',
    sources = [
        'qubitmodule.c',
        'qubit.c',
        'sha3/cubehash.c',
        'sha3/echo.c',
        'sha3/luffa.c',
        'sha3/simd.c',
        'sha3/shavite.c'],
    include_dirs=['.', './sha3'])

setup (name = 'qubit_hash',
       version = '1.0',
       description = 'Bindings for proof of work used by QubitCoin',
       ext_modules = [qubit_hash_module])
