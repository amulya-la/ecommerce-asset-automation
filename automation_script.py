"""
Automated E-Commerce Asset Processing & Dimensional Scaling Engine
Author: Stacy
Description: Processes raw scraped web data, standardizes naming protocols, 
             and programmatically calculates catalog asset layout shapes 
             using Regular Expression patterns.
"""

import os
import re
import pandas as pd

def process_asset_pipeline(input_csv_path, output_excel_path):
    # 1. Verification of the raw source file path
    if not os.path.exists(input_csv_path):
        raise FileNotFoundError(f"Source file '{input_csv_path}' could not be located in the current workspace.")
    
    print(f"🔄 Ingesting data stream from: {input_csv_path}")
    df_raw = pd.read_csv(input_csv_path)
    
    final_dataset = []
    
    # 2. Iterating through rows to execute extraction loops
    for index, row in df_raw.iterrows():
        # Fallback to standard indexing if listing name column is corrupt/missing
        raw_name = row['s_wnSvX'] if 's_wnSvX' in df_raw.columns and pd.notna(row['s_wnSvX']) else f"Asset {index + 1}"
        img_url = str(row['QHl0ZB src']) if 'QHl0ZB src' in df_raw.columns else ""
        
        # 3. Utilizing Regular Expressions to parse display container dimension text
        width_match = re.search(r'w_(\d+)', img_url)
        height_match = re.search(r'h_(\d+)', img_url)
        
        # Safe default layout fallback
        calculated_position = "Top to Bottom" 
        
        # 4. Applying algorithmic conditional rules to determine aspect layout
        if width_match and height_match:
            width_val = int(width_match.group(1))
            height_val = int(height_match.group(1))
            
            if width_val > height_val:
                calculated_position = "Left to right"
            elif width_val == height_val:
                calculated_position = "Square / Uniform"
                
        # 5. Compiling structured tracking records (Intentionally isolating unverified data)
        final_dataset.append({
            "Present Name": raw_name,
            "Position": calculated_position
        })
        
    # 6. Compiling matrix out to clean native Excel format
    df_output = pd.DataFrame(final_dataset)
    df_output.to_excel(output_excel_path, index=False)
    print(f"🎉 Pipeline Execution Complete! Clean dataset generated at: {output_excel_path}")

if __name__ == "__main__":
    # Configure local workspace file hooks
    INPUT_SOURCE = "coincurrencystamp (1).csv"
    OUTPUT_TARGET = "Cleaned_Stamp_Layout.xlsx"
    
    # Run pipeline engine
    try:
        process_asset_pipeline(INPUT_SOURCE, OUTPUT_TARGET)
    except Exception as e:
        print(f"❌ Critical Pipeline Failure: {str(e)}")
