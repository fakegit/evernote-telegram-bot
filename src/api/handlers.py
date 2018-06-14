from datetime import datetime


def telegram_hook(request):
    data = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    return data.encode()


def evernote_oauth(request):
    return b'evernote_oauth'


def error(request):
    raise Exception('Some application error')
