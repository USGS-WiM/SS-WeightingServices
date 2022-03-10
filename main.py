from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ChannelWidthWeighting import weightEst2, weightEst3, weightEst4


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

class WeightEst2(BaseModel):

    # all fields are required
    x1: float
    x2: float
    sep1: float
    sep2: float
    regressionRegionCode: str
    code1: str
    code2: str

    class Config:
        schema_extra = {
            "example": {
                "x1": 1.607,
                "x2": 1.802,
                "sep1": 0.554,
                "sep2": 0.677,
                "regressionRegionCode": "GC1847",
                "code1": "PK1AEP",
                "code2": "BFPK1AEP"
            }
        }


class WeightEst3(BaseModel):

    # all fields are required
    x1: float
    x2: float
    x3: float
    sep1: float
    sep2: float
    sep3: float
    regressionRegionCode: str
    code1: str
    code2: str
    code3: str

    class Config:
        schema_extra = {
            "example": {
                "x1": 2.74,
                "x2": 2.45,
                "x3": 2.50,
                "sep1": 0.234,
                "sep2": 0.262,
                "sep3": 0.283,
                "regressionRegionCode": "GC1851",
                "code1": "PK1AEP",
                "code2": "ACPK1AEP",
                "code3": "BFPK1AEP"
            }
        }

class WeightEst4(BaseModel):

    # all fields are required
    x1: float
    x2: float
    x3: float
    x4: float
    sep1: float
    sep2: float
    sep3: float
    sep4: float
    regressionRegionCode: str
    code1: str
    code2: str
    code3: str
    code4: str

    class Config:
        schema_extra = {
            "example": {
                "x1": 2.74,
                "x2": 2.45,
                "x3": 2.50,
                "x4": 2.60,
                "sep1": 0.234,
                "sep2": 0.262,
                "sep3": 0.283,
                "sep4": 0.299,
                "regressionRegionCode": "GC1851",
                "code1": "PK1AEP",
                "code2": "ACPK1AEP",
                "code3": "BFPK1AEP",
                "code4": "RSPK1AEP"
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


@app.post("/weightest2/")
def weightest2(request_body: WeightEst2):

    z, sepz = weightEst2(
        request_body.x1,
        request_body.x2,
        request_body.sep1,
        request_body.sep2,
        request_body.regressionRegionCode,
        request_body.code1,
        request_body.code2
    )

    return {
        "Z": z,
        "SEPZ": sepz
    }


@app.post("/weightest3/")
def weightest3(request_body: WeightEst3):

    z, sepz = weightEst3(
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

    return {
        "Z": z,
        "SEPZ": sepz
    }

@app.post("/weightest4/")
def weightest4(request_body: WeightEst4, response: Response):

    z, sepz = weightEst4(
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

    response.headers["warning"] = "Only 3 channel width estimation methods can be weighted. The 3 methods with the lowest SEP values were weighted."

    return {
        "Z": z,
        "SEPZ": sepz
    }