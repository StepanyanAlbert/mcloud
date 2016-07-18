<<<<<<< HEAD
#!/usr/bin/env python3.5
=======
#!/usr/bin/env python
>>>>>>> 48a22e972706e483092587876eb19290600e8f8d
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcloud.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
