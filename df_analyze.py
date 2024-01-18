import pandas as pd
import text_format


class DFAnalyze:
    def __init__(self, df):
        self.df = df
        self.text_format = text_format.TextFormat
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

    def analyze(self):
        # Print the first few rows of the DataFrame
        print(f"\n{self.text_format.BOLD}First Few Rows:{self.text_format.RESET}\n")
        print(self.df.head())

        # Print the last few rows of the DataFrame
        print(f"\n{self.text_format.BOLD}Last Few Rows:{self.text_format.RESET}\n")
        print(self.df.tail())

        # Print the shape of our data
        print(f"\n{self.text_format.BOLD}Number of rows:{self.text_format.RESET}\n")
        print(self.df.shape[0])
        print(f"\n{self.text_format.BOLD}Number of columns:{self.text_format.RESET}\n")
        print(self.df.shape[1])

        # Print basic information about the DataFrame
        print(f"\n{self.text_format.BOLD}DataFrame Info:{self.text_format.RESET}\n")
        print(self.df.info())

        # Print unique values of 4 columns of object datatype (String)
        print(f"\n{self.text_format.BOLD}Unique brand values:{self.text_format.RESET}\n")
        print(self.df.brand.unique())
        print(f"\n{self.text_format.BOLD}Unique model values:{self.text_format.RESET}\n")
        print(self.df.model.unique())
        print(f"\n{self.text_format.BOLD}Unique transmission values:{self.text_format.RESET}\n")
        print(self.df.transmission.unique())
        print(f"\n{self.text_format.BOLD}Unique fuelType values:{self.text_format.RESET}\n")
        print(self.df.fuelType.unique())

        # Print summary statistics
        print(f"\n{self.text_format.BOLD}Summary Statistics:{self.text_format.RESET}\n")
        print(self.df.describe())

        # Print the number of missing values in each column
        print(f"\n{self.text_format.BOLD}Missing Values:{self.text_format.RESET}\n")
        print(self.df.isnull().sum())

        # Print the number of duplicate values in DataFrame
        print(f"\n{self.text_format.BOLD}Duplicated Values:{self.text_format.RESET}\n")
        print(self.df.duplicated().sum())

        # Print string columns of the DataFrame
        print(f"\n{self.text_format.BOLD}String columns of the DataFrame:{self.text_format.RESET}\n")
        print(self.df.select_dtypes(include=['object']).head())

        # Print integer columns of the DataFrame
        print(f"\n{self.text_format.BOLD}Integer columns of the DataFrame:{self.text_format.RESET}\n")
        print(self.df.select_dtypes(include=['number']).head())
