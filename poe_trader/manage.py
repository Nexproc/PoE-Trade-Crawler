#!/usr/bin/env python
import os
import sys
from poe_trader.settings import PROJECT_DIRNAME, PROJECT_ROOT

sys.path.append(os.path.abspath(os.path.join(PROJECT_ROOT, "..")))
# Run Django.
if __name__ == "__main__":
    settings_module = "%s.settings" % PROJECT_DIRNAME
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
