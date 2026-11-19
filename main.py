"""news-image-20261119-entry-v2: copy the pre-rendered entry image to the output dir.

Stdlib only. No network. Reads MAKEFUN_OUTPUT_DIR (default /output) and
copies entry.png (sitting next to this file) to <output>/entry.png.
Never deletes the output directory itself.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s" % dst)


if __name__ == "__main__":
    sys.exit(main())
