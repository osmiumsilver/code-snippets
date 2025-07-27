def find_index(the_list, value):
    listo=[]
    for index,outer_element in enumerate(the_list):
        if outer_element == value:
            listo.append([index])
        elif isinstance(the_list[index], list):
            for inner_element in find_index(the_list[index],value):
                listo.append([index]+inner_element)
    return listo
example = [[[1,2,3],2,[1,3]],[1,2,3]]
print(find_index(example,2))