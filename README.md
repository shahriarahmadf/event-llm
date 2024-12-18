### This is Event LLM research project repository.
#### MIT City Senseable Lab
##### UROP RESEARCH Fall 2024
Shahriar Ahmad Fahim
Supervised by Dr. Songhua Hu and Prof. Fabio Duarte

Note. Project Folder Setup for running the notebooks in folder_fall2024. After git cloning, if any of the below folder is missing, ** should be manually created to run the notebooks without error.

```
event-llm/
├── data_CityEvent/         
│   ├── cbg_features/               # Features data for census block groups (CBGs)
│   ├── Cityevents/                 # Raw event data and metadata
│   ├── SafeGraph/                  # Mobility data from SafeGraph
│   ├── Shp/                        # Shapefiles for spatial analysis
│   ├── Weather/                    # Weather data relevant to the events
│   ├── processed/                  # Preprocessed datasets
│       ├── 1_cbgid_assigned_by_category/   # Data after assigning CBGID, as separate file for each category
│           ├── unscheduled_intermediate/   # Intermediate (step) processed from for unscheduled data in assigning CBGID 
│       ├── 2_cbgid_downscaled/             # Downscaled CBG data
│       ├── 3_hourly_events_cbgid_category/ # Hourly event data categorized by CBG ID - exploded into rows
│       ├── 4_events_join_w_mobility/       # Events joined with mobility data
│       ├── 5_processed_daily/              # Final processed daily data - ready for boxplots
├── results/         
│   ├── 1_box_plots/               # Box plots results
├── code_fall2024/                 # All experiment code of Fall2024 wrapped up
├── experiment_notebooks/          # Notebooks that were used for experiments (not the best organized form)
├── utils/                         # Utility functions for assisting the main code 
│   ├── spatial/                   
│   ├── time/                      
├── requirements.txt/              # This file ensure all libraries to install  
```

The results folder may also contain additional results from experiments from experiment_notebooks.