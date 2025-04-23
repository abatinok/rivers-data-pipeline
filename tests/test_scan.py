from pathlib import Path
from rivers.dispatcher import scan_folder

def test_scan_folder(tmp_path):
    # create two dummy files
    (tmp_path/"a.xls").touch()
    (tmp_path/"sub"/"b.pdf").parent.mkdir()
    (tmp_path/"sub"/"b.pdf").touch()

    files = list(scan_folder(tmp_path))
    assert len(files) == 2