"""
Research tools for PDF processing and statistical analysis.
These are the actual functions that do the work.
"""

import PyPDF2
from pathlib import Path
from typing import Dict, List
import json


def extract_pdf_text(filepath: str) -> str:
    """
    Extracts all text from a PDF file.
    
    Args:
        filepath: Path to the PDF file (e.g., "papers/smith-2024.pdf")
    
    Returns:
        String containing all text from the PDF
    
    Example:
        text = extract_pdf_text("papers/research-paper.pdf")
        print(text[:200])  # Print first 200 characters
    """
    # Convert to Path object for better path handling
    pdf_path = Path(filepath)
    
    # Check if file exists
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {filepath}")
    
    # Open and read the PDF
    extracted_text = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Extract text from each page
        for page in pdf_reader.pages:
            extracted_text.append(page.extract_text())
    
    # Combine all pages into one string
    return "\n".join(extracted_text)


def calculate_correlation(experience_data: List[float], 
                         fatigue_data: List[float]) -> Dict:
    """
    Calculates correlation between experience and fatigue.
    
    Args:
        experience_data: List of experience values (years)
        fatigue_data: List of fatigue scores (matching order)
    
    Returns:
        Dictionary with correlation coefficient and p-value
    
    Example:
        experience = [5.2, 8.1, 3.4, 12.5, 6.7]
        fatigue = [3.1, 4.2, 2.8, 4.8, 3.5]
        result = calculate_correlation(experience, fatigue)
        print(f"Correlation: {result['r']}, p-value: {result['p']}")
    """
    import scipy.stats as stats
    import numpy as np
    
    # Convert to numpy arrays for calculation
    exp_array = np.array(experience_data)
    fat_array = np.array(fatigue_data)
    
    # Calculate Pearson correlation
    correlation, p_value = map(float, stats.pearsonr(exp_array, fat_array))
    
    # Calculate confidence interval
    n = len(exp_array)
    z = np.arctanh(correlation)  # Fisher z-transformation
    se = 1 / np.sqrt(n - 3)
    ci_lower = np.tanh(z - 1.96 * se)
    ci_upper = np.tanh(z + 1.96 * se)
    
    return {
        "r": round(correlation, 3),
        "p_value": round(p_value, 4),
        "n": n,
        "ci_95_lower": round(ci_lower, 3),
        "ci_95_upper": round(ci_upper, 3)
    }