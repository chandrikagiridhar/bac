from __future__ import print_function
from django.shortcuts import render

from django.template import Template, Context

from django.http import HttpResponse
from django.http import HttpResponseRedirect

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# If modifying these scopes, delete your previously saved credentials                                                                                                                                                                              
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json                                                                                                                                                                                   
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage
    If nothing has been stored, or if the stored credentials are invalid,                                                                                                                                                                          
    the OAuth2 flow is completed to obtain the new credentials.                                                                                                                                                                                                                                                                                                                                                                                                                                     
    Returns:                                                                                                                                                                                                                                  
        Credentials, the obtained credential.                                                                                                                                                                                                      
    """
    # TODO (chandrika): Change to correct /var/www path in server.
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    return (credentials);
 

def status(request):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url)

    # This is the Google spreadsheet which has the data.
    # spreadsheet_id = '1kJKLHsX8oClQVnAdEcJmt2H4KstvPtXC1E7qfFZIHvg'
    spreadsheet_id = '1c01LKRoA2hDCs7vUoYPPi6rW7Nvarp_y68OcpgVaGH0'
    # Note anytime a new tab is used for a tournament, change tabName
    tab_name = '1'
    range_name = '%s!A2:B' % (tab_name)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        return HttpResponse('No data found. Some issue- we are working on it!')
    status = []
    for row in values:
        if len(row) < 2:
            continue;
        status.append((row[0], row[1]))
    return render(request, 'status.html', {'status': status}) 
