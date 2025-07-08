# Flood Warning Analysis
Welcome! This repository contains the analysis and methodology for estimating how climate change will affect flood warning frequencies in the PNW.

## Project Overview
This project develops methods to translate future streamflow projections into actionable flood risk information for communities. While climate models provide estimates of future water flow rates (discharge), communities and emergency managers need to understand how these changes will affect water levels (stage) and flood warning frequencies.

## Research Objectives
### Primary Target
Calculate changes in the frequency of flood warnings at major river gauges in the PNW using future streamflow projections.

### Specific Objectives
- **Develop and validate methods** for converting between stage and discharge using USGS rating curves
- **Address bias correction** in modeled streamflow to ensure accurate translations
- **Pilot the methodology** for the Snohomish River near Monroe, WA
- **Quantify uncertainty** in stage-discharge extrapolations for higher flow events
- **Create reproducible workflows** for expanding analysis to additional locations

## Data Sources
### Observational Data
- **USGS water data**: Historical stage and discharge measurements, rating curves
   - [Primary site: Snohomish River at Monroe (Site 12150800)](https://waterdata.usgs.gov/monitoring-location/USGS-12150800/#period=P7D&dataTypeId=continuous-00065-0)
- **NOAA/NWS River Forecasts**: Flood warning thresholds (Action, Minor, Moderate, Major)
   - [NWPS website](https://water.noaa.gov/wfo/sew)
- **USGS Rating Tables**: Stage-discharge relationships for unit conversions
   - [Relation example](https://www.usgs.gov/media/images/usgs-stage-discharge-relation-example)
   - [Rating Tables](https://waterdata.usgs.gov/wa/nwis/)

### Climate Projections
- **RMJOC-II Dataset**: River Management Joint Operating Committee's hydrologic projections
- **Pacific Northwest Hydroclimate Scenarios**: Historiiacl baseline comparison
- **Localized watershed studies**: Additional validation datasets


---

## Setup Instructions
If you wish, clone the GitHub repository into a remote server (atmos) via VS Code.
1. SSH into the remote server from VS Code--if you open the command palette and don't find the `Remote-SSH: Connect to Host` command, follow these steps:
   1. Install the Remote-SSH extension in VS Code (official extension by Microsoft)
   2. Set up your SSH host in VS Code. Open the command palette (Cmd/Ctrl + Shift + P) and type and select "Remote-SSH: Add new SSH Host...". Then enter the SSH command you normally use, something like `ssh [your username]@[server name]` and choose the default SSH config file `(~/.ssh/config)`. Now VS Code knows about your remote server.
2. Connect to your server via Remote-SSH
   1. Open the command palette and connect to the host, now the window should say `SSH: [server name]`
3. Open a terminal and clone this GitHub repo
   * Run `git clone https://github.com/username/repo-name.git
cd repo-name`
4. Install dependencies `pip install -r requirements.txt`
45 Now you can work with files remotely just like locally!

## Setting up conda environment on atmos server
If you're checking `python --version` or `python3 --version` and it shows `python 2.7.2` or `python 3.7.3` (or anything of the sorts), you need to create a conda virtual environment if you want to install certain packages.
First, try running `conda --version`. It should say command not found. 
**Install `miniconda3` on Linux**
1. Download the miniconda3 installer
   - Run the following command: `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
2. Run the installer
   - Run the following command: `bash Miniconda3-latest-Linux-x86_64.sh`. Press enter to start the installation, select `yes` if prompted to.
   - When asked for the install location, choose something like `/home/disk/cig-home/[yourusername]/miniconda3`
3. Initialize conda
   - Run the following command: `conda init` (this modifies the shell configuration `.bashrc`, `.zshrc`, etc. to enable conda automatically on login)
   - Reload the shell by running `source ~/.bashrc`
   - Run `conda --version` again to see if it's successfully installed.
4. (Optional) Clean things up a little
   - You can also run `rm Miniconda3-latest-Linux-x86_64.sh` to remove the installer but it's completely optional and I didn't do it.

Now it should work and you can run `conda install --yes --file requirements.txt` to install all necessary dependencies. 

---
## Github Structure

```bash
flood_water_analysis/
├── data/
│   ├── raw_data/                         # data retrieved directly from websites, etc.
│   ├── processed_data/                   # cleaned data (e.g., specific WA site codes)
│   ├── external/
│   ├── site_codes_all.txt                # from GAGES-II dataset (little human influence geographical location)
│   ├── site_codes_ref.txt                # same as above but washington state sites
│   └── scraped/
│       └── WA_sites.json                 # all WA gauge sites, contains decommissioned ones as well
├── docs/                  
│   ├── images/                           # misc. image storage
│   ├── pilot_location_analysis.md        # contains very specific information for one site
│   └── research_log.md                   # contains findings and summaries
├── notebooks/
│   ├── data_vix.py                       # script to gather reference gauges in WA state to make site_codes_ref.txt
│   ├── flood_levels_all_sites.csv        # spreadsheet for information on all scraped washingon gauge sites
│   ├── flood_levels_all_sites_valid.csv  # same as above but only the ones that have at least one flood warning threshold 
│   ├── flood_data_SNZM7.json             # pilot location detailed gauge and site information
│   ├── initial_data_exploration.ipynb    # jupyter notebook w/ pilot analysis
│   └── WA_site_codes.py                  # yet another script to scrape WA site locations
├── src/
├── venv/
├── LICENSE
├── README.md                             # this doc
└── requirements.txt                      # installs necessary dependencies for running all files in this repo.
```


---
Public repository for data analysis @ UW's EarthLab and Climate Impacts Group. 
Duration: 9-week summer research internship
Contact: vickyye@uw.edu