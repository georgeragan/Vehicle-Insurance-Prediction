from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run
from pydantic import BaseModel

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier

# Initialize FastAPI application
app = FastAPI()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

# Allow all origins for Cross-Origin Resource Sharing (CORS)
origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VehicleDataModel(BaseModel):
    Gender: int
    Age: int
    Driving_License: int
    Region_Code: float
    Previously_Insured: int
    Annual_Premium: float
    Policy_Sales_Channel: float
    Vintage: int
    Vehicle_Age_lt_1_Year: int
    Vehicle_Age_gt_2_Years: int
    Vehicle_Damage_Yes: int

# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for vehicle data input.
    """
    return templates.TemplateResponse(request, "vehicledata.html", {"context": "Rendering"})

# Route to handle form submission and make predictions
@app.post("/")
async def predictRouteClient(request: Request, data: VehicleDataModel):
    """
    Endpoint to receive form data, process it, and make a prediction.
    """
    try:
        vehicle_data = VehicleData(
                                Gender=data.Gender,
                                Age=data.Age,
                                Driving_License=data.Driving_License,
                                Region_Code=data.Region_Code,
                                Previously_Insured=data.Previously_Insured,
                                Annual_Premium=data.Annual_Premium,
                                Policy_Sales_Channel=data.Policy_Sales_Channel,
                                Vintage=data.Vintage,
                                Vehicle_Age_lt_1_Year=data.Vehicle_Age_lt_1_Year,
                                Vehicle_Age_gt_2_Years=data.Vehicle_Age_gt_2_Years,
                                Vehicle_Damage_Yes=data.Vehicle_Damage_Yes
                                )

        # Convert form data into a DataFrame for the model
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Initialize the prediction pipeline
        model_predictor = VehicleDataClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=vehicle_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

        # Render the same HTML page with the prediction result
        return templates.TemplateResponse(request, "vehicledata.html", {"context": status})
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)