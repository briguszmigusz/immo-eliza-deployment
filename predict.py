import pandas as pd
import joblib

# Loading models
model = joblib.load("models/best_model.pkl")
encoders = joblib.load("models/encoders.pkl")
medians = joblib.load("models/medians.pkl")
modes = joblib.load("models/modes.pkl")
scaler = joblib.load("models/scaler.pkl")

# Cleaning function
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes the columns that we decided to drop during training
    """
    drop_cols = ["Kitchen type", "Surface garden", "Number of showers", "Attic",
        "Number of garages", "Swimming pool", "Kitchen equipment",
        "url", "Property ID", "price_per_sqm", "Price_per_sqm_land",
        "Availability", "Total land surface", "Garage",
        "Type of glazing", "Surface terrace", "Furnished"]

    for col in drop_cols:
        if col in df.columns:
            df = df.drop(col, axis=1)

    return df

# Preprocessing function
def preprocess_new_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    - drop location columns
    - fill missing values using medians/modes learned from training
    - apply label encoding using saved encoders
    """
    # Dropping geographical columns
    for col in ["city", "province", "Region"]:
        if col in df.columns:
            df = df.drop(col, axis=1)

    # Filling numeric missing values with training medians
    for col, med in medians.items():
        if col in df.columns:
            df[col] = df[col].fillna(med)

    # Filling categorical missing values with training modes
    for col, mode in modes.items():
        if col in df.columns:
            df[col] = df[col].fillna(mode)

    # Applying label encoders to categorical columns
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col])

    # Apply scaling only if model used a scaler (linear regression)
    if scaler is not None:
        numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
        df[numeric_cols] = scaler.transform(df[numeric_cols])

    return df

# Predict function
def predict_price(data: dict) -> float:
    """
    Main prediction function called by Streamlit.
    Accepts a dictionary with property information.
    1. Convert dict → DataFrame
    2. Clean data (drop unused columns)
    3. Preprocess (encoding, imputing, optional scaling)
    4. Predict with trained model
    5. Return float price
    """
    # Convert to DataFrame
    df = pd.DataFrame([data])
    # Clean and preprocess
    df = clean_data(df)
    df_ready = preprocess_new_data(df)
    # Predict
    prediction = model.predict(df_ready)

    return float(prediction[0])
