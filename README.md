# CreditScoreClassification

A machine learning-based application to predict the credit score category of individuals based on various financial and personal factors. This project utilizes a CatBoost classification model to provide accurate predictions based on input data.

## Description

This project allows users to input key financial details such as annual income, loan types, and payment history to predict their credit score. It uses a pre-trained CatBoost model pipeline to predict the user's credit score category, which helps individuals better understand their creditworthiness.

### Features:
- **User Input Interface**: Input financial data through an intuitive interface powered by Streamlit.
- **Prediction Output**: Displays the probability distribution of credit score categories.
- **CatBoost Model**: A robust classification model used to predict the credit score category.

### Differentiating Factors:
- **Customizable Model**: The model can be retrained with new data for improved accuracy.
- **Interactive UI**: The Streamlit UI is designed to be user-friendly for anyone without technical expertise.

## Badges

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Installation

To set up the `CreditScoreClassification` project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/CreditScoreClassification.git
    cd CreditScoreClassification
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

### Input
Provide the following data through the Streamlit interface:
- **Financial Information**: Income, loans, payment history, etc.
- **Personal Information**: Age, occupation, etc.
- **Loan Types**: Select the loan type(s) you have.

### Output
The app will display:
- **Credit Score Prediction**: The most likely credit score category.
- **Prediction Probabilities**: The probability distribution for each credit score category.

### Example Input:
- **Annual Income**: 50,000 USD
- **Occupation**: Developer
- **Loan Types**: Personal Loan, Auto Loan

### Example Output:
- **Predicted Credit Score**: Good
- **Prediction Probabilities**:
    - **Good**: 78%
    - **Fair**: 15%
    - **Poor**: 7%

## Support

If you encounter any issues, feel free to reach out via the following:
- [Create an issue on GitHub](https://github.com/your-username/CreditScoreClassification/issues)

## Roadmap

- **Future Releases**:
    - Implement the ability to retrain the model with new data.
    - Enhance user interface with more detailed financial input categories.
    - Add model interpretability features (e.g., SHAP values).

## Contributing

Contributions are welcome! If you would like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Open a pull request.

Please ensure that your contributions do not break any existing functionality and that all tests pass.

## Authors and Acknowledgments

- **Shushan Gevorgyan** - Creator and Lead Developer
- **CatBoost** - Model implementation and algorithm
- **Streamlit** - Interactive app interface



## Project Status

This project is actively maintained and open for contributions. Feel free to submit issues or pull requests for improvements.
