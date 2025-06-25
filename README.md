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
Might move this section later

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

---
Public repository for data analysis @ UW's EarthLab and Climate Impacts Group. 
Duration: 9-week summer research internship
Contact: vickyye@uw.edu