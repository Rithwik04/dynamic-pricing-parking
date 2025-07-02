# 🅿️ Dynamic Pricing for Urban Parking Lots

**Capstone Project – Summer Analytics 2025**  
**Consulting & Analytics Club × Pathway**

---

## 📌 Project Overview

Urban parking spaces suffer from static pricing inefficiencies. This project builds a **dynamic, real-time pricing engine** for 14 urban parking lots using demand, competition, and real-time environmental features. The model adjusts prices intelligently using data-driven logic built from scratch using `NumPy`, `Pandas`, and `Pathway`.

---

## 🛠 Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - Data Processing: `pandas`, `numpy`
  - Visualization: `bokeh`
  - Real-time Ingestion: `Pathway`
- **Platform**: Google Colab

---

## 🧠 Architecture Diagram

See [`architecture_diagram.md`](architecture_diagram.md) for the flowchart.  
Visual diagram built using Mermaid.

```mermaid
flowchart TD
    A[Data Source: dataset.csv] --> B[Pathway Stream Engine]
    B --> C[Real-time Feature Engineering]
    C --> D[Dynamic Pricing Models]
    D --> E[Price Output Stream]
    D --> F[Optional: Rerouting Suggestions]
    E --> G[Visualization via Bokeh]
