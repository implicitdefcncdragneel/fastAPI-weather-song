## Installation and Launching

1. Create a env file command: `python -m venv env` and activate: `source env/Scripts/activate`
2. Install the required dependencies specified in the `requirements.txt` file command: `pip install -r requirements`.
3. Launch the application with uvicorn command: `uvicorn main:app --reload`

# Folder Structure

https://fastapi.tiangolo.com/tutorial/bigger-applications/


## Testing and Coverage

1. Launch the mock server located in mockServer folder command: `npm install` then `npm start` 
2. Do coverage check command: `coverage run -m pytest` and report command: `coverage report`.

## Contact

For any questions or inquiries, please contact [chandranandan.chandrakar@gmail.com](mailto:chandranandan.chandrakar@gmail.com).

**Note:** 
1. Use your our API Key by visiting https://openweathermap.org/guide for OPEN_WEATHER_API_KEY and https://www.last.fm/api/authspec for OPEN_WEATHER_API_KEY
2. Create a .env file and insert OPEN_WEATHER_API_KEY and OPEN_WEATHER_API_KEY, reset application will take care.
3. In the repo `fastAPI-weather-song.postman_collection` is present for testing.