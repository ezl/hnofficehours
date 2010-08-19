def tag_clean(tagstring):
    return ' '.join(filter(lambda x: x != u'', tagstring.split(' ')))
