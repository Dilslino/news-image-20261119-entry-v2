"""news-image-20261119-entry-v2: copy the pre-rendered entry image to the output dir.

Stdlib only. No network. Reads MAKEFUN_OUTPUT_DIR (default /output) and
copies entry.png (sitting next to this file) to <output>/entry.png.
Never deletes the output directory itself.
"""

import hashlib
import os
import shutil
import sys


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_hash = _sha256(src)
    dst_hash = _sha256(dst)
    if src_hash != dst_hash:
        print("ERROR: copied output hash %s != source hash %s" % (dst_hash, src_hash), file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dst, os.path.getsize(dst), dst_hash))


if __name__ == "__main__":
    sys.exit(main())
