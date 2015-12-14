from django.db import models

class Event(models.Model):
	created = models.DateTimeField()
	event = models.CharField(max_length = 100)
	user_id = models.CharField(max_length = 200)
	content_id = models.CharField(max_length = 200)
	sessionId = models.CharField(max_length = 200)

	class Meta:
		managed = False
		db_table = 'evidenceCollector_log'

def get_likes(strategy, details, response, *args, **kwargs):
    if strategy.backend.name == 'facebook':
        likes = strategy.backend.get_json(
            'https://graph.facebook.com/%s/likes' % response['id'],
            params={'access_token': response['access_token']}
        )
        for like in likes['data']:
            pass  # Process and save likes here
