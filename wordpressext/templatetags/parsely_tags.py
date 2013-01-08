import json

from django import template
from django.conf import settings

IMAGE_URL = getattr(settings, "PARSELY_IMAGE_URL", None)

register = template.Library()


@register.simple_tag(takes_context=True)
def parselymeta(context, post):

    request = context.get("request")

    if not request:
        return  # fail silently, request context is required

    data = {
        "title": post.title,
        "link": request.build_absolute_uri(post.get_absolute_url()),
        "type": "post",
        "post_id": post.id,
        "pub_date": post.post_date.isoformat(),
        "section": "Blog",
        "author": post.author.display_name,
        "tags": [t.name for t in post.tags()],
    }

    if IMAGE_URL:
        data["image_url"] = IMAGE_URL

    return """<meta name="parsely-page" content="%s">""" % json.dumps(data)
