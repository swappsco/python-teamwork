import requests


class Teamwork(object):
    """
    Basic wrapper to work with the Teamwork API
    """
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key
        self.account = self.authenticate()
        self.user = User(self.account.get('userId'))

    def request(self, path=None, params=None, data=None, request_type='get'):
        url = self.get_base_url()
        if path:
            url = "%s/%s" % (url, path)
        payload = {}
        if params:
            payload = params
        if request_type == 'get':
            request = requests.get(
                url, auth=(self.api_key, ''), params=payload)
        if request_type == 'post':
            request = requests.post(
                url, auth=(self.api_key, ''), params=payload)

        if request.json().get('STATUS') == 'OK':
            return request.json()
        else:
            raise RuntimeError("Not Valid request")

    def get(self, path=None, params=None, data=None):
        return self.request(path, params, data, request_type='get')

    def post(self, path=None, params=None, data=None):
        return self.request(path, params, data, request_type='post')

    def get_base_url(self):
        return 'https://%s' % self.domain

    def authenticate(self):
        result = self.get('authenticate.json')
        return result.get('account')

    def get_projects(self):
        result = self.get('projects.json')
        return result.get('projects')

    def get_project_times(self, project_id, user_id=None, start_date=None,
                          end_date=None):
        """
        Get project time entries
        user_id: User id
        start_date: Start date
        end_date: End Date
        """
        payload = {}
        if start_date:
            payload['fromdate'] = start_date
        if end_date:
            payload['todate'] = end_date
        if user_id:
            payload['userId'] = user_id

        result = self.get("/projects/%i/time_entries.json" % project_id,
                          params=payload)
        return result.get('time-entries')

    def save_project_time(self, project_id, data):
        pass

    def update_project_time(self, project_id, data):
        pass

    def get_project_user_times(self, project_id, user_id):
        pass


class User(object):
    def __init__(self, id):
        self.id = id
