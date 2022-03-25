import pandas as pd
import glob



def find_row_by_index(df : pd.DataFrame, date : str,) -> pd.DataFrame:
    """
    Função para encontrar uma linha de um dataframe a partir de um index
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe a ser pesquisado
    date : str
        Index a ser pesquisado
    Returns
    -------
    pd.DataFrame
        Dataframe com a linha pesquisada
    """
    return df.filter(items=[date], axis=0)