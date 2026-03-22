import requests

URL = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata"

def get_current_time():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            return data.get("dateTime", "Time data not available")
        else:
            return "Unable to fetch time data."
    except Exception as e:
        print("An error occurred while fetching time data:", str(e))
        return "Error fetching time data."
    
# if __name__ == "__main__":
#     current_time = get_current_time()
#     print(f"The current time in Asia/Kolkata is: {current_time}")   