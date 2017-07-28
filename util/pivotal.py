from pivotalclient import PivotalClient

# from config import PIVOTAL_PROJECT_ID, PIVOTAL_API_KEY
PIVOTAL_PROJECT_ID = '2086981'
PIVOTAL_API_KEY = '3a84ad0dbf10e6ca7520334371cc5fdc'

def add_story(story_dict, story_type='bug'):

	pivotal = PivotalClient(PIVOTAL_API_KEY, project_id=PIVOTAL_PROJECT_ID)

	labels = ['bug', ]
	labels.append('add-new-label-here')

	story_dict = {
		'project_id': PIVOTAL_PROJECT_ID,
		'name': 'My Test Story 2',
		'description': 'Lorem ipsum dolor sic amet consectitur yadda yadda yadda blah blah blah',
		'story_type': story_type,
		'current_state': 'unstarted', # MUST always be 'unstarted'
		'labels': labels,
	}
	new_story = pivotal.create_story(story_dict)

	# print "This story's ID number is:", new_story.id
	return new_story.id