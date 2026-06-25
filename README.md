# ecommerce-asset-automation
A Python based automation pipeline that extracts catalog asset indexes and dynamically processes layout positions using Regular Expressions.


# Automated E-Commerce Asset Processing & Dimensional Scaling Engine

An automated backend data pipeline engineered in Python to handle large-scale catalog digitization, structural data sanitization, and asset layout mapping. This project eliminates hours of tedious manual QA assessment by programmatically parsing unstructured web assets, standardizing identification indexing rules, and calculating asset orientations with mathematical precision via text-based Regular Expressions.

## 🚀 The Core Problem vs. Automation Solution
* **The Manual Overhead:** Without automation, mapping display attributes across a database of thousands of items requires a QA analyst or data operator to visually open every image file container, inspect its orientation, and manually record layout tags into a tracking sheet.
* **The Automated Pipeline:** This script completely bypasses manual interaction. It scans thousands of background resource records in seconds, programmatically extracting display sizing parameters directly from the image link text string to instantly compute shapes with zero manual entry required.

## 🛠️ Technology Stack & Automation Tools
* **Core Language:** Python 3
* **Data Processing & Analytics:** Pandas (DataFrame matrix manipulations, column filtering)
* **Pattern Analysis:** Regular Expressions (`re` built-in module for sub-string parsing)
* **System Operations:** `os` module (filesystem architecture, environment paths handling)
* **Data Delivery:** OpenPyXL (compiling data arrays cleanly into native Microsoft Excel `.xlsx` templates)
* **Core Development Environment:** Google Colab Cloud Notebook Runtime

## 📋 Technical Workflow Architecture
1. **Data Ingestion:** The script mounts and parses the raw unstructured `.csv` web dataset file, dynamically creating fallback indexing protocols if the source product lacks uniform name headings.
2. **URL Parameter Mining:** Instead of running heavy graphics rendering engines to read image files, the program uses custom Regex configurations to pull geometric sizing parameters (e.g., extracting width and height dimensions from strings matching `w_XXX,h_XXX`).
3. **Algorithmic Shape Mapping:** Applies conditional logic checking: if width exceeds height, the asset is automatically categorized as `Left to right`. If dimensions are equal, it flags a `Square / Uniform` status, otherwise defaulting safely to a vertical `Top to Bottom` layout.
4. **Data Integrity Architecture:** Relies strictly on objective parameter data, stripping out error-prone third-party visual guessing layers to deliver a reliable, clean schema layout ready for cloud-database migrations.

## 🧠 Engineering Roadblocks & Strategic Fixes

### 1. Cloud Filesystem Path Drift (`FileNotFoundError`)
* **The Failure:** Relational file routing rules crashed intermittently inside cloud container runtimes because variable system directories misplaced the source data folder hook.
* **The Fix:** Programmed an adaptive root filesystem scan module utilizing `os.walk('/')`. This allows the script to trace, intercept, and lock onto the file target independently of server environment changes.

### 2. Optical Character Recognition (OCR) / Vision Model Pivot
* **The Failure:** Initial structural variants attempted to call visual recognition models (like BLIP AI) to pull stylized historical script markings. However, due to complex imagery backgrounds, non-standard text arches, and varying font styles, the models suffered high hallucination rates and outputted inaccurate results.
* **The Fix:** Executed a vital engineering pivot by stripping away unreliable vision layers entirely. Refocused the processing model on algorithmic parameters (URL dimension text parsing), guaranteeing absolute data reliability and an error-free, predictable data schema.

## 📊 Industry Alignment: Relevant Software Engineering Roles
This automation project maps directly onto core responsibilities within these specialized job fields:
* **Automation Test Engineer / SDET:** Demonstrates writing script configurations to replace high-overhead manual validation tasks.
* **QA (Quality Assurance) Analyst:** Showcases rigorous edge-case handling, data mapping, and failure analysis system pivots.
* **Associate Data Engineer:** Exhibits core ETL (Extract, Transform, Load) loop design and custom text regex manipulation.
