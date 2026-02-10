import importlib

import pytest

MODULES_TO_IMPORT = [
    "squadds",
    "squadds.calcs",
    "squadds.core",
    "squadds.database",
    "squadds.interpolations",
    "squadds.core.utils",
    "squadds.core.design_patterns",
    "squadds.core.analysis",
    "squadds.database.utils",
    "squadds.interpolations.interpolator",
    "squadds.calcs.qubit",
    "squadds.calcs.transmon_cross",
]


def import_with_status_message(module_name: str) -> None:
    try:
        importlib.import_module(module_name)
        print(f"Successfully imported {module_name}")
    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")
        raise
    except Exception as e:
        print(f"Error while importing {module_name}: {e}")
        raise


@pytest.mark.parametrize("module_name", MODULES_TO_IMPORT)
def test_import(module_name: str) -> None:
    import_with_status_message(module_name)
