## simple program to identify a name and return it like an author's name ##

words = ['junior', 'filho', 'filha', 'neto', 'neta'] # so here i defined some possible agnomes that could be in the end
                                                     # of the given name, and then give it preference with the first condition
                                                     # e.g input = João Silva Neto | output = SILVA NETO, João.

def org(name):
    name_list = name.split() # i splited the name into a list so i can iterate between words using index 
    if any(i in words for i in name_list): # if any word 'i' in the list 'words' is in the 'name_list' which i just splitted exists, then
        org_name = name_list[-2].upper() + ' ', name_list[-1].upper() + ', ', name_list[0].capitalize() # it will rearrange the name adding the 'word' next to the last name, then the first name.
        final_org_name = ''.join(org_name) #here i created a variable containing the rearragend and formated name so i can
        return final_org_name # return it
    
    elif len(name_list) == 1: # now if the input name is a single cell 
        org_name = name_list[1].capitalize() # just capitalize it and return
        final_org_name = ''.join(org_name)
        return final_org_name
    
    else: # if theres no words from the words list, return it author's name like
        org_name = name_list[-1].upper() + ', ', name_list[0].capitalize()
        final_org_name = ''.join(org_name)
        return final_org_name


name = input(str())
print('Autor: {}'.format(org(name)))
