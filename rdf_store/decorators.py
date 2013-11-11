# coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext


#Source: http://lincolnloop.com/blog/2008/may/10/getting-requestcontext-your-templates/
def render_to(template_name):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(template_name, output, context_instance=RequestContext(request))
        return wrapper
    return renderer