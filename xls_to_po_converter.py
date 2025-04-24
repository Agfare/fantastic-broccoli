import pandas as pd
import polib
import argparse
from pathlib import Path

def create_po_entry(msgid, msgstr, source_lang=None):
    """Create a PO entry with the given message ID and translation."""
    entry = polib.POEntry(
        msgid=msgid,
        msgstr=msgstr,
    )
    if source_lang:
        entry.comment = f"Source language: {source_lang}"
    return entry

def create_multilingual_po(df, output_file):
    """Create a single multilingual PO file."""
    po = polib.POFile()
    po.metadata = {
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    for _, row in df.iterrows():
        msgid = str(row.iloc[0])  # First column is message ID
        for lang in df.columns[1:]:  # Skip the first column (message ID)
            msgstr = str(row[lang])
            entry = create_po_entry(msgid, msgstr, lang)
            po.append(entry)

    po.save(output_file)
    print(f"Created multilingual PO file: {output_file}")

def create_separate_po_files(df, source_lang, output_dir):
    """Create separate PO files for each language pair."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    source_column = df.columns[0]  # First column is message ID
    target_languages = df.columns[1:]  # All other columns are target languages

    for target_lang in target_languages:
        po = polib.POFile()
        po.metadata = {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
            'Language': target_lang,
        }

        for _, row in df.iterrows():
            msgid = str(row[source_column])
            msgstr = str(row[target_lang])
            entry = create_po_entry(msgid, msgstr)
            po.append(entry)

        output_file = output_dir / f"po_{source_lang}_{target_lang}.po"
        po.save(str(output_file))
        print(f"Created PO file: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Convert XLS file to PO files')
    parser.add_argument('input_file', help='Input XLS file path')
    parser.add_argument('--multilingual', action='store_true', help='Create a single multilingual PO file')
    parser.add_argument('--source-lang', default='en', help='Source language code (default: en)')
    parser.add_argument('--output-dir', default='po_files', help='Output directory for separate PO files')
    args = parser.parse_args()

    # Read the Excel file
    df = pd.read_excel(args.input_file)

    if args.multilingual:
        output_file = 'po_compendium_multilingual.po'
        create_multilingual_po(df, output_file)
    else:
        create_separate_po_files(df, args.source_lang, args.output_dir)

if __name__ == '__main__':
    main() 