def new_list():
    newlist ={
        'first': None,
        'last': None,
        'size': 0,
    }
    return newlist


def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list): 
        raise IndexError('list index out of range')  
    
    node = my_list["first"]
    searchpos = 0
    
    while searchpos < pos:
        if node is None:
            raise IndexError('list index out of range')
        node = node["next"]
        searchpos += 1

    if node is None:
        raise IndexError('list index out of range')

    return node



def is_present(my_list,element, cmp_function): 
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
            
    if not is_in_array:
        count = -1
    return count
    
    
def size(my_list):
    return my_list['size']


def add_first(my_list, element):
    dict_element = {
        'info': element,
        'next': my_list['first'] 
    }

    my_list['first'] = dict_element 
    
    if my_list['last'] is None: 
        my_list['last'] = dict_element

    my_list['size'] += 1
    
    return my_list




def add_last(my_list,element):
    
    dict_element = {}
    dict_element['info'] = element
    dict_element['next'] = None
    
    if my_list['last'] == None:
        my_list['first'] = dict_element
        my_list['last'] = dict_element
    else:
        my_list['last']['next'] = dict_element
        my_list['last'] = dict_element
        
    my_list['size'] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['first']
    
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['last']
    
    
def is_empty(my_list):
    if my_list['size'] == 0:
        return True
    else:
        return False
    
def remove_first(my_list):
    if size(my_list) == 0:
        raise IndexError('list index out of range')
    
    node = my_list['first']
            
    if my_list['first']['next'] is None:
        my_list['first'] = None
        my_list['last'] = None
    else:
        my_list['first'] = my_list['first']['next']
        
    my_list['size'] -= 1
    return node['info']
        
        
def remove_last(my_list):
    if my_list['first'] is None:
        raise IndexError('list index out of range')
    
    temp = my_list['first']
    
    if temp['next'] is None:
        return remove_first(my_list)
    
    while temp['next']['next'] is not None:
        temp = temp['next']
        
    node = temp['next']
    temp['next'] = None
    my_list['last'] = temp
    my_list['size'] -= 1

    return node['info']

  
    
def insert_element(my_list,element,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    new_node = {
        'info': element,
        'next': None
    }
    if pos == 0:
        return add_first(my_list,element)
    elif pos == size(my_list):
        return add_last(my_list,element)
    else:
        temp = my_list['first']
        for i in range(pos - 1):
            temp = temp['next']

        new_node['next'] = temp['next']
        temp['next'] = new_node
        
    my_list['size'] += 1
    return my_list
    
def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
  
    if pos == 0:
        remove_first(my_list)
        return my_list
    elif pos == size(my_list) -1:
        remove_last(my_list)
        return my_list
    else:
        
        temp = my_list['first']
        for i in range(pos - 1):
            temp = temp['next']

        node = temp['next']
        temp['next'] = node['next']
        
    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    node = my_list["first"]
    for i in range(pos):
        node = node["next"]

    node["info"] = new_info 
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 > my_list['size'] or
        pos_2 < 0 or pos_2 > my_list['size']):
        raise Exception('list index out of range')
    
    if pos_1 == pos_2:
        return my_list

    node_1 = my_list['first']
    for _ in range(pos_1):
        node_1 = node_1['next']
    
    node_2 = my_list['first'] 
    for _ in range(pos_2):
        node_2 = node_2['next']
        

    node_1['info'], node_2['info'] = node_2['info'], node_1['info']
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos_i + num_elements > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    node_1 = get_element(my_list,pos_i)

    sublist ={
        'first': node_1,
        'last': None,
        'size': num_elements,
    }
    
    node_2 = get_element(my_list,num_elements)
    sublist['last'] = node_2
        
    return sublist




#Algoritmos de ordenamiento

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted   

def shell_sort(my_list, sort_criteria):

    n = size(my_list)
    gap = n // 2  

    while gap > 0:
        for i in range(gap, n):
            temp_value = get_element(my_list, i)  
            j = i

 
            while j >= gap and sort_criteria(get_element(my_list, j - gap), temp_value) > 0:
                change_info(my_list, j, get_element(my_list, j - gap))  
                j -= gap

            change_info(my_list, j, temp_value)  

        gap //= 2  
def selection_sort(my_list, compare_function):
    if my_list['first'] is None:
        return
    
    current = my_list['first']
    
    while current:
        min_node = current
        next_node = current['next']
        
        while next_node:
            if compare_function(next_node['info'], min_node['info']):
                min_node = next_node
            next_node = next_node['next']
            
        if current != min_node:
            current['info'], min_node['info'] = min_node['info'], current['info']
            
        current = current['next']
    
    return my_list


def insertion_sort(my_list,sort_criteria):
    
    tamanio = size(my_list)

    if tamanio != 0 :
        
  
     for i in range(1,tamanio):
        
        element = get_element(my_list,i)
        
        j = i - 1
        
        while j >= 0 and sort_criteria(element,get_element(my_list,j)):
            
            
            exchange(my_list,j+1,j)
            j -= 1
            
        change_info(my_list, j + 1, element)
        
        
    return my_list
            


def merge_sort(my_list, sort_criteria):
    
    
    if size(my_list) > 1:
        mid = size(my_list) // 2
        left_half = sub_list(my_list, 0, mid)
        right_half = sub_list(my_list, mid, size(my_list) - mid)

        merge_sort(left_half, sort_criteria)
        merge_sort(right_half, sort_criteria)

        merge(my_list, left_half, right_half, sort_criteria)

    return my_list



def merge(my_list, left_half, right_half, sort_criteria):
   
    left_node = left_half['first']
    right_node = right_half['first']
    current = None

    if sort_criteria(left_node['info'], right_node['info']):
        my_list['first'] = left_node
        left_node = left_node['next']
    else:
        my_list['first'] = right_node
        right_node = right_node['next']

    current = my_list['first']

    while left_node is not None and right_node is not None:
        if sort_criteria(left_node['info'], right_node['info']):
            current['next'] = left_node
            left_node = left_node['next']
        else:
            current['next'] = right_node
            right_node = right_node['next']
        current = current['next']

    while left_node is not None:
        current['next'] = left_node
        left_node = left_node['next']
        current = current['next']

    while right_node is not None:
        current['next'] = right_node
        right_node = right_node['next']
        current = current['next']

    my_list['last'] = current
    my_list['size'] = size(left_half) + size(right_half)


def quick_sort(my_list, sort_criteria):
    if size(my_list) <= 1:
        return my_list
    
    pivot = get_element(my_list, size(my_list) - 1)
    left = {'first': None, 'last': None, 'size': 0}
    right = {'first': None, 'last': None, 'size': 0}
    equal = {'first': None, 'last': None, 'size': 0}
    
    current = my_list['first']
    while current is not None:
        if sort_criteria(current['info'], pivot):
            append(left, current['info'])
        elif sort_criteria(pivot, current['info']):
            append(right, current['info'])
        else:
            append(equal, current['info'])
        current = current['next']
    
    quick_sort(left, sort_criteria)
    quick_sort(right, sort_criteria)
    
    return concat_listas(left, equal, right)


def append(my_list, value):
    new_node = {'info': value, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    my_list['size'] += 1


def concat_listas(left, equal, right):
    result = {'first': None, 'last': None, 'size': 0}
    
    for lst in [left, equal, right]:
        if lst['first'] is not None:
            if result['first'] is None:
                result['first'] = lst['first']
            else:
                result['last']['next'] = lst['first']
            result['last'] = lst['last']
            result['size'] += lst['size']
    
    return result














