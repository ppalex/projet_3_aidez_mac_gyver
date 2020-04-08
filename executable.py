"""Installation file for script app.py."""

from cx_Freeze import setup, Executable


setup(
    name="application",
    version="0.1",
    description="Projet mac_gyver",
    executables=[Executable("app.py")],
)
