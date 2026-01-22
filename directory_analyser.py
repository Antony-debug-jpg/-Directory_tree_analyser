import os


def format_size(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"


def analyze_directory(path):
    total_files = 0
    total_dirs = 0
    total_size = 0
    extension_map = {}
    largest_files = []

    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)

        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)

            # Get file extension
            ext = os.path.splitext(file)[1].lower()
            if ext == "":
                ext = "NO EXTENSION"

            extension_map[ext] = extension_map.get(ext, 0) + 1

            # Get file size safely
            try:
                size = os.path.getsize(file_path)
                total_size += size
                largest_files.append((size, file_path))
            except (PermissionError, FileNotFoundError, OSError):
                continue

    # Sort files by size (largest first)
    largest_files.sort(reverse=True)

    return {
        "total_files": total_files,
        "total_dirs": total_dirs,
        "total_size": total_size,
        "extensions": extension_map,
        "largest_files": largest_files[:5]
    }


def main():
    print("DIRECTORY TREE ANALYZER\n")

    path = input(str("Enter directory path to analyze: ")).strip()

    if not os.path.exists(path):
        print("ERROR: Path does not exist.")
        return

    print("\nScanning directory...\n")

    result = analyze_directory(path)

    print("ANALYSIS RESULTS")
    print(f"Total folders : {result['total_dirs']}")
    print(f"Total files   : {result['total_files']}")
    print(f"Total size    : {format_size(result['total_size'])}")

    print("\nFiles by extension:")
    for ext, count in result["extensions"].items():
        print(f"  {ext}: {count}")

    print("\nTop 5 Largest Files:")
    for size, file in result["largest_files"]:
        print(f"  {format_size(size)} - {file}")


if __name__ == "__main__":
    main()
