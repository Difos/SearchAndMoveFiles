import os
import pandas as pd
import shutil
import datetime



def main():

    dfIncomplete = pd.read_csv("C:\Dados\Analise\incomplete_exports.csv")
    dfAllResults = pd.read_csv(r"C:\Dados\Analise\all_results_no_probability.csv")
    dfwrongPaterns = pd.read_csv("C:\Dados\Analise\wrong_pattern_csvs.csv")

    dfIncomplete["mdp_name"] = dfIncomplete["mdp_name"]+".mdp"
    dfAllResults["mdp_name"] = dfAllResults["mdp_name"]+".mdp"
    dfwrongPaterns["mdp_name"] = dfwrongPaterns["mdp_name"]+".mdp"



    dfAll = pd.concat([dfIncomplete["mdp_name"],dfAllResults["mdp_name"],dfwrongPaterns["mdp_name"]],axis=0)

    print(dfAll.value_counts().sum)

    filematch =""
    filetarget = ""

    print(dfAll.head())

    for p in dfAll:
        start = datetime.datetime.now()
        filematch = os.path.join(r"F:\INP. ULTRASSOM", p)
        filetarget = os.path.join(r"C:\Dados\Ultras",p)
        if(os.path.exists(filematch)):
            shutil.copyfile(filematch,filetarget)
            end = datetime.datetime.now()
            totaltime = (start - end).total_seconds()
            print(f"Copiado --> {filetarget} total tempo ->{totaltime}")