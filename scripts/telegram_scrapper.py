from telethon.sync import TelegramClient
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='scripts/scraping_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Telegram API credentials
api_id = '1705947'
api_hash = 'dc0f2a2e3acbfcf7a46dcaa0d1108251'
phone_number = '+251936678553'

# Create a Telegram Client
client = TelegramClient('scraper_session4', api_id, api_hash)

# Function to scrape Telegram channel messages
def scrape_telegram_channel(channel_username, limit=100):
    logging.info(f'Starting scraping for {channel_username}')
    try:
        with client:
            # Join the channel and get messages
            messages = []
            for message in client.iter_messages(channel_username, limit=limit):
                if message.message:
                    messages.append([message.id, message.date, message.message])
            logging.info(f'Successfully scraped {len(messages)} messages from {channel_username}')
            return messages
    except Exception as e:
        logging.error(f'Error while scraping {channel_username}: {e}')
        return []

# Store scraped data in a DataFrame
def store_scraped_data(data, filename='data/scraped_data.csv'):
    df = pd.DataFrame(data, columns=['Message ID', 'Date', 'Message'])
    df.to_csv(filename, index=False)
    logging.info(f'Stored scraped data to {filename}')

# Main scraping function
def main():
    # List of Telegram channels to scrape
    channels = ['DoctorsET', 'lobelia4cosmetics', 'yetenaweg', 'EAHCI']
    
    for channel in channels:
        # Scrape data from each channel
        scraped_data = scrape_telegram_channel(channel, limit=500)  # Set limit to 500 messages
        if scraped_data:
            # Store data for each channel
            store_scraped_data(scraped_data, f'{channel}_data.csv')

# Run the scraper
if __name__ == "__main__":
    logging.info('Starting Telegram scraping script')
    main()
    logging.info('Finished Telegram scraping script')
