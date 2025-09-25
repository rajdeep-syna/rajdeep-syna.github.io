#!/usr/bin/env python3
"""
Script to create embedded PDF documentation from PDF files
Usage: python3 extract_section.py <pdf_file> <title> <output_filename>
"""

import sys
import re
import os
import shutil

def create_embedded_pdf_rst(pdf_file, title, output_file):
    """
    Create an RST file with embedded PDF viewer
    """
    
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file '{pdf_file}' not found!")
        return False
    
    # Get PDF filename for the static path
    pdf_filename = os.path.basename(pdf_file)
    
    # Create the RST content with embedded PDF
    rst_content = f"""{title}
{"=" * len(title)}

View the complete {title} directly below:

.. raw:: html

   <div style="margin-bottom: 20px; text-align: center;">
       <a href="_static/{pdf_filename}" download style="background-color: #0066cc; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; margin-right: 10px;">📄 Download PDF</a>
       <a href="_static/{pdf_filename}" target="_blank" style="background-color: #28a745; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px;">🌐 Open in New Tab</a>
   </div>

   <div style="width: 100%; height: 700px; border: 1px solid #ccc; margin-bottom: 20px; border-radius: 5px;">
       <iframe src="_static/{pdf_filename}" width="100%" height="100%" type="application/pdf" style="border-radius: 5px;">
           <p>Your browser does not support PDFs. <a href="_static/{pdf_filename}">Download the PDF</a> instead.</p>
       </iframe>
   </div>

   <script>
       // Fallback for browsers that don't support PDF embedding
       window.addEventListener('load', function() {{
           const iframe = document.querySelector('iframe[src*="{pdf_filename}"]');
           if (iframe) {{
               iframe.onerror = function() {{
                   iframe.style.display = 'none';
                   const fallback = document.createElement('div');
                   fallback.innerHTML = '<div style="text-align: center; padding: 50px; background-color: #f8f9fa; border-radius: 5px;"><h3>PDF Preview Not Available</h3><p>Your browser does not support inline PDF viewing.</p><p><a href="_static/{pdf_filename}" download style="background-color: #0066cc; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px;">📄 Download PDF</a></p></div>';
                   iframe.parentNode.appendChild(fallback);
               }};
           }}
       }});
   </script>

About This Document
-------------------

This document provides detailed information and technical specifications. Use the buttons above to download or view the PDF in a new tab.

The PDF includes comprehensive documentation with:

* Detailed procedures and instructions
* Technical specifications  
* Code examples and references
* Troubleshooting information

For the best viewing experience, click "Open in New Tab" to view in a dedicated browser tab, or use "Download PDF" to save locally.
"""
    
    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rst_content)
        print(f"✅ Created RST file '{output_file}' with embedded PDF viewer")
        return True
    except Exception as e:
        print(f"Error writing RST file: {e}")
        return False

def copy_pdf_to_static(pdf_file):
    """
    Copy PDF file to _static directory or use existing file if already there
    """
    # Create _static directory if it doesn't exist
    static_dir = "_static"
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print(f"✅ Created directory '{static_dir}'")
    
    pdf_filename = os.path.basename(pdf_file)
    static_pdf_path = os.path.join(static_dir, pdf_filename)
    
    # Check if the PDF is already in _static directory
    if os.path.abspath(pdf_file) == os.path.abspath(static_pdf_path):
        print(f"✅ PDF already exists in _static directory: '{pdf_file}'")
        return pdf_filename
    
    # Check if PDF already exists in _static with same name
    if os.path.exists(static_pdf_path):
        print(f"✅ PDF already exists in _static directory: '{static_pdf_path}'")
        return pdf_filename
    
    # Copy PDF to _static directory
    try:
        shutil.copy2(pdf_file, static_pdf_path)
        print(f"✅ Copied '{pdf_file}' to '{static_pdf_path}'")
        return pdf_filename
    except Exception as e:
        print(f"Error copying PDF file: {e}")
        return None

