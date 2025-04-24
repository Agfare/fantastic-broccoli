# XLS to PO Converter

This script converts multilingual XLS files to PO (Portable Object) files. The input XLS file should have the first column as Message ID and subsequent columns as translations in different languages (using CLDR locale codes).

## Requirements

- Python 3.6 or higher
- Required packages (install using `pip install -r requirements.txt`):
  - pandas
  - polib
  - openpyxl

## Usage

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script with your XLS file:
   ```bash
   # For separate PO files (default)
   python xls_to_po_converter.py input.xlsx

   # For a single multilingual PO file
   python xls_to_po_converter.py input.xlsx --multilingual

   # Specify source language (default is 'en')
   python xls_to_po_converter.py input.xlsx --source-lang en

   # Specify output directory (default is 'po_files')
   python xls_to_po_converter.py input.xlsx --output-dir my_po_files
   ```

## Output

- When using separate files mode (default):
  - Creates a directory named `po_files` (or specified output directory)
  - Generates separate PO files for each language pair (e.g., `po_en_ru.po`, `po_en_fr.po`, etc.)

- When using multilingual mode (`--multilingual`):
  - Creates a single file named `po_compendium_multilingual.po` containing all translations

## Input File Format

The input XLS file should be structured as follows:

| Message ID | en | fr | de | ... |
|------------|----|----|----|-----|
| msg1       | ...| ...| ...| ... |
| msg2       | ...| ...| ...| ... |
| ...        | ...| ...| ...| ... |
