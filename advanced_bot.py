import schedule
import telegram
from telegram.ext import Application, CommandHandler
import asyncio
from matka_predictor import KalyanMatkaPredictor
import time
from datetime import datetime

class AdvancedMatkaBot:
    def __init__(self, telegram_token=None):
        self.predictor = KalyanMatkaPredictor()
        self.telegram_token = telegram_token
        
    async def send_telegram_alert(self, message):
        """Send prediction via Telegram"""
        if self.telegram_token:
            bot = telegram.Bot(token=self.telegram_token)
            # Add your chat_id here
            chat_id = "YOUR_CHAT_ID"  # Replace with actual chat ID
            await bot.send_message(chat_id=chat_id, text=message)
    
    def schedule_predictions(self):
        """Schedule daily predictions"""
        print("[INFO] Scheduling daily predictions...")
        schedule.every().day.at("09:00").do(self.daily_prediction_job)
        schedule.every().day.at("21:00").do(self.daily_prediction_job)
        
        print("[INFO] Bot is running. Predictions scheduled for 9:00 AM and 9:00 PM daily.")
        print("Press Ctrl+C to stop the bot.")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n[STOP] Bot stopped by user.")
    
    def daily_prediction_job(self):
        """Automated daily prediction job"""
        print(f"[INFO] Running scheduled prediction at {datetime.now()}")
        
        try:
            self.predictor.scrape_historical_data()
            self.predictor.train_prediction_model()
            report = self.predictor.generate_daily_report()
            
            # Save to file
            filename = f'scheduled_prediction_{datetime.now().strftime("%Y%m%d_%H%M")}.txt'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            
            # Send via Telegram if token is configured
            if self.telegram_token:
                asyncio.run(self.send_telegram_alert(report))
                print("[INFO] Prediction sent via Telegram")
            
            print(f"[OK] Scheduled prediction completed and saved to {filename}")
            
        except Exception as e:
            print(f"[ERROR] Error during scheduled prediction: {e}")

def main():
    print("[START] Starting Advanced Matka Bot...")
    print("[WARNING] This is for educational purposes only!")
    print("[WARNING] Gambling activities may be illegal in your jurisdiction!")
    
    # Initialize bot
    # To use Telegram integration, replace None with your Telegram bot token
    telegram_token = None  # Replace with "YOUR_BOT_TOKEN" if you have one
    
    bot = AdvancedMatkaBot(telegram_token=telegram_token)
    
    # Start scheduling
    bot.schedule_predictions()

if __name__ == "__main__":
    main()
