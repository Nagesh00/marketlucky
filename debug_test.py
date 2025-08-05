import sys
print("Python version:", sys.version)

try:
    import pandas as pd
    print("[OK] pandas imported successfully")
    print("pandas version:", pd.__version__)
except ImportError as e:
    print("[ERROR] pandas import failed:", e)

try:
    import numpy as np
    print("[OK] numpy imported successfully")
    print("numpy version:", np.__version__)
except ImportError as e:
    print("[ERROR] numpy import failed:", e)

try:
    import sklearn
    print("[OK] sklearn imported successfully")
    print("sklearn version:", sklearn.__version__)
except ImportError as e:
    print("[ERROR] sklearn import failed:", e)

try:
    from matka_predictor import KalyanMatkaPredictor
    print("[OK] KalyanMatkaPredictor imported successfully")
    
    # Test basic functionality
    predictor = KalyanMatkaPredictor()
    print("[OK] Predictor initialized")
    
    # Test data generation
    data = predictor.scrape_historical_data(days=10)
    print(f"[OK] Generated {len(data)} days of test data")
    
    # Test model training
    predictor.train_prediction_model()
    print("[OK] Model trained successfully")
    
    # Test prediction
    prediction = predictor.generate_prediction()
    print("[OK] Prediction generated successfully")
    print("Sample prediction:", prediction['ml_prediction'])
    
except Exception as e:
    print("[ERROR] Error in matka_predictor:", e)
    import traceback
    traceback.print_exc()

print("[DEBUG] Debug test completed!")
