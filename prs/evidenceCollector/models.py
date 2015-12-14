from django.db import models

class Log(models.Model):
	created = models.DateTimeField('date happened')
	user_id = models.CharField(max_length=200)
	content_id = models.CharField(max_length=200)
	event = models.CharField(max_length=200)
	sessionId = models.CharField(max_length=200)
	visitCount = models.IntegerField()

	def _str_(self):
		return "%s, %s, %s" % (user_id, content_id, event)
