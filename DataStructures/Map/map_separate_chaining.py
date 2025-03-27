import random
from DataStructures import array_list as array
from DataStructures import single_linked_list as slist
from DataStructures import map_entry as me
from DataStructures import map_functions as mf
from Utils import error as error

def new_map(num_elements, load_factor, prime=109345121):
    try:
        
        TESTING_MODE = True

        map_struct = {
            'prime': prime,
            'capacity': mf.next_prime(int(num_elements / load_factor)),
            'scale': 1 if TESTING_MODE else random.randint(1, prime - 1),
            'shift': 0 if TESTING_MODE else random.randint(0, prime - 1),
            'table': array.newList('ARRAY_LIST'),
            'current_factor': 0.0,
            'limit_factor': load_factor,
            'size': 0
        }

        for _ in range(map_struct['capacity']):
            array.addLast(map_struct['table'], slist.newList('SINGLE_LINKED'))

        return map_struct

    except Exception as e:
        error.reraise(e, 'new_map')

def put(map_struct, key, value):
    try:
        pos = mf.hash_value(key, map_struct['capacity'],
                            map_struct['prime'],
                            map_struct['scale'],
                            map_struct['shift'])

        bucket = array.getElement(map_struct['table'], pos)

        for i in range(slist.size(bucket)):
            entry = slist.getElement(bucket, i)
            if entry['key'] == key:
                entry['value'] = value
                return

        new_entry = me.newMapEntry(key, value)
        slist.addLast(bucket, new_entry)

        map_struct['size'] += 1
        map_struct['current_factor'] = map_struct['size'] / map_struct['capacity']

        if map_struct['current_factor'] >= map_struct['limit_factor']:
            rehash(map_struct)

    except Exception as e:
        error.reraise(e, 'put')

def default_compare(key1, key2):
    return key1 == key2

def contains(map_struct, key):
    try:
        pos = mf.hash_value(key, map_struct['capacity'],
                            map_struct['prime'],
                            map_struct['scale'],
                            map_struct['shift'])

        bucket = array.getElement(map_struct['table'], pos)

        for i in range(slist.size(bucket)):
            entry = slist.getElement(bucket, i)
            if entry['key'] == key:
                return True

        return False

    except Exception as e:
        error.reraise(e, 'contains')

def remove(map_struct, key):
    try:
        pos = mf.hash_value(key, map_struct['capacity'],
                            map_struct['prime'],
                            map_struct['scale'],
                            map_struct['shift'])

        bucket = array.getElement(map_struct['table'], pos)

        for i in range(slist.size(bucket)):
            entry = slist.getElement(bucket, i)
            if entry['key'] == key:
                slist.removeElement(bucket, i)
                map_struct['size'] -= 1
                map_struct['current_factor'] = map_struct['size'] / map_struct['capacity']
                return

    except Exception as e:
        error.reraise(e, 'remove')

def get(map_struct, key):
    try:
        pos = mf.hash_value(key, map_struct['capacity'],
                            map_struct['prime'],
                            map_struct['scale'],
                            map_struct['shift'])

        bucket = array.getElement(map_struct['table'], pos)

        for i in range(slist.size(bucket)):
            entry = slist.getElement(bucket, i)
            if entry['key'] == key:
                return entry['value']

        return None

    except Exception as e:
        error.reraise(e, 'get')

def size(map_struct):
    return map_struct['size']

def is_empty(map_struct):
    return map_struct['size'] == 0

def key_set(map_struct):
    try:
        keys = array.newList('ARRAY_LIST')

        for i in range(map_struct['capacity']):
            bucket = array.getElement(map_struct['table'], i)
            for j in range(slist.size(bucket)):
                entry = slist.getElement(bucket, j)
                array.addLast(keys, entry['key'])

        return keys

    except Exception as e:
        error.reraise(e, 'key_set')
        
def value_set(map_struct):
    try:
        values = array.newList('ARRAY_LIST')

        for i in range(map_struct['capacity']):
            bucket = array.getElement(map_struct['table'], i)
            for j in range(slist.size(bucket)):
                entry = slist.getElement(bucket, j)
                array.addLast(values, entry['value'])

        return values

    except Exception as e:
        error.reraise(e, 'value_set')

def rehash(map_struct):
    try:
        new_capacity = mf.next_prime(map_struct['capacity'] * 4)
        new_table = array.newList('ARRAY_LIST')

        for _ in range(new_capacity):
            array.addLast(new_table, slist.newList('SINGLE_LINKED'))

        old_table = map_struct['table']
        old_capacity = map_struct['capacity']

        map_struct['capacity'] = new_capacity
        map_struct['table'] = new_table
        map_struct['size'] = 0

        for i in range(old_capacity):
            bucket = array.getElement(old_table, i)
            for j in range(slist.size(bucket)):
                entry = slist.getElement(bucket, j)
                put(map_struct, entry['key'], entry['value'])

        map_struct['current_factor'] = map_struct['size'] / map_struct['capacity']

    except Exception as e:
        error.reraise(e, 'rehash')

