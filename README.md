### This is Event LLM research project repository.

notebooks folder:
The notebooks folder contains different folders for different tasks

1.1_understand_events

For three different types of events, the datasets are loaded in pandas dataframe and checked with basic properties- no. of columns, datetimes, etc.

1.2_spatial_distribution

This contains notebook to visualize spatial distribution of the events on a map. Two functions to produce such spatial distribution are also written in utils/spatial folder.

1.3_time_frequency

This folder contains notebook to visualize the time distribution in different ways.

1.4_assign_cbgid

spatial join between events GEO location and shapefile to assign CBGID to events data.

1.5_join_event_with_mobility

Assign #visits from mobility data on events data based on hour, date and CBGID.