# K-LHUR: A Data-Driven Framework for Identifying the *k*-Length High-Utility Routes in Urban Traffic Networks

## Overview
Urban traffic congestion significantly impacts economic productivity and quality of life. Identifying **high-utility routes** within urban road networks is essential for efficient transportation planning and policy design.  

This study introduces **K-LHUR**, a novel **data-driven framework** designed to identify *k*-length high-utility routes that reflect overall network performance more comprehensively than traditional measures (e.g., volume-over-capacity or level-of-service).

## Key Innovation
K-LHUR constructs a **weighted utility graph** integrating:
- **Traffic flow utilization**, and  
- **Speed utilization**  

This fusion provides a multidimensional assessment of route performance, enabling the discovery of critical road segments that influence system-wide efficiency.

## Methodological Components
The framework integrates four major analytical components:

1. **Partial Bayesian Network** – Estimates latent traffic flow conditions.  
2. **K-Means Clustering** – Determines optimal thresholds for critical speed and capacity.  
3. **Dijkstra’s Algorithm** – Computes feasible and efficient *k*-length routes.  
4. **Parallel FP-Growth Algorithm** – Identifies frequent high-utility route patterns.

Each component contributes to computing a **composite priority score** for ranking *k*-length routes based on comprehensive utilization metrics.

## Experimental Validation
K-LHUR was validated using both **real-world traffic data** and **noise-augmented simulation data**. The results confirm that:
- The framework achieves **high accuracy in flow estimation**.  
- Weighted utilization metrics are **theoretically consistent and empirically validated**.  
- The identified routes and road segments **align with key congestion and efficiency hotspots**, offering actionable insights for policy-makers and transport planners.

## Policy and Planning Implications
The K-LHUR framework supports:
- **Data-driven prioritization** of road maintenance and upgrades,  
- **Optimization of traffic management strategies**, and  
- **Evidence-based infrastructure investments** aligned with smart-city objectives.

## Repository Information
- **Dataset:** [http://research.microsoft.com/apps/pubs/?id=217455](http://research.microsoft.com/apps/pubs/?id=217455)  
- **Source Code:** [https://github.com/Shahid-cse/K-LHUR](https://github.com/Shahid-cse/K-LHUR)

## Citation
If you use this framework in your research, please cite:

> Md. Shahiduzzaman, Md. Fazle Rabbi, Muhammad Abdullah Adnan.  
> *K-LHUR: A novel data-driven framework for identifying the k-length for high-utility routes in urban traffic networks.*  
> (Manuscript submitted to *Transportation Research Part D: Transport and Environment*.)

---

### License
This repository is released for academic and research use only. Proper citation is required when reproducing or adapting results.

