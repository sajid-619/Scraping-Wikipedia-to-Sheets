# Scraping-Wikipedia-to-Sheets

This is a Python script that scrapes data from Wikipedia pages and saves them as Google Sheets. It uses the requests, BeautifulSoup, gspread and oauth2client modules to perform the scraping and the sheet operations.

#How to use

1. Clone this repository. Then use the following command to activate virtualenv:

    ```python3 -m venv env
       source env/Scripts/activate 
    ```

2. Install the required modules using 
    
    ```
    pip install -r requirements.txt

    ```

3. Create a Google API project and enable the Google Sheets API. Download the credentials file as ***credentials.json*** and place it in the same folder as the script.

4. Run the script using ***python scrape_wiki.py***.

5. Enter the name of the Google Sheet you want to create or use. If it does not exist, it will be created automatically.

6. The script will scrape the data from the Wikipedia page and save it as a Google Sheet in your Google Drive. You can view and edit the sheet online.
