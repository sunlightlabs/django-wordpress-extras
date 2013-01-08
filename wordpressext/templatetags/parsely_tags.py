import json

from django import template
from django.conf import settings

IMAGE_URL = getattr(settings, "PARSELY_IMAGE_URL", None)

register = template.Library()


def _parsely_clean(s):
    s = s.replace('"', '\\"')     # double quote to escaped double quote
    s = s.replace("'", "\u0027")  # single quote to unicode
    s = s.replace("\n", " ")      # new line to empty string
    return s


@register.simple_tag(takes_context=True)
def parselymeta(context, post):

    request = context.get("request")

    if not request:
        return  # fail silently, request context is required

    data = {
        "title": _parsely_clean(post.title),
        "link": request.build_absolute_uri(post.get_absolute_url()),
        "type": "post",
        "post_id": post.id,
        "pub_date": post.post_date.isoformat(),
        "section": "Blog",
        "author": _parsely_clean(post.author.display_name),
        "tags": [_parsely_clean(t.name) for t in post.tags()],
    }

    if IMAGE_URL:
        data["image_url"] = IMAGE_URL

    return """<meta name='parsely-page' content='%s'>""" % json.dumps(data)
