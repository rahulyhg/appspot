# -*- coding:utf8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from srishell.sritext.trie import TRIE
from converters.getUnicode import getUnicode
atoz = ''.join(map(chr, range(ord('a'),ord('z')+1)))
def ajax_words(request):
    inp = request.GET.get('input')
    getwords=lambda inp:[getUnicode(str(x).replace("|",'')) for x in TRIE.findAll(inp, False)]
    return HttpResponse(simplejson.dumps(getwords(inp)))