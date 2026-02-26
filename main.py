"""
TerraMind - Main Entry Point
Author: TerraMind Project
Description: Launches the TerraMind CLI application.
"""

import sys
from cli import run


def main():
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
        print("Exiting TerraMind safely.\n")
        sys.exit(0)
    except Exception as e:
        print("\nUnexpected error occurred:")
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()