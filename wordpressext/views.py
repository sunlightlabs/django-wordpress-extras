from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from wordpress.models import Post


def _get_sender():
    """ Attempt to find the best sender for emails. WPEXT_SENDER is checked
        first, then POSTMARK_SENDER, then the first ADMINS email address.
    """

    if hasattr(settings, 'WPEXT_SENDER'):
        return settings.WPEXT_SENDER

    elif hasattr(settings, 'POSTMARK_SENDER'):
        return settings.POSTMARK_SENDER

    elif settings.ADMINS and settings.ADMINS[0][1]:
        return settings.ADMINS[0][1]

    return "sender@example.com"


def disqus(request, year, month, day, slug):

    if request.method == 'POST' and 'id' in request.POST:

        disqus_id = request.POST['id']
        text = request.POST.get('text', '')

        # get post object

        filters = {
            'post_date__year': int(year),
            'post_date__month': int(month.lstrip('0')),
            'post_date__day': int(day.lstrip('0')),
            'slug': slug,
        }

        post = get_object_or_404(Post.objects.published(), **filters)

        if post.author.email:

            # render email body

            context = {
                'disqus_id': disqus_id,
                'text': text,
                'post': post,
                'site': get_current_site(request),
            }

            subject = render_to_string('wordpressext/email/new_comment_subject.txt', context)
            body = render_to_string('wordpressext/email/new_comment_body.txt', context)

            # send the mail

            send_mail(
                subject=subject,
                message=body,
                from_email=_get_sender(),
                recipient_list=[post.author.email],
            )

    return HttpResponse("")
