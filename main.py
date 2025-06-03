import os


def normalize_path(path):
    return os.path.abspath(path).replace("\\", "/")


def scrape_files_to_txt(root_folder, output_file, exclude_paths=None):
    root_folder = normalize_path(root_folder)
    exclude_paths = set(normalize_path(p) for p in (exclude_paths or []))

    with open(output_file, "w", encoding="utf-8") as out_f:
        for dirpath, dirnames, filenames in os.walk(root_folder):
            dirpath = normalize_path(dirpath)

            # Skip entire folder if it's in the excluded paths
            if dirpath in exclude_paths:
                dirnames[:] = []  # Don't descend into subdirs
                continue

            # Filter out subfolders that are in exclude list
            dirnames[:] = [
                d
                for d in dirnames
                if normalize_path(os.path.join(dirpath, d)) not in exclude_paths
            ]

            for filename in filenames:
                file_path = normalize_path(os.path.join(dirpath, filename))
                if file_path in exclude_paths:
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read().replace(
                            '"', r"\""
                        )  # Escape double quotes
                        out_f.write(f'"{file_path}":\n"{content}"\n\n')
                except Exception as e:
                    print(f"Skipping {file_path}: {e}")


# Example usage:
scrape_files_to_txt(
    root_folder="",
    output_file="output.txt",
    exclude_paths=[],
)
