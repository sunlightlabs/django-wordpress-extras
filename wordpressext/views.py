from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from wordpress.models import Post


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
            }

            body = render_to_string('wordpressext/email/new_comment.txt', context)

            # send the mail

            send_mail(
                subject='[SunlightFoundation.com] New comment on %s' % post.title,
                message=body,
                from_email='contact@sunlightfoundation.com',
                recipient_list=[post.author.email],
            )

    return HttpResponse("")
