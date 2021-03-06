from django.views.generic import TemplateView

from common.views import BaseServicesListView, BaseServicesDetailView, BaseBeforeAfterListView, BaseBlogListView, \
    BaseBlogDetailView, BaseServiceCategoryListView, BaseServiceCategoryDetailView, BaseSearchView
from male.forms import MaleBlogCommentForm
from male.models import MaleServiceItem, MaleBeforeAfterItem, MaleBlog, MaleBlogCategory, MaleServiceCategory, \
    MaleBeforeAfterCategory
from utils.views import GenderedViewMixin


class MaleHomePage(GenderedViewMixin, TemplateView):
    gender = "male"
    template_name = "pages/home.html"


class MaleAboutPage(GenderedViewMixin, TemplateView):
    gender = "male"
    template_name = "pages/about.html"


class MaleServiceCategoryListView(BaseServiceCategoryListView):
    gender = "male"
    model = MaleServiceCategory


class MaleServiceCategoryDetailView(BaseServiceCategoryDetailView):
    gender = "male"
    model = MaleServiceCategory


class MaleServicesListView(BaseServicesListView):
    model = MaleServiceItem
    gender = "male"


class MaleServicesDetailView(BaseServicesDetailView):
    gender = "male"
    model = MaleServiceItem


class MaleHowitworksPage(GenderedViewMixin, TemplateView):
    gender = "male"
    template_name = "pages/howitworks.html"


class MaleBeforeAfterListView(BaseBeforeAfterListView):
    gender = "male"
    model = MaleBeforeAfterItem
    category_model = MaleBeforeAfterCategory


class MaleBlogListView(BaseBlogListView):
    gender = "male"
    model = MaleBlog
    category_model = MaleBlogCategory


class MaleBlogDetailView(BaseBlogDetailView):
    gender = "male"
    model = MaleBlog
    form_class = MaleBlogCommentForm


class MaleContactPage(GenderedViewMixin, TemplateView):
    gender = "male"
    template_name = "pages/contact.html"


class MaleKVKKPage(GenderedViewMixin, TemplateView):
    gender = "male"
    template_name = "pages/kvkk.html"


class MaleSearchView(BaseSearchView):
    gender = "male"
    blog_model = MaleBlog
    service_model = MaleServiceItem
