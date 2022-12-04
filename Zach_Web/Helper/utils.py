menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Add', 'url_name': 'add'},
    {'title': 'Projects', 'url_name': 'projects'},
    {'title': 'Organizer', 'url_name': 'organizer'},
    {'title': 'Settings', 'url_name': 'settings'},
]


class DataMixin:
    # формирует контекст по умолчанию
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_select' not in context:
            context['cat_select'] = 0
        return context
