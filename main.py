from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import json

from ChannelWidthWeighting import weightEst, weightEst2, weightEst3, weightEst4


app = FastAPI(
    title='Channel Width Weighting Services',
    openapi_url='/openapi.json',
    docs_url='/docs'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

######
##
## Pydantic Schemas
##
######

# These schemas provide format and data type validation
#  of request body inputs, and automated API documentation

class WeightEst(BaseModel): # NOT WORKING

    x1: float = Field(default=None, title="Statstic Value 1", description="Value of first statistic (float)", example="122")
    x2: float = Field(default=None, title="Statstic Value 2", description="Value of second statistic (float)", example="null")
    x3: float = Field(default=None, itle="Statstic Value 3", description="Value of third statistic (float)", example="null")
    x4: float = Field(default=None, title="Statstic Value 4", description="Value of fourth statistic (float)", example="26.6")
    sep1: float = Field(default=None, title="SEP Value 1", description="Mean standard error of prediction value of first statistic (float)", example="0.483")
    sep2: float = Field(default=None, title="SEP Value 2", description="Mean standard error of prediction value of second statistic (float)", example="null")
    sep3: float = Field(default=None, title="SEP Value 3", description="Mean standard error of prediction value of third statistic (float)", example="null")
    sep4: float = Field(default=None, title="SEP Value 4", description="Mean standard error of prediction value of fourth statistic (float)", example="0.538")
    regressionRegionCode: str = Field(..., title="Regression Region Code", description="Code for regression region", example="GC1834")
    code1: str = Field(default=None, title="Statistic Code 1", description="Code for first statistic", example="ACPK66_7AE")
    code2: str = Field(default=None, title="Statistic Code 2", description="Code for second statistic", example="null")
    code3: str = Field(default=None, title="Statistic Code 3", description="Code for third statistic", example="null")
    code4: str = Field(default=None, title="Statistic Code 4", description="Code for fourth statistic", example="RSPK66_7AE")

    class Config:
        null = None
        schema_extra = {
            "example": {
                "x1": 122,
                "x2": null,
                "x3": null,
                "x4": 26.6,
                "sep1": 0.483,
                "sep2": null,
                "sep3": null,
                "sep4": 0.538,
                "regressionRegionCode": "GC1834",
                "code1": "ACPK66_7AE",
                "code2": null,
                "code3": null,
                "code4": "RSPK66_7AE"
            }
        }

class WeightEst2(BaseModel):

    # all fields are required
    x1: float = Field(..., title="Statstic Value 1", description="Value of first statistic (float)", example="122")
    x2: float = Field(..., title="Statstic Value 2", description="Value of second statistic (float)", example="8.24")
    sep1: float = Field(..., title="SEP Value 1", description="Mean standard error of prediction value of first statistic (float)", example="0.483")
    sep2: float = Field(..., title="SEP Value 2", description="Mean standard error of prediction value of second statistic (float)", example="0.376")
    regressionRegionCode: str = Field(..., title="Regression Region Code", description="Code for regression region", example="GC1832")
    code1: str = Field(..., title="Statistic Code 1", description="Code for first statistic", example="ACPK66_7AE")
    code2: str = Field(..., title="Statistic Code 2", description="Code for second statistic", example="PK66_7AEP")

    class Config:
        schema_extra = {
            "example": {
                "x1": 122,
                "x2": 8.24,
                "sep1": 0.483,
                "sep2": 0.376,
                "regressionRegionCode": "GC1832",
                "code1": "ACPK66_7AE",
                "code2": "PK66_7AEP"
            }
        }


class WeightEst3(BaseModel):

    # all fields are required
    x1: float = Field(..., title="Statstic Value 1", description="Value of first statistic (float)", example="122")
    x2: float = Field(..., title="Statstic Value 2", description="Value of second statistic (float)", example="8.24")
    x3: float = Field(..., title="Statstic Value 3", description="Value of third statistic (float)", example="45.9")
    sep1: float = Field(..., title="SEP Value 1", description="Mean standard error of prediction value of first statistic (float)", example="0.483")
    sep2: float = Field(..., title="SEP Value 2", description="Mean standard error of prediction value of second statistic (float)", example="0.376")
    sep3: float = Field(..., title="SEP Value 3", description="Mean standard error of prediction value of third statistic (float)", example="0.467")
    regressionRegionCode: str = Field(..., title="Regression Region Code", description="Code for regression region", example="GC1833")
    code1: str = Field(..., title="Statistic Code 1", description="Code for first statistic", example="ACPK66_7AE")
    code2: str = Field(..., title="Statistic Code 2", description="Code for second statistic", example="PK66_7AEP")
    code3: str = Field(..., title="Statistic Code 3", description="Code for third statistic", example="BWPK66_7AE")

    class Config:
        schema_extra = {
            "example": {
                "x1": 122,
                "x2": 8.24,
                "x3": 45.9,
                "sep1": 0.483,
                "sep2": 0.376,
                "sep3": 0.467,
                "regressionRegionCode": "GC1833",
                "code1": "ACPK66_7AE",
                "code2": "PK66_7AEP",
                "code3": "BWPK66_7AE"
            }
        }

class WeightEst4(BaseModel):

    # all fields are required
    x1: float = Field(..., title="Statstic Value 1", description="Value of first statistic (float)", example="122")
    x2: float = Field(..., title="Statstic Value 2", description="Value of second statistic (float)", example="8.24")
    x3: float = Field(..., title="Statstic Value 3", description="Value of third statistic (float)", example="45.9")
    x4: float = Field(..., title="Statstic Value 4", description="Value of fourth statistic (float)", example="26.6")
    sep1: float = Field(..., title="SEP Value 1", description="Mean standard error of prediction value of first statistic (float)", example="0.483")
    sep2: float = Field(..., title="SEP Value 2", description="Mean standard error of prediction value of second statistic (float)", example="0.376")
    sep3: float = Field(..., title="SEP Value 3", description="Mean standard error of prediction value of third statistic (float)", example="0.467")
    sep4: float = Field(..., title="SEP Value 4", description="Mean standard error of prediction value of fourth statistic (float)", example="0.538")
    regressionRegionCode: str = Field(..., title="Regression Region Code", description="Code for regression region", example="GC1834")
    code1: str = Field(..., title="Statistic Code 1", description="Code for first statistic", example="ACPK66_7AE")
    code2: str = Field(..., title="Statistic Code 2", description="Code for second statistic", example="PK66_7AEP")
    code3: str = Field(..., title="Statistic Code 3", description="Code for third statistic", example="BWPK66_7AE")
    code4: str = Field(..., title="Statistic Code 4", description="Code for fourth statistic", example="RSPK66_7AE")

    class Config:
        schema_extra = {
            "example": {
                "x1": 122,
                "x2": 8.24,
                "x3": 45.9,
                "x4": 26.6,
                "sep1": 0.483,
                "sep2": 0.376,
                "sep3": 0.467,
                "sep4": 0.538,
                "regressionRegionCode": "GC1834",
                "code1": "ACPK66_7AE",
                "code2": "PK66_7AEP",
                "code3": "BWPK66_7AE",
                "code4": "RSPK66_7AE"
            }
        }

######
##
## API Endpoints
##
######


# redirect root and /settings.SERVICE_NAME to the docs
@app.get("/", include_in_schema=False)
def docs_redirect_root():
    return RedirectResponse(url=app.docs_url)

@app.post("/weightest/")
def weightest(request_body: WeightEst, response: Response):

    try:
        Z, SEPZ, CI, PIL, PIU, warningMessage  = weightEst(
            request_body.x1,
            request_body.x2,
            request_body.x3,
            request_body.x4,
            request_body.sep1,
            request_body.sep2,
            request_body.sep3,
            request_body.sep4,
            request_body.regressionRegionCode,
            request_body.code1,
            request_body.code2,
            request_body.code3,
            request_body.code4,
        )
        if warningMessage is not None:
            response.headers["X-USGSWIM-Messages"] = json.dumps({'warning': warningMessage})
        response.headers["Access-Control-Expose-Headers"] = "X-USGSWIM-Messages"
        return {
            "Z": Z,
            "SEPZ": SEPZ,
            "CI": CI,
            "PIL": PIL,
            "PIU": PIU
        }

    except Exception as e:
        raise HTTPException(status_code = 500, detail =  str(e))

@app.post("/weightest2/")
def weightest2(request_body: WeightEst2, response: Response):

    try: 
        Z, SEPZ, CI, PIL, PIU, warningMessage = weightEst2(
            request_body.x1,
            request_body.x2,
            request_body.sep1,
            request_body.sep2,
            request_body.regressionRegionCode,
            request_body.code1,
            request_body.code2
        )
        if warningMessage is not None:
            response.headers["X-USGSWIM-Messages"] = json.dumps({'warning': warningMessage})
        response.headers["Access-Control-Expose-Headers"] = "X-USGSWIM-Messages"
        return {
            "Z": Z,
            "SEPZ": SEPZ,
            "CI": CI,
            "PIL": PIL,
            "PIU": PIU
        }

    except Exception as e:
        raise HTTPException(status_code = 500, detail =  str(e))

@app.post("/weightest3/")
def weightest3(request_body: WeightEst3, response: Response):

    try:
        Z, SEPZ, CI, PIL, PIU, warningMessage = weightEst3(
            request_body.x1,
            request_body.x2,
            request_body.x3,
            request_body.sep1,
            request_body.sep2,
            request_body.sep3,
            request_body.regressionRegionCode,
            request_body.code1,
            request_body.code2,
            request_body.code3
        )
        if warningMessage is not None:
            response.headers["X-USGSWIM-Messages"] = json.dumps({'warning': warningMessage})
        response.headers["Access-Control-Expose-Headers"] = "X-USGSWIM-Messages"
        return {
            "Z": Z,
            "SEPZ": SEPZ,
            "CI": CI,
            "PIL": PIL,
            "PIU": PIU
        }

    except Exception as e:
        raise HTTPException(status_code = 500, detail =  str(e))


@app.post("/weightest4/")
def weightest4(request_body: WeightEst4, response: Response):

    try:
        Z, SEPZ, CI, PIL, PIU, warningMessage = weightEst4(
            request_body.x1,
            request_body.x2,
            request_body.x3,
            request_body.x4,
            request_body.sep1,
            request_body.sep2,
            request_body.sep3,
            request_body.sep4,
            request_body.regressionRegionCode,
            request_body.code1,
            request_body.code2,
            request_body.code3,
            request_body.code4,
        )
        if warningMessage is not None:
            response.headers["X-USGSWIM-Messages"] = json.dumps({'warning': warningMessage})
        response.headers["Access-Control-Expose-Headers"] = "X-USGSWIM-Messages"
        return {
            "Z": Z,
            "SEPZ": SEPZ,
            "CI": CI,
            "PIL": PIL,
            "PIU": PIU
        }

    except Exception as e:
        raise HTTPException(status_code = 500, detail =  str(e))
