from django.shortcuts import render
from google.appengine.api import search


def index(request):
    index = dict(request.REQUEST).get('index', 'city')

    context = {
        'index': index
    }
    return render(request, 'api_search/index.html', context)


def text_search(request):
    limit = int(dict(request.REQUEST).get('limit'))
    offset = int(dict(request.REQUEST).get('offset'))
    search_string = dict(request.REQUEST).get('search_string')
    curr_index = dict(request.REQUEST).get('index', 'city')

    index_search = search.Index(curr_index)

    list_of_ids = query_offset(index_search, search_string, offset, limit)
    total_matches = len(list_of_ids)

    context = {
        'index': curr_index,
        'total_matches': total_matches,
        'list_of_ids': list_of_ids
    }

    return render(request, 'api_search/search_result.html', context)


def query_offset(index, query_string, offset, limit):
    ret = []

    options = search.QueryOptions(offset=offset, limit=limit)
    query = search.Query(query_string=query_string, options=options)

    results = index.search(query)

    for document in results:
        ret.append(document.doc_id)

    return ret


def add(request):
    curr_index = dict(request.REQUEST).get('index', 'city')
    document_title = dict(request.REQUEST).get('document_title')
    document_content = dict(request.REQUEST).get('document_content')

    index_search = search.Index(curr_index)

    document = search.Document(
        fields=[
            search.TextField(name='title', value=document_title),
            search.TextField(name='content', value=document_content)
        ]
    )
    successful = True

    try:
        index_search.put(document)
    except Exception as e:
        successful = False

    context = {
        'successful': successful,
        'index': curr_index
    }
    return render(request, 'api_search/index.html', context)
