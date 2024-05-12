import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm

def ask_user_for_statistical_analysis():
    # Input data from the user
    file_path = input("Enter the path to your CSV file: ")
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Failed to read the file: {e}")
        return

    # Display first few rows of the data
    print("\nFirst 5 rows of your data:")
    print(data.head())

    # Asking the user what analysis to perform
    while True:
        print("\nAvailable statistical analyses:")
        print("1: Descriptive Statistics")
        print("2: Correlation Matrix")
        print("3: Simple Linear Regression")
        print("4: Hypothesis Testing (T-Test for two independent samples)")
        print("5: Exit")
        choice = input("Select an analysis to perform (1-5): ")

        if choice == '1':
            # Descriptive Statistics
            print("\nDescriptive Statistics:")
            print(data.describe())
            print("\nModes:\n", data.mode().iloc[0])
        elif choice == '2':
            # Correlation Matrix
            print("\nCorrelation Matrix:")
            print(data.corr())
        elif choice == '3':
            # Simple Linear Regression
            if data.shape[1] < 2:
                print("Not enough columns for linear regression.")
            else:
                x_column = input("Enter the column name for the independent variable: ")
                y_column = input("Enter the column name for the dependent variable: ")
                if x_column not in data.columns or y_column not in data.columns:
                    print("Invalid column names entered.")
                else:
                    X = data[[x_column]]
                    Y = data[y_column]
                    X = sm.add_constant(X)  # Adds a constant term to the predictor
                    model = sm.OLS(Y, X)
                    results = model.fit()
                    print("\nLinear Regression Results:")
                    print(results.summary())
        elif choice == '4':
            # Hypothesis Testing
            if data.shape[1] < 1:
                print("Not enough data for hypothesis testing.")
            else:
                column1 = input("Enter the first column name for the t-test: ")
                column2 = input("Enter the second column name for the t-test: ")
                if column1 not in data.columns or column2 not in data.columns:
                    print("Invalid column names entered.")
                else:
                    t_stat, p_value = stats.ttest_ind(data[column1].dropna(), data[column2].dropna(), equal_var=False)
                    print(f"\nT-test results:\nT-statistic = {t_stat}, P-value = {p_value}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Example of how to run the function
ask_user_for_statistical_analysis()

