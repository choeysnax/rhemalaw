from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    pass


# Insights
@register_snippet
class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class AboutPage(Page):
    content_panels = Page.content_panels + [
    ]


class AreasOfPracticePage(Page):
    content_panels = Page.content_panels + [
    ]


class ContactPage(Page):
    content_panels = Page.content_panels + [
    ]


class TeamPage(Page):
    content_panels = Page.content_panels + [
    ]


class StandardPage(Page):
    body = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class InsightPage(Page):
    insight_title = models.TextField(blank=True)
    subtitle = models.CharField(blank=True, max_length=255)
    body = RichTextField()
    external_link = models.URLField(blank=True)
    date_published = models.DateField(
        "Date article published", blank=True, null=True
    )
    tags = models.ManyToManyField(Tag)

    content_panels = Page.content_panels + [
        FieldPanel('insight_title', classname="full"),
        FieldPanel('subtitle', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('external_link', classname="full"),
        FieldPanel('tags'),
        FieldPanel('date_published'),
    ]

    # Specifies parent to BlogPage as being BlogIndexPages
    parent_page_types = ['InsightIndexPage']
    subpage_types = []


class InsightIndexPage(RoutablePageMixin, Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]
    subpage_types = ['InsightPage']

    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request, **kwargs):
        context = super(InsightIndexPage, self).get_context(request)
        context['insights'] = InsightPage.objects.descendant_of(self).live().order_by(
            '-date_published')
        return context
