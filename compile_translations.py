#!/usr/bin/env python
"""
Simple script to compile .po files to .mo files for Django translations.
This is a workaround for Windows systems where gettext tools might not be available.
"""

import os
import polib

def compile_po_to_mo():
    """Compile .po files to .mo files"""
    locale_dir = 'locale'
    
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                mo_path = po_path.replace('.po', '.mo')
                
                try:
                    # Read the .po file
                    po = polib.pofile(po_path)
                    
                    # Write the .mo file
                    po.save_as_mofile(mo_path)
                    print(f"Compiled: {po_path} -> {mo_path}")
                    
                except Exception as e:
                    print(f"Error compiling {po_path}: {e}")

if __name__ == '__main__':
    compile_po_to_mo() 