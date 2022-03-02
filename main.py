from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ChannelWidthWeighting import weightEst2, weightEst3


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
    r12: float

    class Config:
        schema_extra = {
            "example": {
                "x1": 1.607,
                "x2": 1.802,
                "sep1": 0.554,
                "sep2": 0.677,
                "r12": 0.658
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
    r12: float
    r13: float
    r23: float

    class Config:
        schema_extra = {
            "example": {
                "x1": 2.74,
                "x2": 2.45,
                "x3": 2.50,
                "sep1": 0.234,
                "sep2": 0.262,
                "sep3": 0.283,
                "r12": 0.553,
                "r13": 0.518,
                "r23": 0.907
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
        request_body.r12
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
        request_body.r12,
        request_body.r13,
        request_body.r23
    )

    return {
        "Z": z,
        "SEPZ": sepz
    }
