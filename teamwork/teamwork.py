import requests
import json


class Teamwork(object):
    """
    Basic wrapper to work with the Teamwork API
    """
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key
        self.account = self.authenticate()
        self.user = User(self.account.get('userId'))

    def get(self, path=None, params=None, data=None):
        url = self.get_base_url()
        if path:
            url = "%s/%s" % (url, path)
        payload = {}
        if params:
            payload = params

        request = requests.get(
            url, auth=(self.api_key, ''), params=payload)

        if request.json().get('STATUS') == 'OK':
            return request.json()
        else:
            raise RuntimeError("Not Valid request")

    def post(self, path=None, data=None):
        url = self.get_base_url()
        if path:
            url = "%s/%s" % (url, path)

        request = requests.post(
            url, auth=(self.api_key, ''), data=data)
        if request.status_code != 201:
            raise RuntimeError("Not Valid request")
        return request.text

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

    def save_project_time_entry(self, project_id, entry_date, duration,
                                user_id, description, start_time):
        """
        project_id: Project ID
        date: datetime.date Date of time entry
        duration: datetime.timedelta Duration
        user_id: Integer Id of person
        description: String Id of person
        start_time: datetime.timedelta
        """
        duration_hours, duration_minutes = timedelta_to_hours_minutes(duration)

        data = {
                    "time-entry": {
                        "description": description,
                        "person-id": user_id,
                        "date": entry_date.strftime('%Y%m%d'),
                        "time": time_to_hhmm(start_time),
                        "hours": duration_hours,
                        "minutes": duration_minutes,
                        "isbillable": "1"
                    }
                }
        result = self.post(
            '/projects/%i/time_entries.json' % project_id,
            data=json.dumps(data))
        return result

    def get_time_entry(self, time_id):
        result = self.get('time_entries/%i.json' % time_id)
        return result.get('time-entry')

    def update_time_entry(self):
        pass

    def delete_time_entry(self):
        pass

    def update_project_time(self, project_id, data):
        pass

    def get_project_user_times(self, project_id, user_id):
        pass


def timedelta_to_hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


def time_to_hhmm(time_input):
    return '%i:%i' % (time_input.hour, time_input.minute)


class User(object):
    def __init__(self, id):
        self.id = id
