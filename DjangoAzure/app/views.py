"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'お問い合わせ',
            'message':'お問い合わせ',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'免責事項',
            'message':'本サイトで公表するプログラム及び資料等により、使用者が直接間接に蒙ったいかなる損害に対しても、何らの保証責任及び賠償責任を負うものではありません。 使用者の責任のもと、プログラムの使用、結果の利用を行ってください。',
            'year':datetime.now().year,
        }
    )
