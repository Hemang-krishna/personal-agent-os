# Firecrawl AnyDoc & Agency Document Engine

- **Integrated By:** Dxrk sky & Hermes Agent
- **Git Author:** obsiagent-boop (obsi.agent@gmail.com)
- **Engine Path:** `/data/integrations/agency_doc_engine.py` & `/data/bin/anydoc`
- **Status:** 🟢 Production-Ready

---

## ⚡ Supported Document Formats (14 Types)
AnyDoc automatically parses and converts into GitHub-Flavored Markdown:
* **Office & Presentations:** `.docx`, `.doc`, `.pptx`, `.ppt`, `.odt`, `.odp`
* **Spreadsheets & Data:** `.xlsx`, `.ods`, `.csv`
* **Documents & Books:** `.pdf`, `.epub`, `.rtf`

---

## 🚀 How to Use

### 1. Direct CLI Conversion:
```bash
# Convert any document to Markdown on stdout
anydoc proposal.docx

# Convert presentation to a markdown file
anydoc pitch_deck.pptx -o pitch_deck.md
```

### 2. Agency Python Engine (`agency_doc_engine.py`):
```bash
# Ingest and convert incoming client files
python3 /data/integrations/agency_doc_engine.py parse client_brief.docx client_brief.md

# Generate branded Agency PDF records
python3 /data/integrations/agency_doc_engine.py pdf "Agency Strategy 2026" strategy.md agency_strategy.pdf
```
