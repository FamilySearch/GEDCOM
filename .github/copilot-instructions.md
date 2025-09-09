# FamilySearch GEDCOM Specification Repository

Always reference these instructions first and only fallback to search or bash commands when you encounter unexpected information that does not match the information provided here.

The FamilySearch GEDCOM repository is a specification repository that defines the standard for genealogical data exchange. This is NOT a software application with runtime components, but rather a documentation project that builds specification documents (HTML/PDF) from markdown source files.

## Working Effectively

### Bootstrap and Build Dependencies
Install all required dependencies in this exact order:
```bash
# Install system dependencies
sudo apt-get update && sudo apt-get install -y pandoc

# Install Python dependencies  
python3 -m pip install --user --upgrade weasyprint mdformat_gfm
```

Verify installations:
```bash
python3 --version        # Should show Python 3.x
pandoc --version         # Should show pandoc version
yamllint --version       # Should show yamllint (pre-installed)
make --version           # Should show GNU Make
```

### Build the Specification
Build the complete specification (HTML and PDF) and extract all generated files:
```bash
cd build
# Ensure tags directory exists (required after distclean)
mkdir -p ../extracted-files/tags
make
```
**NEVER CANCEL: Build takes ~30 seconds. Set timeout to 60+ seconds.**

If the build completes but the `extracted-files/tags/` directory is empty, run the URI extraction manually:
```bash
cd build
python3 uri-def.py ../specification/gedcom*.md ../extracted-files/tags
```

This command generates:
- `specification/gedcom.html` - Complete specification in HTML format  
- `specification/gedcom.pdf` - Complete specification in PDF format
- `extracted-files/grammar.abnf` - ABNF grammar definitions
- `extracted-files/grammar.gedstruct` - Structure grammar definitions  
- `extracted-files/tags/` - Individual tag definition files
- Various `.tsv` files with cardinalities, enumerations, payloads, substructures

### Clean Generated Files
Remove temporary build files only:
```bash
cd build
make clean
```

Remove all generated files (HTML, PDF, extracted files):
```bash
cd build  
make distclean
# Recreate tags directory for next build
mkdir -p ../extracted-files/tags
```

## Validation

### Validate YAML Files
Always run YAML validation before committing changes:
```bash
yamllint .
```
**Completes in <1 second. This must pass for CI to succeed.**

### Build Validation
Always validate that the build process completes successfully after making changes to specification files:
```bash
cd build
make
```

The build process will show expected warnings about CSS properties (these are normal and documented in build/README.md). Any actual errors will cause the build to fail.

### End-to-End Validation Workflow
After making changes to specification markdown files, always run this complete validation:
```bash
# Validate YAML files
yamllint .

# Clean and rebuild everything
cd build
make distclean
mkdir -p ../extracted-files/tags
make

# If tags directory is empty, run URI extraction manually
python3 uri-def.py ../specification/gedcom*.md ../extracted-files/tags

# Verify generated files exist
ls -la ../specification/gedcom.html ../specification/gedcom.pdf
ls -la ../extracted-files/grammar.abnf ../extracted-files/grammar.gedstruct
ls -la ../extracted-files/tags/
```

## CI/CD Integration

The repository has automated workflows that run on pushes and pull requests:

### YAML Validation Workflow
- Triggered on: pushes and PRs to main, v7.1, next-patch branches
- Command: `yamllint .`
- Must pass for PRs to be mergeable

### File Generation Workflow  
- Triggered on: pushes to main and v7.1 branches
- Automatically runs grammar and tag extraction
- Creates PRs with updated extracted files if changes detected
- Uses commands:
  - `python3 extract-grammars.py ../specification/gedcom*.md ../extracted-files/`
  - `python3 uri-def.py ../specification/gedcom*.md ../extracted-files/tags`

## Repository Structure

### Key Directories
- `specification/` - Markdown source files for the GEDCOM specification (main content)
- `build/` - Build tools, scripts, and configuration files  
- `extracted-files/` - Auto-generated files (DO NOT EDIT MANUALLY)
- `version-detection/` - Version detection specification
- `.github/workflows/` - CI pipeline definitions

### Specification Source Files (in order)
- `specification/gedcom-0-introduction.md`
- `specification/gedcom-1-hierarchical-container-format.md`  
- `specification/gedcom-2-data-types.md`
- `specification/gedcom-3-structures-1-organization.md`
- `specification/gedcom-3-structures-3-meaning.md`
- `specification/gedcom-3-structures-4-enumerations.md`
- `specification/gedcom-4-gedzip.md`
- `specification/gedcom-5-contributors.md`
- `specification/gedcom-6-appendix-calendars.md`

### Build Tools (build/ directory)
- `Makefile` - Orchestrates the build process
- `hyperlink.py` - Adds hyperlinks to markdown 
- `hyperlink-code.py` - Adds hyperlinks to code blocks in HTML
- `extract-grammars.py` - Extracts ABNF and structure grammars
- `uri-def.py` - Extracts tag definitions and generates YAML files
- `push_to_gedcomio.py` - Uploads to gedcom.io (requires special access)

## Common Development Tasks

### Making Specification Changes
1. Edit the appropriate `specification/gedcom-*.md` file
2. Run validation: `yamllint .`
3. Test build: `cd build && make`
4. Review generated files for correctness
5. Commit changes (extracted files will be auto-updated by CI)

### Adding New GEDCOM Structures
1. Add structure definition to appropriate specification file
2. Add any new tag definitions to `specification/terms/` if needed
3. Run full build validation
4. Verify new structures appear in extracted files

### Debugging Build Issues
If build fails:
1. Check for YAML syntax errors: `yamllint .`
2. Check Python script syntax: verify `.py` files in build/ directory
3. Verify pandoc can process individual markdown files
4. Check build/README.md for known issues and requirements

### Branch Strategy
- `main` - Current release (stable)
- `v7.1` - Working draft of next minor release
- `sandbox` - Candidate changes for future consideration
- Other branches are temporary discussion drafts

## Important Notes

### What This Repository Does NOT Include
- No runtime software application  
- No unit tests or test suites
- No server/client components
- No database dependencies
- No package.json, requirements.txt, or similar dependency files

### Timeouts and Performance
- YAML validation: <1 second
- Full specification build: ~30 seconds  
- Grammar extraction: <1 second
- URI extraction: ~4 seconds
- **Always use 60+ second timeouts for build commands to avoid premature cancellation**

### Expected Build Warnings
The build process emits CSS-related warnings from weasyprint - these are normal and documented. Only stop the build for actual errors, not warnings.

### File Publishing
Publishing to gedcom.io requires access to the separate GEDCOM.io repository and is not part of normal development workflows.