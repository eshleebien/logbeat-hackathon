from pivotalclient import PivotalClient

# from config import PIVOTAL_PROJECT_ID, PIVOTAL_API_KEY
PIVOTAL_PROJECT_ID = '2086981'
PIVOTAL_API_KEY = '3a84ad0dbf10e6ca7520334371cc5fdc'


def add_story(data, story_type='bug'):

    pivotal = PivotalClient(PIVOTAL_API_KEY, project_id=PIVOTAL_PROJECT_ID)

    labels = ['bug', ]
    labels.append('add-new-label-here')

    requester_id = _lookup_id_by_email('paolo.barazon@gengo.com')

    story_dict = {
        'project_id': PIVOTAL_PROJECT_ID,
        'name': data['name'],
        'description': data['description'],
        'story_type': story_type,
        'current_state': 'unstarted', # MUST always be 'unstarted'
        'labels': labels,
        'requested_by_id': requester_id,
    }
    new_story = pivotal.create_story(story_dict)

    # print "This story's ID number is:", new_story.id
    return new_story['id']


def _lookup_id_by_email(email_address):
    pivotal = PivotalClient(PIVOTAL_API_KEY, project_id=PIVOTAL_PROJECT_ID)
    for user_data in pivotal.get_project_memberships():
        this_person = user_data['person']
        if this_person['email']==email_address:
            return this_person['id']
    return -1


if __name__=='__main__':
    # pivotal = PivotalClient(PIVOTAL_API_KEY, project_id=PIVOTAL_PROJECT_ID)
    # for user in pivotal.get_project_memberships():
    #   print user
    # requester_id = _lookup_id_by_email('paolo.barazon@gengo.com')
    # print requester_id
    pass
