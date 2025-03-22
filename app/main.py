from utils.absenteeism_generator import generate_absenteeism_data
from ETL.extract import extract_excel
import os

def generate_excel_files(files: int = 10):
    """
    Function generate and save excel files.

    Args:
        files (int): The number of files to generate.
    """
    if os.path.isdir("./data/input") == False:
        os.makedirs("./data/input")

    for file in range(files):
        df = generate_absenteeism_data()
        output_path = os.path.join("data/input", f"absenteeism_data_{file}.xlsx")
        df.to_excel(output_path, index=False)

if __name__ == "__main__":
    generate_excel_files()
    list_df = extract_excel("data/input")