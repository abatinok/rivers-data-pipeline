from pathlib import Path

def scan_folder(root: Path):
    """Yield Path objects for every file under *root*."""
    return root.rglob("*.*")