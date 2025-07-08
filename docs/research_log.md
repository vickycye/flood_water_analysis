[//]: # (This file will document the key concepts I'm learning, the data sources I find, questions that arise, and daily progress notes)

### June 25th, 2025 - June 29th, 2025
Selected pilot location: Snohomish River at Monroe

Available data: 
![Pilot location gauge info](images/gauge_mrow1.png)
![Gauge height, feet info](images/detailed_gauge_info_mrow1.png)

Set up `requirements.txt` and overall repo structure.
Set up conda virtual environment as well.

Stage-Discharge Relationship slides: ![Stage-Discharge Realtionship](https://ca.water.usgs.gov/FERC/presentations/Rating_shape-extensions.pdf)
Found USGS API for efficient data collection: ![API website](https://api.waterdata.usgs.gov/)
Good visual on trends of water flow: ![Rating curve example](https://www.researchgate.net/profile/Ida-Westerberg-2/publication/281460381/figure/fig8/AS:280667301662788@1443927708023/Uncertainties-in-rating-curve-modeling-of-the-stage-discharge-relationship-with-examples.png)

### June 30th, 2025 - July 4th, 2025
Learning how scraping works from this ![YouTube link](https://www.youtube.com/watch?v=8dTpNajxaH0)

Find this table for flood threshold:
`<table class="categories-table uk-table table-xsmall uk-table-divider svelte-17s0s5l">`

Apparently, it's not static on the website, so I have to go under the "Network" tab to find the api request, which comes from: 
`response = requests.get('https://api.water.noaa.gov/nwps/v1/gauges/SNZM7')`. 

First trial scrape worked, now trying to scrape for all sites, so I created the `WA_site_codes.ipynb` file to scrape those as well from ![USGS waterdata website](https://waterdata.usgs.gov/state/Washington/).

### July 7th - July 11th
There are a total of 120 reference gauges in Washington states that I extracted from the GAGES-II dataset.
Data location: ![GAGES-II](https://www.sciencebase.gov/catalog/item/631405bbd34e36012efa304a), ![USGS Summary](https://data.usgs.gov/datacatalog/data/USGS:1d623649-ccb9-4238-8add-3174bc322fdf)

USGS Rating Curves: ![Base](https://waterdata.usgs.gov/nwisweb/get_ratings?site_no=12150800&file_type=base), ![exsa](https://waterdata.usgs.gov/nwisweb/get_ratings?site_no=12150800&file_type=exsa). Replace "12150800" with another site name to find other info.

Scraped flood levels for all sites and exported to a .csv. 
The following stations are operated seasonally:
* 12020800, 12020525, etc.