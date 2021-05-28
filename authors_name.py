# simple program to identify a name and return it like an author's name

words = ['junior', 'filho', 'neto'] # 

def org(name):
    full_name = name.split() # 

    if any(i in words for i in full_name): # 
        agnome = str([a for a in words if a in full_name])
        if full_name[-1] == agnome:
            if len (full_name) > 2:
                org_name = full_name[-2] + ', ', agnome.upper() + ', ', full_name[0].capitalize() #
            else:
                return TypeError
        else:
            return TypeError
    
    else:
        org_name = full_name[-1].upper() + ', ', full_name[0].capitalize()

    final_org_name = ''.join(org_name)
    return final_org_name

# some output
name = input(str())
print('Autor: {}'.format(org(name)))
