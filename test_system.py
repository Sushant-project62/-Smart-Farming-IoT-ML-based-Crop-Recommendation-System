#!/usr/bin/env python3
"""
Test script for the Crop Recommendation System
"""

import pickle
import pandas as pd
import numpy as np

def test_model_loading():
    """Test if the ML model can be loaded"""
    try:
        model = pickle.load(open("crop.pkl", "rb"))
        print(" ML model loaded successfully")
        return True
    except Exception as e:
        print(f" Error loading ML model: {e}")
        return False

def test_data_loading():
    """Test if the crop data can be loaded"""
    try:
        data = pd.read_csv("crop_recommendation.csv")
        print(f" Crop data loaded successfully: {len(data)} samples")
        print(f"   Columns: {list(data.columns)}")
        print(f"   Unique crops: {data['label'].nunique()}")
        return True
    except Exception as e:
        print(f" Error loading crop data: {e}")
        return False

def test_prediction():
    """Test if the model can make predictions"""
    try:
        model = pickle.load(open("crop.pkl", "rb"))
        
        # Test with sample data
        test_features = np.array([[90, 42, 43, 20.9, 82.0, 6.5, 202.9]])
        prediction = model.predict(test_features)[0]
        
        print(f" Model prediction successful: {prediction}")
        return True
    except Exception as e:
        print(f" Error making prediction: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Crop Recommendation System...\n")
    
    tests = [
        ("Model Loading", test_model_loading),
        ("Data Loading", test_data_loading),
        ("Prediction", test_prediction)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to run.")
        print("\nTo start the application:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run: python app.py")
        print("3. Open: http://localhost:5000")
    else:
        print("  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
