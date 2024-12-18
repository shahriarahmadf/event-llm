### This is Event LLM research project repository.

Project Folder Setup 

event-llm/
├── data_CityEvent/         
│   ├── cbg_features/               # Features data for census block groups (CBGs)
│   ├── Cityevents/                 # Raw event data and metadata
│   ├── SafeGraph/                  # Mobility data from SafeGraph
│   ├── Shp/                        # Shapefiles for spatial analysis
│   ├── Weather/                    # Weather data relevant to the events
│   ├── processed/                  # Preprocessed datasets
│       ├── 1_cbgid_assigned_by_category/
│           ├── unscheduled_intermediate/   # Intermediate data for unscheduled events
│       ├── 2_cbgid_downscaled/             # Downscaled CBG data
│       ├── 3_hourly_events_cbgid_category/ # Hourly event data categorized by CBG ID
│       ├── 4_events_join_w_mobility/       # Events joined with mobility data
│       ├── 5_processed_daily/              # Final processed daily data
├── results/         
│   ├── 1_box_plots/               # Box plots for visualizing results
├── coe_fall2024/                  # Files and documentation for the COE (Fall 2024)
├── experiment_notebooks/          # Jupyter notebooks for analysis and experiments
├── utils/ 
│   ├── spatial/                   # Utility scripts for spatial data processing
│   ├── time/                      # Utility scripts for time-related data processing
