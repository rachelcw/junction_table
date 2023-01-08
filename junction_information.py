import pandas as pd
import numpy as np

def junction_informaion(junction, sample):
    """
    Args:
        junction (_type_): chr:start:end:cluster
        sample (_type_): sample of cll

    Returns:
        dataframe: the percent of the junction by the sample, avg, sf3b1- m/um
    """
    ptable=pd.read_csv("/home/ls/rachelcw/projects/LEAFCUTTER/lc_20221211/lc_20221221_perind.percent.csv",index_col=0)
    ptable.set_index('chrom',inplace=True)
    values=ptable.loc[[junction]].values
    sample_value=ptable.loc[junction,sample]
    avg=np.mean(values)
    cll_table=pd.read_csv("/home/ls/rachelcw/projects/LEAFCUTTER/cll_data.csv",index_col='key')
    sample_sf3b1=cll_table.loc[sample,'SF3B1_mut']
    result=pd.DataFrame({"junction":[junction],"sample":[sample],"sample_percent":[sample_value],"avg_junction":[avg],"SF3B1":[sample_sf3b1]})
    return result