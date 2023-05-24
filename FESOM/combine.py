import yaml

# Load the three catalogs
with open('IFS_4.4-FESOM_5-cycle3.yaml', 'r') as file:
    catalog1 = yaml.safe_load(file)

with open('IFS_4.4-FESOM_5-cycle3_interpolated.yaml', 'r') as file:
    catalog2 = yaml.safe_load(file)

with open('IFS_4.4-FESOM_5-cycle3_zarr.yaml', 'r') as file:
    catalog3 = yaml.safe_load(file)

# Merge the 'sources' from all catalogs
combined_sources = {**catalog1['sources'], **catalog2['sources'], **catalog3['sources']}

# Define the plugins
plugins = {
    'source': [
        {'module': 'intake_xarray'}
    ]
}

# Prepare the combined catalog
combined_catalog = {'plugins': plugins, 'sources': combined_sources}

# Write the combined catalog to a new YAML file
with open('combined_catalog.yaml', 'w') as file:
    yaml.dump(combined_catalog, file)
