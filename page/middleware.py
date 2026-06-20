from .models import VisitorLog

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. محاولة الحصول على الـ IP الحقيقي عبر X-Forwarded-For
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # العنوان الحقيقي يكون أول عنوان في القائمة
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            # في حال عدم وجوده، نستخدم REMOTE_ADDR التقليدي
            ip = request.META.get('REMOTE_ADDR')

        path = request.path
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # استثناء الملفات الثابتة ولوحة التحكم من التسجيل لتوفير المساحة
        if not path.startswith('/static/') and not path.startswith('/admin/'):
            VisitorLog.objects.create(
                ip_address=ip,
                page_visited=path,
                user_agent=user_agent
            )

        response = self.get_response(request)
        return response