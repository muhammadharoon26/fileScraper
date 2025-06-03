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
    root_folder="D:/Git-Hub/product-images-scraping",
    output_file="output.txt",
    exclude_paths=[
        "D:/Git-Hub/product-images-scraping/.git/",
        "D:/Git-Hub/product-images-scraping/amazonScraper/node_modules",
        "D:/Git-Hub/product-images-scraping/amazonScraper/.env",
        "D:/Git-Hub/product-images-scraping/amazonScraper/amazon_results.json",
        "D:/Git-Hub/product-images-scraping/amazonScraper/deploy.sh",
        "D:/Git-Hub/product-images-scraping/amazonScraper/Dockerfile",
        "D:/Git-Hub/product-images-scraping/amazonScraper/filteredProducts.md",
        "D:/Git-Hub/product-images-scraping/amazonScraper/keywords.txt",
        "D:/Git-Hub/product-images-scraping/amazonScraper/package-lock.json",
        "D:/Git-Hub/product-images-scraping/amazonScraper/package.json",
        "D:/Git-Hub/product-images-scraping/amazonScraper/products.json",
        "D:/Git-Hub/product-images-scraping/amazonScraper/README.md",
        "D:/Git-Hub/product-images-scraping/amazonScraper/sample.env",
        "D:/Git-Hub/product-images-scraping/amazonScraper/tsconfig.json",
        "D:/Git-Hub/product-images-scraping/amazonScraper/tsconfig.tsbuildinfo",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/src/__pycache__",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/src/api/__pycache__",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/src/api/__init__.py",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/src/services/__pycache__",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/src/utils/__pycache__",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/.env",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/Dockerfile",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/google_html_output_bose_quietcomfort_ultra.html",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/README.md",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/requirements.txt",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/run.py",
        "D:/Git-Hub/product-images-scraping/googleSearchScrapper/sample.env",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/api/__pycache__",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/api/__init__.py",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/__pycache__",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/services/__pycache__",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/services/__init__.py",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/src/utils/__init__.py",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/venv",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/deploy.sh",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/Dockerfile",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/README.md",
        "D:/Git-Hub/product-images-scraping/image-dedup-api/requirements.txt",
        "D:/Git-Hub/product-images-scraping/orchestrator/__pycache__",
        "D:/Git-Hub/product-images-scraping/orchestrator/requirements.txt",
        "D:/Git-Hub/product-images-scraping/orchestrator/sample.env",
        "D:/Git-Hub/product-images-scraping/amazon_results.json",
        "D:/Git-Hub/product-images-scraping/.gitignore",
        "D:/Git-Hub/product-images-scraping/output.txt",
        "D:/Git-Hub/product-images-scraping/README.md",
    ],
)
