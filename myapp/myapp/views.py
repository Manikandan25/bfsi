from django.http import HttpResponse



def read_file(request):
    f = open('.well-known/pki-validation/E606AF4FAC6B2F58B272721FDE6B8E16.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
