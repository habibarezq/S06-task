from setuptools import find_packages, setup

package_name = 'pkg_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='habiba-rezq',
    maintainer_email='habibarezq30@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "temp_node=pkg_py.temp_node:main",
            "collector=pkg_py.collector:main",
            "pressure=pkg_py.pressure:main",
            "humidity=pkg_py.humidity:main",
            "server=pkg_py.server:main"
        ],
    },
)
