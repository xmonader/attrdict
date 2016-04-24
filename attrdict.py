
class attrdict(dict):
    def __getattr__(self, k):
        return self[k]

    def __dir__(self):
        atts=list(self.keys())
        atts.extend(dir(super()))

        return atts

def toattrdict(d):
    if isinstance(d, dict):
        d=attrdict(d) #the parent
        for k,v in d.items():
            if isinstance(v, dict):
                d[k]=toattrdict(v)

        return d
    return d

if __name__=="__main__":

    d={'person': {
    'name': 'ahmed',
    'age': 26,
    'contact': {
    'email': {
        'personal': 'xmonader@gmail.com',
        'work': 'thabeta@codescalers.com',
    },
    'phone':'01224124',
    }
    }}

    #d2=toattrdict(d)
    d2=toattrdict(d)
    d2['a']=5
    print(dir(d2))
    print(d2.person.contact.email.work)
