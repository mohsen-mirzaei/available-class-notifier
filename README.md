# Sess available class notifier
Notifies you by playing an alarm sound when specific sections of a class on SESS become available.

## Requirements
- Python 3.8+
- Google Chrome installed
- Internet access

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

## Configure
Open `main.py` and adjust these variables at the top of the file:

- `COURSES`: A mapping of course number (as shown on SESS) to a list of desired section numbers.
- `SOUND_PATH`: Path to the sound file that will be played for alerts (default: `alarm.mp3`).
- `WAIT_TIME`: Seconds to wait between each scan cycle (default: 15).

Example (already in the file):

```python
COURSES = {
	"۱۲۰۶۳۱۸۰۱": [4, 5],
	"۱۲۰۶۳۱۱۴۱": [1]
}
SOUND_PATH = "alarm.mp3"
WAIT_TIME = 15
```

Notes:
- Copy the course numbers exactly as displayed on SESS. The script searches the page text for those strings.

## Run
```powershell
python .\main.py
```

When Chrome opens:
1. Log in to your SESS account.
2. Navigate to the "برنامه کلاسی نیمسال" page and select the appropriate "نیمسال" and "بخش".
3. In the terminal, press Enter when prompted ("Navigate to desired page and press enter to continue").

The script will:
- Iterate through the configured courses and sections.
- Open each row, read current student count and total capacity.
- Print a line with timestamp, section, counts, and free capacity.
- If free capacity is not zero, it will continuously play the alarm sound until you stop the script.

Stop the script with Ctrl+C in the terminal.
