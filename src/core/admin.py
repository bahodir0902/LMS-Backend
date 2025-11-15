"""
Django Unfold admin callbacks and configurations
"""
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display


def environment_callback(request):
    """
    Callback function to display environment information in the admin header
    """
    from decouple import config
    
    environment = config("ENVIRONMENT", default="development")
    colors = {
        "development": "bg-yellow-100 text-yellow-800",
        "staging": "bg-blue-100 text-blue-800",
        "production": "bg-red-100 text-red-800",
    }
    
    color_class = colors.get(environment.lower(), "bg-gray-100 text-gray-800")
    
    return format_html(
        '<span class="px-2 py-1 rounded text-xs font-semibold {}">{}</span>',
        color_class,
        environment.upper(),
    )


def dashboard_callback(request, context):
    """
    Dashboard callback to display widgets and statistics
    """
    from django.contrib.auth import get_user_model
    from src.apps.courses.models import Course
    from src.apps.assignments.models import Task
    from src.apps.submissions.models import Answer
    from src.apps.grades.models import Grade
    from src.apps.notifications.models import Notification
    
    User = get_user_model()
    
    # Add dashboard widgets to context
    context.update({
        "dashboard_widgets": [
            {
                "type": "link",
                "title": "Total Users",
                "description": f"{User.objects.count()} registered users",
                "link": "/admin/users/user/",
            },
            {
                "type": "link",
                "title": "Total Courses",
                "description": f"{Course.objects.count()} active courses",
                "link": "/admin/courses/course/",
            },
            {
                "type": "link",
                "title": "Total Assignments",
                "description": f"{Task.objects.count()} tasks",
                "link": "/admin/assignments/task/",
            },
            {
                "type": "link",
                "title": "Total Submissions",
                "description": f"{Answer.objects.count()} answers",
                "link": "/admin/submissions/answer/",
            },
            {
                "type": "link",
                "title": "Total Grades",
                "description": f"{Grade.objects.count()} graded submissions",
                "link": "/admin/grades/grade/",
            },
            {
                "type": "link",
                "title": "Unread Notifications",
                "description": f"{Notification.objects.filter(is_read=False).count()} unread",
                "link": "/admin/notifications/notification/",
            },
        ]
    })
    
    return context

