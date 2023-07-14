import requests
from bs4 import BeautifulSoup
from collections import Counter
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Scrape Wikipedia page and extract the main article text
def scrape_wikipedia():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    main_article = soup.find("div", id="mw-content-text").text
    return main_article

# Count the frequency of words in the text
def count_words(text):
    words = text.split()
    word_count = Counter(words)
    return word_count

# Insert the frequency count into Google Sheets
def insert_into_sheets(sorted_word_count):
    credentials = service_account.Credentials.from_service_account_file("scraping-wikipedia-d73328354ba9.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
    service = build("sheets", "v4", credentials=credentials)

    spreadsheet_id = "<your-Google-Sheet-id>"  # Replace with your Google Sheets spreadsheet ID
    sheet_name = "<your-Google-Sheet-name>"  # Replace with your sheet name

    values = []
    for word, count in sorted_word_count:
        values.append([word, count])

    body = {"values": values}
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    print(f"{result['updatedCells']} cells updated.")

# Main function
def main():
    article_text = scrape_wikipedia()
    word_count = count_words(article_text)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    insert_into_sheets(sorted_word_count)

if __name__ == "__main__":
    main()
