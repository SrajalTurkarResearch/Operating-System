import os
from docx import Document

def create_os_syllabus_directory_structure(docx_path, base_dir="Operating_Systems_Project"):
    """
    Reads a syllabus .docx file and creates a directory structure for an OS project,
    similar to the current NLG directory structure.
    """
    # Load the syllabus document
    doc = Document(docx_path)
    # Extract headings (assuming Heading 1 for modules/sections)
    modules = []
    for para in doc.paragraphs:
        if para.style.name.startswith("Heading 1"):
            module_name = para.text.strip()
            if module_name:
                # Clean up the module name for directory naming
                safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in module_name)
                modules.append(safe_name)

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create subdirectories for each module
    for module in modules:
        module_dir = os.path.join(base_dir, module)
        os.makedirs(module_dir, exist_ok=True)
        # Optionally, create placeholder files
        with open(os.path.join(module_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {module}\n\nContent for this module goes here.\n")

    print(f"Directory structure created under '{base_dir}' with modules: {modules}")

# Example usage:
# create_os_syllabus_directory_structure(
#     r"C:\Users\Rishu\OneDrive\Desktop\Computer_Science\Syllabus\Final Operating Systems Syllabus for Aspiring Computer Scientists.docx"
# )
