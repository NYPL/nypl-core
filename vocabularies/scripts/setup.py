from setuptools import setup

print "Installing dependencies for serialize scripts"

setup(name='serializescripts',
      version='1.0.0',
      description='Various scripts for serializing CSV to JSON-LD',
      author='Shawn Averkamp',
      license='MIT',
      install_requires=[
          'rdflib',
          'rdflib-jsonld',
      ])
