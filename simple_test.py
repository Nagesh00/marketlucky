import sys
import os
print("Current directory:", os.getcwd())
print("Python path:", sys.executable)
print("Python version:", sys.version)

# Test import
try:
    import pandas as pd
    import numpy as np
    import sklearn
    print("All imports successful!")
    
    # Test creating the predictor
    import matka_predictor
    print("matka_predictor module imported successfully")
    
    # Test creating instance
    predictor = matka_predictor.KalyanMatkaPredictor()
    print("KalyanMatkaPredictor created successfully")
    
    # Test basic functionality
    print("Testing data generation...")
    data = predictor.scrape_historical_data(days=5)
    print(f"Data shape: {data.shape}")
    
    print("Testing model training...")
    predictor.train_prediction_model()
    
    print("Testing prediction...")
    prediction = predictor.generate_prediction()
    print("Prediction generated:", prediction['ml_prediction'])
    
    print("SUCCESS: All tests passed!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
