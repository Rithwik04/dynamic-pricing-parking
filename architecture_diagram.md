flowchart TD

    A["Input Data: dataset.csv (14 Parking Lots, 73 Days, 18 Time Points)"] --> B["Ingestion Layer: Pathway Streaming"]
    B --> C1["Feature: Occupancy Ratio"]
    B --> C2["Feature: Queue Length"]
    B --> C3["Feature: Traffic Conditions"]
    B --> C4["Feature: Special Day Indicator"]
    B --> C5["Feature: Vehicle Type Weight"]

    C1 & C2 & C3 & C4 & C5 --> D1["Model 1: Linear Pricing"]
    C1 & C2 & C3 & C4 & C5 --> D2["Model 2: Demand-based Pricing"]
    C1 & C2 & C3 & C4 & C5 --> D3["Model 3: Competitive Pricing + Rerouting"]

    D1 --> E["Price Output Stream"]
    D2 --> E
    D3 --> E

    E --> F["Bokeh Real-time Dashboard"]
    D3 --> G["Optional: Rerouting Suggestions"]
