import rich.traceback; rich.traceback.install()
import rich.console; console = rich.console.Console()

import os
import sys

from printVars import echo

ROOT = os.getenv("ROOT")

def main():
    echo(ROOT)
    pass




if __name__ == "__main__":
    main()
