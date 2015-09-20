from setuptools import setup

setup(name='fretwork',
        version='0.0.1',
        description='Game library used by FoFiX, and FoF:R.',
        author='Matthew Sitton',
        author_email='matthewsitton@gmail.com',
        license='GPLv2+',
        url='https://github.com/fofix',
        packages=['fretwork'],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Topic :: Multimedia :: Graphics',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
        ],
        keywords='music engine fofix frets game',
        install_requires=['Pillow', 'cython', 'pygame', 'OpenGL', 'numpy']
     )