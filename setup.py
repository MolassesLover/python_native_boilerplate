import shutil
import subprocess
from setuptools import setup
from Cython.Build import cythonize

cmake_flags:str = "-D CMAKE_BUILD_TYPE=Release"

commands:list[str] = [
    "swig -python -o src/native/bindings/example_module.c src/native/bindings/example.i",
    f"cmake -B build {cmake_flags}",
    "cmake --build build -j$(nproc)",
    "cp build/lib.*/bindings/example.*.so build/",
    "cp src/cli.py build/cli.py"
]

setup(
    ext_modules = cythonize("src/native/bindings/example.py")
)

for command in commands:
    subprocess.run(command, check=True, shell=True)
