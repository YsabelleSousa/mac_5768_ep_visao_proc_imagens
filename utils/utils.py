from pathlib import Path


def return_folder_size_mb(path):

    root_directory = Path(path)
    return round(sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()) / 1000000, 2)

