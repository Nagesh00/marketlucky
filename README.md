# MarketLucky

This repository contains both a [Next.js](https://nextjs.org) web application and a Python-based Kalyan Matka prediction system for educational purposes.

⚠️ **IMPORTANT DISCLAIMER**: The matka prediction system is for educational and research purposes only. Gambling activities may be illegal in your jurisdiction and carry significant risks.

## Project Components

### 1. Next.js Web Application

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

#### Getting Started with Web App

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

### 2. Kalyan Matka Prediction System

A Python-based educational system that demonstrates statistical analysis and machine learning techniques applied to pattern recognition.

#### Features
- Historical data analysis and pattern recognition
- Machine learning-based predictions using RandomForest
- Hot/Cold number analysis and frequency tracking
- Automated daily predictions with scheduling
- Telegram bot integration for notifications
- Data export to CSV and JSON formats

#### Quick Start with Matka Predictor

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the basic predictor**:
   ```bash
   python matka_predictor.py
   # Or double-click: run_predictor.bat (Windows)
   ```

3. **Run data analysis utilities**:
   ```bash
   python data_utils.py
   # Or double-click: run_data_utils.bat (Windows)
   ```

4. **Run the advanced bot with scheduling**:
   ```bash
   python advanced_bot.py
   # Or double-click: run_advanced_bot.bat (Windows)
   ```

#### Python Dependencies
- pandas, numpy, scikit-learn
- requests, beautifulsoup4
- schedule, python-telegram-bot

See `requirements.txt` for complete list and `MATKA_README.md` for detailed documentation.

#### Output Files
The system generates various output files:
- `kalyan_prediction_YYYYMMDD.txt` - Daily prediction reports
- `analysis_report_YYYYMMDD.json` - Statistical analysis
- `matka_data_YYYYMMDD.csv` - Historical data exports

## Web Application Documentation

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
