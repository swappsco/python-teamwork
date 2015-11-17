===============
python-teamwork
===============
Python Wrapper for Teamwork API

API Reference: http://developer.teamwork.com/

To use, simply do::

    >>> import teamwork
    >>> instance = teamork.Teamwork('company.teamwork.com', 'API_KEY')
    >>> instance.get_projects()

***************
Installation
***************

Using pip:
    >>> pip install python-teamwork

Using the source code:
    >>> python setup.py install

******************
Available methods
******************

Methods implementation in progress. This is the list of the available ones:

instance.get_projects()
-----------------------

Returns all the projects of the account.
http://developer.teamwork.com/projectsapi#retrieve_all_proj

instance.get_project_times(project_id)
--------------------------------------
Returns the times for a specific project.
Available parameters for filtering:

- user_id: User id
- start_date: Start date
- end_date: End Date

instance.save_project_time_entry(project_id, entry_date, duration, user_id, description, start_time)
------------------------------------------------------------------------------------------------------------
Create time entry for specified project.

- project_id: Project ID
- date: datetime.date Date of time entry
- duration: datetime.timedelta Duration
- user_id: Integer Id of person
- description: String Id of person
- start_time: datetime.timedelta