from .models import VisitorLog

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # استخراج عنوان الـ IP والمسار
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # استثناء الملفات الثابتة (static) من التسجيل لتقليل حجم البيانات
        if not path.startswith('/static/') and not path.startswith('/admin/'):
            VisitorLog.objects.create(
                ip_address=ip,
                page_visited=path,
                user_agent=user_agent
            )

        response = self.get_response(request)
        return response