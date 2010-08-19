from search.forms import SearchForm
from django.views.generic.simple import direct_to_template
from profiles.models import Profile, Skill
from profiles.controllers import tag_clean
from itertools import chain

def search(request):
    if request.method == "POST":
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            query = searchform.data.get('query')
            query_list = query.lower().split(',')
            if len(query_list) > 1:
                try:
                    qs = [list(chain(*[skill.profile_set.all() for skill in Skill.objects.filter(name__contains=tag_clean(qry))])) for qry in query_list]
                    results = list(set(qs[0]).intersection(*qs))
                except Exception as e:
                    results = None
            else:
                try:
                    results = list(chain(Skill.objects.get(name__contains=query_list[0]).profile_set.all()))
                except Exception as e:
                    if e.__class__ == Skill.MultipleObjectsReturned:
                        results = list(chain(*[skill.profile_set.all() for skill in Skill.objects.filter(name__contains=query_list[0])]))
                    else:
                        results = None
            searchform = SearchForm({'query':query})
    else:
        searchform = SearchForm()
    return direct_to_template(request, 'search/grep.html', locals())
