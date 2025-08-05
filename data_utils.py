import json
import csv
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from matka_predictor import KalyanMatkaPredictor

class DataManager:
    def __init__(self):
        self.predictor = KalyanMatkaPredictor()
    
    def export_to_csv(self, data, filename=None):
        """Export data to CSV format"""
        if filename is None:
            filename = f"matka_data_{datetime.now().strftime('%Y%m%d')}.csv"
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"[OK] Data exported to {filename}")
        return filename
    
    def export_predictions_to_json(self, predictions, filename=None):
        """Export predictions to JSON format"""
        if filename is None:
            filename = f"predictions_{datetime.now().strftime('%Y%m%d')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(predictions, f, indent=2, default=str)
        
        print(f"[OK] Predictions exported to {filename}")
        return filename
    
    def generate_analysis_report(self):
        """Generate comprehensive analysis report"""
        self.predictor.scrape_historical_data(days=180)
        analysis = self.predictor.analyze_patterns()
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'data_period': '180 days',
            'total_records': len(self.predictor.data),
            'most_frequent_jodis': analysis['most_frequent_jodis'].to_dict(),
            'day_wise_patterns': analysis['day_wise_patterns'].to_dict(),
            'monthly_patterns': analysis['monthly_patterns'].to_dict(),
            'statistics': {
                'jodi_mean': float(self.predictor.data['jodi'].mean()),
                'jodi_std': float(self.predictor.data['jodi'].std()),
                'open_pana_mean': float(self.predictor.data['open_pana'].mean()),
                'close_pana_mean': float(self.predictor.data['close_pana'].mean())
            }
        }
        
        # Save report
        filename = f"analysis_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"[INFO] Analysis report saved to {filename}")
        return report

class WebScraper:
    """
    Template for web scraping functionality
    Note: This is a template - actual implementation would need
    to comply with website terms of service and robots.txt
    """
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_website_template(self, url):
        """
        Template function for scraping matka websites
        WARNING: Always check robots.txt and terms of service
        """
        print("[WARNING] This is a template function for educational purposes")
        print("[WARNING] Actual web scraping must comply with website terms")
        
        # Template implementation
        # In real implementation, you would:
        # 1. Check robots.txt
        # 2. Respect rate limits
        # 3. Handle errors gracefully
        # 4. Parse HTML properly
        
        return []

class NumberAnalyzer:
    def __init__(self):
        pass
    
    def calculate_number_frequency(self, data, number_type='jodi'):
        """Calculate frequency distribution of numbers"""
        if number_type == 'jodi':
            freq = data['jodi'].value_counts()
        elif number_type == 'open_pana':
            freq = data['open_pana'].value_counts()
        elif number_type == 'close_pana':
            freq = data['close_pana'].value_counts()
        else:
            return {}
        
        return freq.to_dict()
    
    def find_patterns(self, data):
        """Find various patterns in the data"""
        patterns = {}
        
        # Consecutive number patterns
        patterns['consecutive_jodis'] = self.find_consecutive_patterns(data['jodi'])
        
        # Sum digit patterns
        patterns['sum_patterns'] = self.analyze_sum_patterns(data['jodi'])
        
        # Even/Odd patterns
        patterns['even_odd'] = self.analyze_even_odd_patterns(data['jodi'])
        
        return patterns
    
    def find_consecutive_patterns(self, numbers):
        """Find consecutive number patterns"""
        consecutive = []
        for i in range(len(numbers) - 1):
            if abs(numbers.iloc[i] - numbers.iloc[i + 1]) == 1:
                consecutive.append((numbers.iloc[i], numbers.iloc[i + 1]))
        
        return consecutive[:10]  # Return top 10
    
    def analyze_sum_patterns(self, numbers):
        """Analyze digit sum patterns"""
        sums = []
        for num in numbers:
            digit_sum = sum(int(digit) for digit in str(num))
            sums.append(digit_sum)
        
        sum_freq = pd.Series(sums).value_counts()
        return sum_freq.head(10).to_dict()
    
    def analyze_even_odd_patterns(self, numbers):
        """Analyze even/odd number patterns"""
        even_count = sum(1 for num in numbers if num % 2 == 0)
        odd_count = len(numbers) - even_count
        
        return {
            'even_count': even_count,
            'odd_count': odd_count,
            'even_percentage': (even_count / len(numbers)) * 100,
            'odd_percentage': (odd_count / len(numbers)) * 100
        }

def main():
    print("[INFO] Running Data Management and Analysis Tools...")
    
    # Initialize components
    data_manager = DataManager()
    analyzer = NumberAnalyzer()
    
    # Generate and export analysis
    print("[INFO] Generating analysis report...")
    report = data_manager.generate_analysis_report()
    
    # Analyze patterns
    print("[INFO] Analyzing number patterns...")
    patterns = analyzer.find_patterns(data_manager.predictor.data)
    
    # Export data
    print("[INFO] Exporting data...")
    data_manager.export_to_csv(data_manager.predictor.data)
    
    # Generate comprehensive report
    comprehensive_report = {
        'analysis': report,
        'patterns': patterns,
        'export_timestamp': datetime.now().isoformat()
    }
    
    filename = f"comprehensive_report_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(comprehensive_report, f, indent=2, default=str)
    
    print(f"[OK] Comprehensive report saved to {filename}")
    print("[COMPLETE] Data management and analysis complete!")

if __name__ == "__main__":
    main()
