"""Installation file for script app.py."""

from cx_Freeze import setup, Executable


setup(
    name="application",
    version="0.1",
    description="Projet mac_gyver",

    options={"build_exe": {"packages": ["pygame", "random", "sys"],
                           "include_files": ["images", "data"]}},
    executables=[Executable("app.py", base="Win32GUI")]
)
