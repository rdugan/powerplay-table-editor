import setuptools
import os

headless = os.environ.get("HEADLESS", None)
deps = [
    'npyscreen @ git+https://github.com/rdugan/npyscreen@develop#egg=npyscreen-5.0.0'
]
entry_points={
    'console_scripts': [
        'amdgpu-pptable-to-json=amdgpu_pptable.dump:main',
        'amdgpu-pptable-tui=amdgpu_pptable.tui:main'
    ]
}
if not headless: 
    deps.append('PyQt5')
    entry_points['gui_scripts'] = 'amdgpu-pptable-gui=amdgpu_pptable.gui:main'

setuptools.setup(
    name='amdgpu-pptable',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=deps,
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    entry_points=entry_points,
    python_requires='>=3.6',
    use_scm_version={'write_to': 'src/amdgpu_pptable/version.py'}
)
