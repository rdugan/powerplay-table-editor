import setuptools


setuptools.setup(
    name='amdgpu-pptable',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyQt5',
        'npyscreen @ git+https://github.com/rdugan/npyscreen@develop#egg=npyscreen-5.0.0'
    ],
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    entry_points={
        'console_scripts': [
            'amdgpu-pptable-to-json=amdgpu_pptable.dump:main',
            'amdgpu-pptable-tui=amdgpu_pptable.tui:main'
        ],
        'gui_scripts': [
            'amdgpu-pptable-gui=amdgpu_pptable.gui:main',
        ]
    },
    python_requires='>=3.6',
    use_scm_version={'write_to': 'src/amdgpu_pptable/version.py'}
)
