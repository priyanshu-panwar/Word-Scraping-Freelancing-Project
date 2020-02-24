from setuptools import find_packages, setup
from setuptools.command.develop import develop as _develop


class InstallDeps(_develop):

    def run(self):
        import os.path
        import nltk

        _develop.run(self)

        nltk_dependencies = {'tokenizers': 'punkt',
                             'taggers': 'averaged_perceptron_tagger'}
        for path, name in nltk_dependencies.items():

            try:
                path = os.path.join(path, name)
                nltk.data.find(path)
            except LookupError:
                nltk.download(name)


setup(
    name='word-scraper-counter',
    version='0.0.1',
    author='Constverum',
    author_email='constverum@gmail.com',
    cmdclass={
        'develop': InstallDeps,
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'wheel==0.29.0',
        'django==1.10.5',
        'nltk==3.2.2',
        'pandas==0.19.2',
        'matplotlib==2.0.0',
        'seaborn==0.7.1',
        'scipy==0.18.1',
        'nose==1.3.7',
        'django-nose==1.4.4',
        'nosedjango==1.0.13',
    ],
    test_suite='tests',
    tests_require=['nose'],
)
