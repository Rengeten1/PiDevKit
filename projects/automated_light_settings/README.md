# Automated Light Settings for Raspberry Pi

This project provides a program to automate the control of lighting using a Raspberry Pi Zero 2 W. It allows users to schedule lights to turn on or off based on predefined times or sensor input. The program retrieves sunset data from Open-Meteo through an API call that runs daily at a specified time. Based on this data, the lights turn on at sunset and turn off at another predefined time.

- Turns on after sunset
- Turns off at 10:30 PM automatically

## Setup

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Edit Bluetooth addresses and settings in `main.py` and `turn_off.py` as needed.**

3. **Set up the following cron jobs (run `crontab -e`):**
   ```
   0 18 * * * /usr/bin/python3 /path/to/your/project/main.py
   30 22 * * * /usr/bin/python3 /path/to/your/project/turn_off.py
   ```

## Files

- `main.py` – Turns the light on after sunset
- `turn_off.py` – Turns the light off at 10:30 PM
- `data.py` – Gets today's sunset time from Open-Meteo
- `time_utils.py` – Gets current UTC time

## Requirements

- Python 3.7+
- [bleak](https://pypi.org/project/bleak/)
- [openmeteo-requests](https://pypi.org/project/openmeteo-requests/)
- [requests-cache](https://pypi.org/project/requests-cache/)
- [retry-requests](https://pypi.org/project/retry-requests/)
- pandas

Install everything with:
```
pip install bleak openmeteo-requests requests-cache retry-requests pandas
```