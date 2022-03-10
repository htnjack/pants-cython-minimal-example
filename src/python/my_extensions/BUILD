python_sources()

resource(name="pyproject", source="pyproject.toml")
resources(name="pyx-sources", sources=["*.pyx"])

python_distribution(
    name="dist",
    dependencies=[
        ":pyproject",
        ":my_extensions",
        ":pyx-sources",
    ],
    provides=setup_py(
        name="hello-dist",
        version="0.0.1",
    ),
    wheel_config_settings={"--global-option": ["--python-tag", "py39"]},
    generate_setup = False,
)
