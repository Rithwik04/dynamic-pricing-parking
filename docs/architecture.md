
# 📐 Project Architecture – Dynamic Pricing for Urban Parking Lots

**Capstone Project – Summer Analytics 2025**  
**Consulting & Analytics Club × Pathway**

---

## 📝 Overview

This document provides a detailed explanation of the system architecture of the **Dynamic Pricing for Urban Parking Lots** project.

The architecture is designed to:
- Process real-time data streams
- Compute pricing dynamically based on demand, competition, and external factors
- Provide smooth and explainable pricing decisions
- Optionally recommend rerouting vehicles when lots are full

---

## 🔄 Workflow Stages

### 1️⃣ Input Data

We start with a **historical dataset**:
- 18,368 records covering 14 urban parking lots
- Data spans 73 days, with 18 time points per day
- Features include:
  - Occupancy
  - Capacity
  - Queue length
  - Vehicle type (car, bike, truck)
  - Nearby traffic conditions
  - Special day indicator
  - Latitude and longitude for each lot
  - Timestamp

This data is placed in `data/dataset.csv`.

---

### 2️⃣ Ingestion Layer

The **Pathway** stream processing engine simulates a real-time data feed from the dataset.  
Key tasks:
- Stream records one by one, preserving their chronological order.
- Mimic real-world sensor or IoT data streams.
- Feed data into the feature engineering and pricing logic modules.

---

### 3️⃣ Feature Engineering

At each time step, we extract and compute:
- **Occupancy Ratio** = current occupancy / capacity
- **Queue Length** = vehicles waiting
- **Traffic Level Weight**: mapping `low`, `medium`, `high` to numeric weights
- **Special Day Indicator**: binary (0/1)
- **Vehicle Type Weight**: cars, bikes, trucks assigned different weights

These features serve as inputs to the pricing models.

---

### 4️⃣ Pricing Engine

We implement three progressive models of increasing sophistication:

#### Model 1: Baseline Linear Pricing
- Adjusts the price linearly based on occupancy ratio:
  \[
  P_{t+1} = P_t + \alpha \cdot \frac{\text{occupancy}}{\text{capacity}}
  \]
- Simple, easy-to-interpret, but doesn’t consider other features.

#### Model 2: Demand-based Pricing
- Builds a weighted demand function:
  \[
  \text{Demand} = \alpha_1 \cdot \text{Occupancy Ratio} + \alpha_2 \cdot \text{Queue} - \alpha_3 \cdot \text{Traffic} + \alpha_4 \cdot \text{Special Day} + \alpha_5 \cdot \text{Vehicle Weight}
  \]
- Normalizes demand and adjusts the price smoothly.

#### Model 3: Competitive Pricing (Optional)
- Adds geo-intelligence by analyzing competitors:
  - Computes distance to nearby lots.
  - Factors in their prices.
  - Suggests rerouting vehicles to cheaper/less crowded nearby lots.
  - Dynamically adjusts price to remain competitive.

---

### 5️⃣ Output & Visualization

The system outputs:
- Real-time price updates for each parking lot
- Optional rerouting suggestions
- Visualizations via **Bokeh**, including:
  - Price evolution over time
  - Competitor comparisons
  - Queue and occupancy trends

Bokeh outputs are saved in `visuals/pricing_visuals.html`.

---

## 🧾 Design Principles & Assumptions

✅ Real-time, low-latency performance using Pathway  
✅ Smooth and explainable pricing (bounded: **$5–$20**)  
✅ Scalable to more parking lots and more complex features  
✅ No external ML libraries — only Python (`pandas`, `numpy`, `Pathway`)  
✅ Modular structure for easy extensibility

---

## 📁 Files Related to Architecture

| File | Description |
|------|-------------|
| `docs/architecture.md` | This document |
| `architecture_diagram.md` | Mermaid diagram of the system |
| `src/model_baseline.py` | Linear pricing logic |
| `src/model_demand.py` | Demand-based pricing logic |
| `src/model_competition.py` | Competitive pricing logic |
| `notebooks/Dynamic_Pricing_Model.ipynb` | Colab notebook integrating all components |

---

## 📌 Summary

This architecture provides a real-time, explainable, and scalable solution for dynamic pricing of urban parking lots.  
By integrating historical patterns, live conditions, and competitive analysis, it ensures better utilization of resources while keeping customer satisfaction high.

---
