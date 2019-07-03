from distutils.core import setup

def load_requirements():
    with open("requirements.txt") as req:
        return req.readlines()

setup(
    name='blu',
    version='0.1dev',
    install_requires=load_requirements(),
    entry_points={
        'console_scripts': [
            "blu_server=blu.main:server",
            'blu_console=blu.main:console'
        ],
    }
)
