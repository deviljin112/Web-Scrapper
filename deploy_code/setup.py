from setuptools import setup

setup(
    name="ITJobWatch_scrapper",
    version="0.1",
    packages=["sqlite3"],
    url="https://github.com/deviljin112",
    license="",
    author="D3v",
    author_email="hswic@spartaglobal.com",
    description="",
    install_requires=["requests", "beautifulsoup4", "flask", "flask-login", "flask-sqlalchemy"],
)
