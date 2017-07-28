from pivotalclient import PivotalClient

PROJECT_ID = '2086981'
API_KEY = '3a84ad0dbf10e6ca7520334371cc5fdc'

pivotal = PivotalClient(API_KEY, project_id=PROJECT_ID)


story_dict = {
	'project_id': PROJECT_ID,
	'name': 'My Test Story 2',
	'description': 'Lorem ipsum dolor sic amet consectitur yadda yadda yadda blah blah blah',
	'story_type': 'bug',
	'current_state': 'unstarted',
	'labels': ['myproject', 'translate-core', 'admin', 'test-label'],
}
new_story = pivotal.create_story(story_dict)
print "This story's ID number is:", new_story.id