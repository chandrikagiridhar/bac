Display status of tables with realtime spreadsheet changes using Google Spreadsheets API.

status.html --> Table to display spreadsheet results. Refreshes every 10 seconds so it can pick up changes from the spreadsheet realtime

Note included : urls.py -->need entry for mapping the view.

urlpatterns = [
    path('', views.status, name='status'),
]

Also the status.html was in a templates folder.  Might need to configure location based on making sure settings.py has correct template path configured.

For deployment: Also needed is the  ~/.credentials/sheets.googleapis.com-python-quickstart.json file that I get using a local one time run to authenticate for access to the spreadsheet.