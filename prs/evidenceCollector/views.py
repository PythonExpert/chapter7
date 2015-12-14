from django.http import HttpResponse

from evidenceCollector.models import Log 

import datetime
import logging

def index(request, contentid, event):

    sessionId = request.GET.get('sessionid', 0)
    userid = request.GET.get('userid', 0)
    date =  request.GET.get('date', datetime.datetime.now().isoformat())
    visitCount = request.GET.get('visitCount', 0)
    l = Log(created=date, \
    	    user_id = userid, \
    	    content_id = contentid, \
    	    event = event, \
    	    visitCount = visitCount, \
    	    sessionId = sessionId)
    l.save()

    return HttpResponse('ok')