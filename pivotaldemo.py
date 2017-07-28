from pivotalclient import PivotalClient

PROJECT_ID = '2086981'
API_KEY = '3a84ad0dbf10e6ca7520334371cc5fdc'

pivotal = PivotalClient(API_KEY, project_id=PROJECT_ID)


story_dict = {
	'project_id': PROJECT_ID,
	'name': 'My Test Story',
	'description': 'Lorem ipsum dolor sic amet consectitur yadda yadda yadda blah blah blah',
	'story_type': 'bug',
	'current_state': 'unstarted',
}
new_story = pivotal.create_story(story_dict)
print new_story
print dir(new_story)