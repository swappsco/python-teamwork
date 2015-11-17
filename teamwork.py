import requests


class Teamwork(object):
    """
    Basic wrapper to work with the Teamwork API
    """
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key

    def request(self, path=None, data=None):
        url = self.get_base_url()
        if path:
            url = "%s/%s" % (url, path)

        request = requests.get(url, auth=(self.api_key, ''))
        if request.json().get('STATUS') == 'OK':
            return request.json()
        else:
            raise RuntimeError("Not Valid request")

    def get_base_url(self):
        return 'https://%s' % self.domain

    def get_projects(self):
        result = self.request('projects.json')
        return result.get('projects')

    def get_project_times(self, project_id):
        result = self.request("/projects/%i/time_entries.json" % project_id)
        return result.get('time-entries')

    def save_project_time(self, project_id, data):
        pass

    def update_project_time(self, project_id, data):
        pass

    def get_project_user_times(self, project_id, user_id):
        pass
