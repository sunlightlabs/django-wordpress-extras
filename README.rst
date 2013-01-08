=======================
django-wordpress-extras
=======================

A collection of useful, non-WordPress extensions for
django-wordpress (the real one).

::

    pip install the-real-django-wordpress-extras

Add *wordpressext* to INSTALLED_APPS in settings.py.

Be sure to put *wordpressext* **above** *wordpress* in urls.py::

    urlpatterns += patterns('',
        ...
        url(r'^blog/', include('wordpressext.urls')),
        url(r'^blog/', include('wordpress.urls')),
        ...
    )

Email sender is determined in the following order:

    #. **settings.WPEXT_SENDER** email address
    #. **settings.POSTMARK_SENDER** if Postmark settings are configured and WPEXT_SENDER does not exist
    #. **settings.ADMINS** the first admin email address, if POSTMARK_SENDER does not exist


--------
Features
--------

Parse.ly Meta Template Tag
==========================

Generate a `Parse.ly <http://parse.ly/>`_ meta tag::

    {% parselymeta post %}


Disqus Comment Notifications
============================

It's the only feature for now! And it's only half implemented!

If you use `Disqus <http://disqus.com/>`_ for comments, you can provide a
post-comment JavaScript hook to notify post authors of the new comment.
Here is some example JavaScript you can do enable comment notifications::

    var newComment = function(comment) {
        var url = window.location.href + "disqus/";
        var params = {
            id: comment.id,
            text: comment.text,
            csrfmiddlewaretoken: csrftoken  // you'll have to get this from somewhere
        };
        $.post(url, comment, function(data) {
            // don't really need to do anything
        });
    };

    var disqus_config = function() {
        this.callbacks.onNewComment = [function(comment) { newComment(comment); }];
    };

The comment endpoint is located at ``<path_to_blog>/<year>/<month>/<day>/<slug>/disqus/``. It accepts the following POST parameters:

    * *id* the Disqus ID of the comment
    * *text* the text of the comment
    * *csrfmiddlewaretoken* a CSRF token, if protection is enabled

Refer to the `onNewComment <http://help.disqus.com/customer/portal/articles/466258-how-can-i-capture-disqus-commenting-activity-in-my-own-analytics-tool->`_ callback on how to implement your own.

Future versions will connect with the Disqus API to do various things.
