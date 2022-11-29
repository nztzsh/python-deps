from setuptools import setup

def setup_package():
    ext_modules = []
    print("Cythonizing sources")

    setup(
        name="endorsetupcfg",
        version='5.4.7',
        ext_modules=ext_modules,
        package_data={"": ["*.pyx", "*.pxd", "*.pxi", "*.cu", "*.hh"]},
    )


if __name__ == "__main__":
    setup_package()
