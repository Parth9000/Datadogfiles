from datadog import initialize, api


import pandas as pd
price_df=pd.read_csv("C:/Stevens/datadog/AMZN.csv")


options = {
    'api_key': '656e6a56f3d13ead5323057d1c301ce8',
    'app_key': '533cb4db4c8a9823ccb4350341674e2102b8462a'
}

initialize(**options)



title = "The Stock Price of Amazon"
description = "An informative timeboard."

price = price_df['Close'][1]
price= str(price) 



api.Event.create(title=title, text=price)






