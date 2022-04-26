![WiM](wim.png)

# StreamStats Channel Width Weighting Services

This is the basic FastAPI setup of the ChannelWidthWeightingServices. Service documentation can be found at https://ss-weightingservices.streamstats.usgs.gov/docs.

## Prerequisites

```text
Python 3
```

To run the services locally, run the following in your Windows command prompt:

```bash
# create a virtual environment
python -m venv env
# active the virtual environment
.\env\Scripts\activate
# install the project's dependencies
pip install -r requirements.txt
# deploy at a local server
uvicorn main:app --host 0.0.0.0 --port 8000
```

Alternate instructions for the Windows Anaconda3 prompt:

```bash
# create a new Conda environment
conda create --name ss-weightingservices
# active the Conda environment
conda activate ss-weightingservices
# install the project's dependencies
conda install pip
pip install -r requirements.txt
# deploy at a local server
uvicorn main:app --host 0.0.0.0 --port 8000
```

Once the above code has been run successfully, the service documentation will be available at http://127.0.0.1:8000/docs/.

You can make an example `POST` call to http://127.0.0.1:8000/weightest with the following JSON body representing the inputs:

```text
{"x1": 549.54, "x2": null, "x3": null, "x4": 398.11, "sep1": 0.234, "sep2": null, "sep3": null, "sep4": 0.299, "regressionRegionCode": "GC1851", "code1": "PK1AEP", "code2": null, "code3": null, "code4": "RSPK1AEP"}
```

You can make an example `POST` call to http://127.0.0.1:8000/weightest2 with the following JSON body representing the inputs:

```text
{"x1": 40.46, "x2": 63.39, "sep1": 0.554, "sep2": 0.677, "regressionRegionCode": "GC1847", "code1": "PK1AEP", "code2": "BWPK1AEP"}
```

You can make an example `POST` call to http://127.0.0.1:8000/weightest3 with the following JSON body representing the inputs:

```text
{"x1": 549.54, "x2": 281.84, "x3": 316.23, "sep1": 0.234, "sep2": 0.262, "sep3": 0.283, "regressionRegionCode": "GC1851", "code1": "PK1AEP", "code2": "ACPK1AEP", "code3": "BWPK1AEP"}
```

You can make an example `POST` call to http://127.0.0.1:8000/weightest4 with the following JSON body representing the inputs:

```text
{"x1": 549.54, "x2": 281.84, "x3": 316.23, "x4": 398.11, "sep1": 0.234, "sep2": 0.262, "sep3": 0.283, "sep4": 0.299, "regressionRegionCode": "GC1851", "code1": "PK1AEP", "code2": "ACPK1AEP", "code3": "BFPK1AEP", "code4": "RSPK1AEP"}
```
## Deployment

1. [Contact SysOps](https://github.com/USGS-WiM/wim-infrastructure/issues/new) to request access to the FastAPI_Services server
2. Use [Putty](https://www.putty.org/) to SSH onto the FastAPI_Services server. In the Putty Configuration:
     - Host Name: `<you_username>@FastAPI_Services_hostname_or_IP_address`
     - Port: 22
     - Connection type: SSH
     - In the sidebar, Connection > SSH > Auth: "Private key file for authentication:" click "Browse" to upload your private key file
     - Click "Open" to connect
 3. Go to the app directory: `cd /var/www/SS-WeightingServices`
 4. Pull the latest code: `sudo git pull origin master`
 5. Restart the daemon: `sudo systemctl restart channelwidthweighting`
 6. Check that the services were updated: https://ss-weightingservices.streamstats.usgs.gov/docs
 7. Exit when finished: `exit`

## Authors

- **[Seth Siefen](https://www.usgs.gov/staff-profiles/seth-siefken)** - *Channel Width Weighting Script Author* - [USGS Wyoming-Montana Water Science Center](https://www.usgs.gov/centers/wyoming-montana-water-science-center/)
- **[Aaron Stephenson](https://github.com/aaronstephenson)**  - *Web Developer* - [USGS Web Informatics & Mapping](https://wim.usgs.gov/)
- **[Andrea Medenblik](https://github.com/amedenblik)**  - *Web Developer* - [USGS Web Informatics & Mapping](https://wim.usgs.gov/)
- **[Harper Wavra](https://github.com/harper-wavra)**  - *Web Developer* - [USGS Web Informatics & Mapping](https://wim.usgs.gov/)

See also the list of [contributors](../../graphs/contributors) who participated in this project.

## License

This project is licensed under the Creative Commons CC0 1.0 Universal License - see the [LICENSE.md](LICENSE.md) file for details

## Suggested Citation

In the spirit of open source, please cite any re-use of the source code stored in this repository. Below is the suggested citation:

`This project contains code produced by the Wyoming-Montana Water Science Center and the Web Informatics and Mapping (WIM) team at the United States Geological Survey (USGS). As a work of the United States Government, this project is in the public domain within the United States. https://wim.usgs.gov`

## About WIM

- This project authored by the [USGS WIM team](https://wim.usgs.gov)
- WIM is a team of developers and technologists who build and manage tools, software, web services, and databases to support USGS science and other federal government cooperators.
- WIM is a part of the [Upper Midwest Water Science Center](https://www.usgs.gov/centers/upper-midwest-water-science-center).
