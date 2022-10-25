from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import pickle


def trainModel():
    df_ipl = pd.read_csv("data/IPL_Win_Pred.csv")
    X_train = df_ipl.drop("WinningTeam", axis=1)
    y_train = df_ipl["WinningTeam"]

    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)

    pickle.dump(model, open("data/mymodel.pkl", "wb"))
