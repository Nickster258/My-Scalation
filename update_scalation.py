import glob
import logging
import os
import shutil
import sys
import zipfile
from pathlib import Path
from urllib import request

_logger = logging.getLogger("root")
_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
_logger.addHandler(console_handler)


_scalation_destination = Path(__file__).parent / "scalation"


def main():
    _scalation_url = sys.argv[-1]  # python3 update_scalation.py <scalation_url_zip>
    if _scalation_url.startswith("https"):
        _scalation_url = f"http{_scalation_url[5:]}"
    _logger.info(f"Fetching ScalaTion from '{_scalation_url}'...")
    file_name, _ = request.urlretrieve(_scalation_url)  # Download ScalaTion
    _logger.info(f"Removing old ScalaTion...")
    try:
        shutil.rmtree(_scalation_destination)  # Delete old ScalaTion
    except Exception:
        _logger.info("Scalation didn't exist, ignoring")
    _logger.info(f"Unpacking new ScalaTion...")
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
        _logger.info(f"Renaming scalation...")
        residing_dir = Path(__file__).parent
        shutil.move(glob.glob(str(residing_dir / 'scalation*'))[0], residing_dir / 'scalation')
    _logger.info(f"Removing unit tests...")
    shutil.rmtree(_scalation_destination / 'src' / 'test')
    _logger.info(f"Removing ScalaTion SBT...")
    os.unlink(_scalation_destination / 'build.sbt')


if __name__ == "__main__":
    main()
