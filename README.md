![WiM](wim.png)

# StreamStats Channel Width Weighting Services

This is the basic FastAPI setup of the ChannelWidthWeightingServices. Service documentation can be found at https://channelwidthweighting.streamstats.usgs.gov/docs/.

## Prerequisites

```text
Python 3
FastAPI
Uvicorn or Gunicorn
```

To run the services locally, run the following in your Windows command prompt:

```bash
# create a virtual environment
python -m venv env
# active the virtual environment
. env/Scripts/activate
# install the project's dependencies
pip install -r requirements.txt
# deploy at a local server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Once the above code has been run successfully, the service documentation will be available at http://127.0.0.1:8000/docs/.

You can make an example `POST` call to http://127.0.0.1:8000/weightest2 with the following JSON body representing the inputs:

```text
{"x1": 1.607, "x2": 1.802, "sep1": 0.554, "sep2": 0.677, "r12": 0.658}
```

You can also make an example `POST` call to http://127.0.0.1:8000/weightest3 with the following JSON body representing the inputs:

```text
{"x1": 2.74, "x2": 2.45, "x3": 2.5, "sep1": 0.234, "sep2": 0.262, "sep3": 0.283, "r12": 0.553, "r13": 0.518, "r23": 0.907}
```

## Authors

- **[Seth Siefen](https://www.usgs.gov/staff-profiles/seth-siefken)** - *Channel Width Weighting Script Author* - [USGS Wyoming-Montana Water Science Center](https://www.usgs.gov/centers/wyoming-montana-water-science-center/)
- **[Aaron Stephenson](https://github.com/aaronstephenson)**  - *Web Developer* - [USGS Web Informatics & Mapping](https://wim.usgs.gov/)

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
