"""tt URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from . import view
from django.http import FileResponse, Http404
import os

urlpatterns = [
    path('', view.callindex),
    path('admin/', admin.site.urls),
    path('index/', view.callindex),
    path('contact/', view.contact),
    path('about/', view.about),
    path('login/', view.login),
    path('signin/', view.signin),
    path('timetable/', view.timetable),
    path('program/', view.program),
    path('faculty/', view.faculty),
    path('subject/', view.subject),
    path('lecture/', view.lecture),
    path('lab/', view.lab),
    path('generate/', view.generate),
    path('generatepage/', view.generatepage),
    path('output/', view.output),
    path('view_course/', view.view_course),
    path('view_faculty/', view.view_faculty),
    path('view_labRoom/', view.view_labRoom),
    path('view_lectureRoom/', view.view_lectureRoom),
    path('view_program/', view.view_program),
    path('loginadmin', view.loginadmin),
    path('callsignin', view.callsignin),
    path('callprogram', view.callprogram),
    path('callsubjects', view.callsubjects),
    path('calllecture', view.calllecture),
    path('calllab', view.calllab),
    path('callfaculty', view.callfaculty),
    path('callview_course/', view.callview_course),
    path('callview_lectureRoom/', view.callview_lectureRoom),
    path('callview_labRoom/', view.callview_labRoom),
    path('callview_faculty/', view.callview_faculty),
    path('callview_program/', view.callview_program),
    path('deletecourse/', view.delete_course),
    path('deleteprogram/', view.delete_program),
    path('deletefaculty/', view.delete_faculty),
    path('deletelectureroom/', view.delete_lectureroom),
    path('deletelabroom/', view.delete_labroom),
    path('replace_professor/', view.replace_professor),
    path('download_timetable/', view.download_timetable),
    path('download_faculty_report/', view.download_faculty_report),
    path('download_lab_report/', view.download_lab_report),
]

# ============ ADD THIS SECTION TO SERVE STATIC FILES ============
if settings.DEBUG:
    assets_root = os.path.join(settings.BASE_DIR, 'assets')
    
    def serve_asset(request, path):
        """Serve files from assets folder"""
        file_path = os.path.join(assets_root, path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            # Get file extension for content type
            ext = os.path.splitext(file_path)[1].lower()
            content_types = {
                '.mp4': 'video/mp4',
                '.webm': 'video/webm',
                '.ogg': 'video/ogg',
                '.css': 'text/css',
                '.js': 'application/javascript',
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif',
                '.ico': 'image/x-icon',
                '.svg': 'image/svg+xml',
            }
            content_type = content_types.get(ext, 'application/octet-stream')
            return FileResponse(open(file_path, 'rb'), content_type=content_type)
        raise Http404()
    
    urlpatterns += [
        re_path(r'^assets/(?P<path>.*)$', serve_asset),
        # Also serve other static files with common extensions
        re_path(r'^(?P<path>.*\.(?:mp4|webm|ogg|css|js|png|jpg|jpeg|gif|ico|svg))$', serve_asset),
    ]