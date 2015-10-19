from setuptools import setup

setup(name='pyeventick',
      version='0.2',
      description='Simple integrate of API eventick.com.br with python',
      url='https://github.com/hudsonbrendon/pyeventick',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['pyeventick'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
