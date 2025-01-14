"""Example service - CSV parser
Should contain class or methods that will:
- Load CSV from path to dataframe
- converd df columns to lowercase matching names of desired schema (lower plant)
- return dict

Example pseudocode:

def parse_csv(path:str) -> dict:
    df = pandas.DataFrame.from_csv(path)
    df.columns = [column.lower() for column in df.columns]
    return df.to_dict()  # maybe it should be list of dicts -> this is pseudo code ;)
"""