def update_toctree(index_file, new_rst_filename):
    """
    Add the new RST file to the toctree in index.rst
    """
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Find the toctree section and add the new file
    # Remove .rst extension for toctree entry
    toctree_entry = os.path.splitext(new_rst_filename)[0]
    
    # Pattern to find the end of toctree entries
    toctree_pattern = r'(\.\. toctree::\s*\n(?:\s+:[^:]+:[^\n]*\n)*)((?:\s+[^\s\n][^\n]*\n)*)'
    
    match = re.search(toctree_pattern, content, re.MULTILINE)
    if match:
        toctree_header = match.group(1)
        existing_entries = match.group(2)
        new_entries = existing_entries + f"   {toctree_entry}\n"
        
        updated_content = content.replace(match.group(0), toctree_header + new_entries)
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"✅ Added '{toctree_entry}' to toctree in '{index_file}'")
        return True
    else:
        print("Warning: Could not find toctree section to update")
        return False

def update_conf_py(pdf_filename):
    """
    Add PDF to html_extra_path in conf.py
    """
    conf_file = "conf.py"
    if not os.path.exists(conf_file):
        print(f"Warning: {conf_file} not found, skipping configuration update")
        return False
    
    try:
        with open(conf_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {conf_file}: {e}")
        return False
    
    # Check if html_extra_path exists
    if 'html_extra_path' in content:
        # Add to existing html_extra_path
        pattern = r"html_extra_path\s*=\s*\[(.*?)\]"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            current_files = match.group(1)
            if pdf_filename not in current_files:
                new_files = current_files.rstrip() + f", '{pdf_filename}'"
                updated_content = content.replace(match.group(0), f"html_extra_path = [{new_files}]")
                
                with open(conf_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ Added '{pdf_filename}' to html_extra_path in {conf_file}")
                return True
    else:
        # Add html_extra_path if it doesn't exist
        # Find a good place to add it (after html_static_path)
        if 'html_static_path' in content:
            insertion_point = content.find("html_static_path = ['_static']") + len("html_static_path = ['_static']")
            new_line = f"\n\n# Extra files to copy to build output\nhtml_extra_path = ['{pdf_filename}']"
            updated_content = content[:insertion_point] + new_line + content[insertion_point:]
            
            with open(conf_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ Added html_extra_path with '{pdf_filename}' to {conf_file}")
            return True
    
    print(f"Warning: Could not update {conf_file} automatically")
    return False

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 extract_section.py <pdf_file> <title> <output_filename>")
        print("Example: python3 extract_section.py MyGuide.pdf 'My Integration Guide' 'my_guide.rst'")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    title = sys.argv[2]
    output_filename = sys.argv[3]
    
    print(f"Creating embedded PDF documentation:")
    print(f"PDF file: '{pdf_file}'")
    print(f"Title: '{title}'")
    print(f"Output file: '{output_filename}'")
    print("-" * 50)
    
    # Step 1: Copy PDF to _static directory
    pdf_filename = copy_pdf_to_static(pdf_file)
    if not pdf_filename:
        sys.exit(1)
    
    # Step 2: Create RST file with embedded PDF
    if not create_embedded_pdf_rst(pdf_file, title, output_filename):
        sys.exit(1)
    
    # Step 3: Update toctree in index.rst
    if not update_toctree("index.rst", output_filename):
        print("Warning: Could not update toctree automatically")
        print(f"Please manually add '{os.path.splitext(output_filename)[0]}' to your toctree in index.rst")
    
    # Step 4: Update conf.py
    update_conf_py(pdf_filename)
    
    print("-" * 50)
    print("✅ PDF documentation creation completed successfully!")
    print(f"Files created/updated:")
    print(f"  - {output_filename} (RST file with embedded PDF)")
    print(f"  - _static/{pdf_filename} (PDF copy)")
    print(f"  - index.rst (updated toctree)")
    print(f"  - conf.py (updated configuration)")
    print(f"")
    print(f"Next steps:")
    print(f"1. Review the created file: {output_filename}")
    print(f"2. Run 'make html' to rebuild documentation")
    print(f"3. Test the embedded PDF in your browser")

if __name__ == "__main__":
    main()
