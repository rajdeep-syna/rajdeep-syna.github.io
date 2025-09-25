#!/bin/bash

# PDF to Clickable Link Converter for Sphinx Documentation
# Usage: ./pdf_to_link.sh <pdf_file> <document_title>

if [ $# -ne 2 ]; then
    echo "Usage: $0 <pdf_file> <document_title>"
    echo "Example: $0 MyGuide.pdf 'My Integration Guide'"
    exit 1
fi

PDF_FILE="$1"
DOC_TITLE="$2"

# Check if PDF file exists
if [ ! -f "$PDF_FILE" ]; then
    echo "Error: PDF file '$PDF_FILE' not found!"
    exit 1
fi

# Extract filename without extension for RST file name
BASE_NAME=$(basename "$PDF_FILE" .pdf)
RST_FILE="${BASE_NAME}.rst"

echo "Converting '$PDF_FILE' to clickable link documentation..."

# Step 1: Create _static directory if it doesn't exist
mkdir -p _static

# Step 2: Create RST file with clickable link
cat > "$RST_FILE" << EOF
$DOC_TITLE
$(printf '=%.0s' $(seq 1 ${#DOC_TITLE}))

This document provides detailed technical information and instructions.

.. raw:: html

   <div style="text-align: center; margin: 30px 0;">
       <a href="_static/$(basename "$PDF_FILE")" 
          target="_blank" 
          style="display: inline-block; background-color: #0066cc; color: white; padding: 15px 25px; text-decoration: none; border-radius: 8px; font-size: 16px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
          📄 Open $(basename "$PDF_FILE" .pdf) (PDF)
       </a>
   </div>

   <div style="text-align: center; margin: 20px 0;">
       <a href="_static/$(basename "$PDF_FILE")" 
          download 
          style="display: inline-block; background-color: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
          💾 Download PDF
       </a>
   </div>

About This Document
-------------------

This document contains comprehensive information and technical specifications. Click the link above to view the complete PDF content.

The PDF includes:

* Detailed procedures and instructions
* Technical specifications  
* Code examples and references
* Troubleshooting information

For the best viewing experience, click "Open PDF" to view in a new tab, or use "Download PDF" to save locally.
EOF

echo "✓ Created RST file: $RST_FILE"

# Step 4: Show instructions for manual steps
echo ""
echo "🔧 Manual steps required:"
echo "1. Add '$BASE_NAME' to your index.rst toctree section"
echo "2. Add '$(basename "$PDF_FILE")' to html_extra_path in conf.py"
echo "3. Run 'make html' to build documentation"
echo ""
echo "✅ Conversion completed successfully!"
