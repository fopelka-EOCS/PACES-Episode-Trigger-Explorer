# PACES Episode Trigger Explorer

The **PACES Episode Trigger Explorer** is an interactive Streamlit application designed to help analysts, clinicians, and consulting teams quickly identify and understand the trigger logic associated with PACES episodes. The tool enables users to search by episode short descriptor, clinical chapter, or CPT keyword, returning the relevant triggers and their long-form descriptions.

This app is part of the broader **EOCS (Episodes of Care Suite)** initiative, which aims to provide transparent, data-driven tools that support episode design, validation, and value demonstration.

---

## 🔍 Key Features

- **Episode Short Descriptor Search**  
  Enter any episode short descriptor to retrieve all associated triggers.

- **Clinical Chapter & Episode ID Filters**  
  Narrow results to specific clinical domains or episode families.

- **CPT Keyword Search**  
  Identify triggers based on procedure terminology.

- **Downloadable Results**  
  Export tables for further analysis or documentation.

## 📘 Usage Guide

<img width="736" height="565" alt="PACES Epi Trigger Search" src="https://github.com/user-attachments/assets/abd842f0-8b54-454b-921d-1e34dd8b5d1f" />


The PACES Episode Trigger Explorer is designed to make it fast and intuitive to identify which triggers belong to which PACES episodes. The tool supports multiple search pathways depending on what information the user starts with.

## Data Versioning 
- **PACES Episodes:** Updated with PACES v5.3 (Jan 2026 Release)
- - **CPT Descriptions:** Integrated from NHSN public release file <sub> *CPT® is a registered trademark of the American Medical Association.
  - Descriptions shown here reflect the NHSN public release file and may not represent the full AMA CPT code set.* </sub>  

---

### 1. Search by Episode Short Descriptor

Use this workflow when you know the episode name (e.g., “Knee Arthroscopy”).

**Steps:**
1. Select **Episode Short Descriptor** from the sidebar.
2. Begin typing the descriptor.
3. Choose the matching episode from the dropdown.
4. Review all associated triggers and long-form descriptions.

This is the most direct way to validate trigger logic for a specific episode.

---

### 2. Filter by Clinical Chapter or Episode ID

Use this when exploring a clinical domain or reviewing a family of related episodes.

**Steps:**
1. Select **Clinical Chapter** or **Episode ID**.
2. Choose from the dropdown list.
3. View the returned triggers and descriptions.

This workflow is ideal for domain-level review or early-stage episode design.

---

### 3. CPT Keyword Search

Use this when you know a procedure term but not the episode.

**Steps:**
1. Select **CPT Keyword Search**.
2. Enter a keyword (e.g., “arthro”, “laparo”, “fusion”).
3. Review all triggers whose long descriptions contain that keyword.

This is especially useful for exploratory analysis or validating CPT groupings.

---

### 4. Downloading Results

Every results table includes a **Download CSV** button.

Use this to:
- Export triggers into Excel  
- Incorporate logic into modeling workflows  
- Share subsets with clinical or analytic teams  

---

### 5. Intended Use

This tool supports:
- Episode design and refinement  
- Trigger validation  
- Clinical logic review  
- Rapid prototyping for consulting engagements  
- Demonstrations of transparency and traceability in episode construction  

It is part of the broader **EOCS (Episodes of Care Suite)** initiative.

---

## 🚀 How to Use

1. Open the deployed app:  
   **https://fopelka-ecos.streamlit.app**

2. Choose your search method:
   - Episode short descriptor  
   - Clinical chapter  
   - Episode ID  
   - CPT keyword  

3. Review the returned triggers and long descriptions.

4. Download the results table if needed.

---

## 🧱 Project Structure

