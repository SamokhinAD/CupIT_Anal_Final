from setuptools import setup, find_packages

setup(
    name="cupIT_ravens_lib",              # Имя библиотеки
    version="0.1.0",                # Версия
    packages=find_packages(),       # Автоматически находит модули
    install_requires=[],            # Зависимости (если есть)
    author="ravens",
    author_email="antonsamoh0704@gmail.com",
    description="Библиотека CupIT final",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SamokhinAD/CupIT_Anal_Final.git",  # Ссылка на GitHub (если есть)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)