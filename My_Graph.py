from datadog import initialize, api

options = {
    'api_key': '656e6a56f3d13ead5323057d1c301ce8',
    'app_key': '533cb4db4c8a9823ccb4350341674e2102b8462a'
}

initialize(**options)

title = "Parth_Parekh_Timeboard"
description = "An informative timeboard."

graphs = [{
    "definition": {
        "events": [],
        "requests": [
            {"q": "avg:my_metric{*} by {host}"}
        ],
        "viz": "timeseries"
    },
    "title": "my_metric"
},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "anomalies(avg:postgresql.bgwriter.write_time{*}.as_count(), 'basic', 2)"}
        ],
        "viz": "timeseries"
    },
    "title": "postgresql"
},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "avg:my_metric{*}.rollup(sum, 3600)"}
        ],
        "viz": "timeseries"
    },
    "title": "my_metric by hour"
}


]

api.Timeboard.create(title=title,
                     description=description,
                     graphs=graphs
                     )






