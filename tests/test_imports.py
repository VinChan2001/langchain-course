from importlib import import_module
from os import environ
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch


class LessonImportsTest(TestCase):
    def test_root_python_files_import(self):
        project_root = Path(__file__).resolve().parents[1]

        with patch.dict(environ, {"PYTHON_DOTENV_DISABLED": "1"}):
            for script in sorted(project_root.glob("*.py")):
                with self.subTest(script=script.name):
                    import_module(script.stem)
