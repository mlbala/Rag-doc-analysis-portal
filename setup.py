from setuptools import setup, find_packages

def load_requirements(filename="requirements.txt"):
    with open(filename, "r") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#") and not line.startswith("-e")
        ]

setup(
    name="rag_doc_analysis_portal",
    version="0.1.0",
    packages=find_packages(),  # or manually list if needed
    install_requires=load_requirements(),
)
