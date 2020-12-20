from setuptools import setup

setup(
    name="Web-Scrapper",
    version="0.1",
    packages=["sqlite3"],
    url="https://github.com/deviljin112",
    license="OpenSource",
    author="Deviljin112",
    author_email="hswic@spartaglobal.com",
    description="A Flask-based, deployment-ready web-scrapper written in Python.",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "flask",
        "flask-login",
        "flask-sqlalchemy",
    ],
)
