from ajax_select import register, LookupChannel
from .models import Question


@register('questions')
class QuestionLookup(LookupChannel):

    model = Question

    def get_query(self, q, request):
        return self.model.objects.filter(question_text__icontains=q)[:10]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.question_text

