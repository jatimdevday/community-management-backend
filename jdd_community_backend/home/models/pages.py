from django.db import models

from wagtail.search import index
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

class IndexPage(Page):
    '''
    This page is for displaying multiple posts,
    such as blog posts, event posts, etc.
    '''
    template = 'pages/index_page.html'
    parent_page_types = ['home.HomePage']

    intro = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    @property
    def posts(self):
        # Get list of live blog pages that are descendants of this page
        posts = IndexPage.objects.live().descendant_of(self)

        # Order by most recent date first
        posts = posts.order_by('-date')

        return posts

    def get_context(self, request):
        # Get posts
        posts = self.posts

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            posts = posts.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(posts, 10)  # Show 10 posts per page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        # Update template context
        context = super(IndexPage, self).get_context(request)
        context['posts'] = posts
        return context

IndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    # InlinePanel('related_links', label="Related links"),
]

IndexPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]

class SinglePage(Page):
    template = 'pages/single.html'
    parent_page_types = ['home.HomePage']

    intro = RichTextField()
    date = models.DateField("Post date", blank=True, null=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
    ])
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [ 
        index.SearchField('body')
    ]

SinglePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('intro', classname="full"),
    StreamFieldPanel('body')
]

SinglePage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image')
]
