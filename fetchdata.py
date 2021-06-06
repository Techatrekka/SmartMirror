import requests, json
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class fetchdata:    

    def getWeatherUpdate():
        openweatherAPIkey = "251ef3dcc8d484ad7170cb8fe5c4b8f1"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Cratloe"
        complete_url = base_url + "appid=" + openweatherAPIkey + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            current_temperature = round(current_temperature - 273.15,1)
            data = [current_temperature, current_pressure,
                    current_humidity, weather_description]
            
            return data
  
        else:
            print(" City Not Found ")


    def getCalendarInfo():
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        calendarId = "saslynch12@gmail.com"
        base_url = "https://www.googleapis.com/calendar/v3/calendars/"+calendarId+"/events"
        
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events

