# OpenMW-mod-address-extractor
Simple script to automatically extract the paths and file names of OpenMW/umo mods from the root directory

# OpenMW UMO Mod Data Extract – Quick Start

**Author:** Julien Cabana
**Version:** 1.0
**Date:** 2025-12-05

## What it does

Extracts all mod directories and files from your OpenMW UMO folder.
Generates two output files in the script folder:

* `mod_paths.txt` → full paths of mod directories
* `mod_names.txt` → mod files with extensions `.esp`, `.esm`, `.omwaddon`, `.omwscripts`

## Quick Usage

1. Place the script anywhere.
2. Update `root` in the script to your UMO mods folder.
3. Run the script:

```bash
python3 openmw_umo_mod_data_extract.py
```

4. Copy-paste the output files in your `openmw.cfg`.
