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
<table class="categories-table uk-table table-xsmall uk-table-divider svelte-17s0s5l"><thead><tr class="font-size-13 headings" style="background: rgb(240, 240, 240);"><th class="header svelte-17s0s5l" aria-label="Flood categories table"></th> <th class="header bold-black svelte-17s0s5l">CATEGORY</th> <th class="header bold-black svelte-17s0s5l">STAGE</th></tr></thead> <tbody><tr class="font-size-13" style="background: rgba(204, 51, 255, 0.1);"><td class="color svelte-17s0s5l" style="background: rgb(204, 51, 255);"><img alt="open-category-button" class="open-category-button-img" src="/assets/components/hydrograph/public/images/chevron-right.svg" style="" aria-label="Toggle open major category"></td> <td class="category uk-text-bold svelte-17s0s5l">Major Flooding</td> <td class="uk-text-bold svelte-17s0s5l">40 ft</td></tr> <tr class="font-size-13" style="background: rgba(255, 0, 0, 0.1);"><td class="color svelte-17s0s5l" style="background: rgb(255, 0, 0);"><img alt="open-category-button" class="open-category-button-img" src="/assets/components/hydrograph/public/images/chevron-right.svg" style="" aria-label="Toggle open moderate category"></td> <td class="category uk-text-bold svelte-17s0s5l">Moderate Flooding</td> <td class="uk-text-bold svelte-17s0s5l">28 ft</td></tr> <tr class="font-size-13" style="background: rgba(255, 153, 0, 0.1);"><td class="color svelte-17s0s5l" style="background: rgb(255, 153, 0);"><img alt="open-category-button" class="open-category-button-img" src="/assets/components/hydrograph/public/images/chevron-right.svg" style="" aria-label="Toggle open minor category"></td> <td class="category uk-text-bold svelte-17s0s5l">Minor Flooding</td> <td class="uk-text-bold svelte-17s0s5l">26 ft</td></tr> <tr class="font-size-13" style="background: rgba(255, 255, 0, 0.1);"><td class="color svelte-17s0s5l" style="background: rgb(255, 255, 0);"><img alt="open-category-button" class="open-category-button-img" src="/assets/components/hydrograph/public/images/chevron-right.svg" style="" aria-label="Toggle open action category"></td> <td class="category uk-text-bold svelte-17s0s5l">Action</td> <td class="uk-text-bold svelte-17s0s5l">21 ft</td></tr> </tbody></table>

Specifically, this: <table class="categories-table uk-table table-xsmall uk-table-divider svelte-17s0s5l">

Apparently, it's not static on the website, so I have to go under the "Network" tab to find the api request, which comes from: 
`response = requests.get('https://api.water.noaa.gov/nwps/v1/gauges/SNZM7')`. 