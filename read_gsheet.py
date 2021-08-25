import pandas as pd 

def read_gsheet(sheet_id: str = None, sheet_name:str = None) -> pd.DataFrame:
	
	"""
	input:
		sheet_id (str): the id given by google to identify the spreadsheet.
		sheet_name (str): the name of a specific sheet in case of multiple sheets in the spreadsheet.
	
	output:
		Dataframe with all the workouts given by the spreadsheet.

	"""

	if sheet_id == None:
		sheet_id = "1Yb1qliHhS2IcTq_60iRVr6zb7Glt85TEtzLPfOKaFQA"
	if sheet_name == None:
		sheet_name = 'neue_Workouts'		
	
	url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
	
	return pd.read_csv(url).dropna(axis = 1, how = "all")
