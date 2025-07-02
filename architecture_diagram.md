flowchart TD

subgraph Input Data
    A[dataset.csv<br>– 14 Parking Lots<br>– 73 Days × 18 Time Points]
end

subgraph Ingestion Layer
    A --> B[Pathway Stream Simulation<br>(Real-Time Delayed Feed)]
end

subgraph Feature Engineering
    B --> C[Feature Extraction:<br>• Occupancy Rate<br>• Queue Length<br>• Traffic Conditions<br>• Vehicle Type<br>• Special Day Indicator]
end

subgraph Pricing Engine
    C --> D1[Model 1: Baseline Linear Pricing]
    C --> D2[Model 2: Demand-based Dynamic Pricing]
    C --> D3[Model 3: Competitive Pricing<br>(Optional with Geo-Logic)]
end

subgraph Output & Visualization
    D1 --> E[Price Updates Stream]
    D2 --> E
    D3 --> E
    E --> F[Bokeh Visualization:<br>• Real-Time Price Lines<br>• Lot Comparison Graphs]
    D3 --> G[Optional Rerouting Suggestions]
end
