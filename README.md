Learning Django with https://www.youtube.com/watch?v=F5mRW0jo-U4

Learn later:  
where from user in request, what is request  
- в кратце: request это набор текста, который распарсивается - WSGIRequest (django.core.handlers.wsgi)  
- дальше этот request передается в нужную вьюху, но предварительно вьюха оборачивается в мидлвари - WSGIHandler  
- и таким образом реквест попадает во вьюху; причем с нужными аргументами из ResolverMatch
how are routes connected?  
- джанго забирает urlpatterns и составляет список вьюх
what are forms, and how are they connected
- ?

Stopped at 2:14:10 raw html form  
Can I create url from template without hardcode? - yes:)  

Stopped at 3:07:35  
can I improve ListView with context? and data from request?  
why should I use pk in DetailView?  
How exactly work *View? as_view?  
how id is passed from to view functions before?  
very bad form actions on detail page :(  
  I can only make redirect actually with <a... seems nice  

Stopped at 3:24:00  
there are raw forms also...  

the end  

Next steps:  
answer questions above  
watch other videos on yt, get useful info from there  (Next one is getting useful things from: https://www.youtube.com/watch?v=jBzwzrDvZ18)

I want to get info about serialization, postgresql, redis, celery, rabbitmq  


