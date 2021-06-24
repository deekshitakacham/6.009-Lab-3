#!/usr/bin/env python3

import pickle
# NO ADDITIONAL IMPORTS ALLOWED!

# Note that part of your checkoff grade for this lab will be based on the
# style/clarity of your code.  As you are working through the lab, be on the
# lookout for things that would be made clearer by comments/docstrings, and for
# opportunities to rearrange aspects of your code to avoid repetition (for
# example, by introducing helper functions).


#def transform_data(raw_data):
#    #transform into a dictionary where actors are key and movie is value
#    d = {}
#    for i in raw_data:
#        d[i[0],i[1]] = i[2]
#    return d

def transform_data(raw_data):
    """
    Takes in the raw data and transforms into a dictionary that has dictionaries
    of multiple uses. The first is a dictionary that makes a dictionary 
    that that adds movies acted in. The other returns the actors as keys and
    the actors that they've acted with as the values. 
    """
    #transform into a dictionary where actors are key and movie is value
    #return dictionary, dictionary of dictionaries 
    
    d = {'dict1' : {}, 'dict2' : raw_data, 'dict3': {}}
    
    #make a dictionary that returns several different types of data
    
    for i in raw_data:
        if i[0] not in d['dict1']:
            d['dict1'][i[0]] = set()
        d['dict1'][i[0]].add(i[1])
        if i[1] not in d['dict1']:
            d['dict1'][i[1]] = set()
        d['dict1'][i[1]].add(i[0])
        
    #returns actor as the key and actors they've acted with as values
    
    for i in raw_data: 
        if i[2] not in d['dict3']:
            d['dict3'][i[2]] = set()
        d['dict3'][i[2]].add(i[1])
        d['dict3'][i[2]].add(i[0])
    
    #returns movie as the key and actors in the movies as values
          
    return d

def id_to_actor_name(id_num):
    """
    Takes in an actors's ID number and returns the 
    name associated with it. 
    """
    new_names = {value: key for key, value in namesdb.items()}
    return new_names[id_num]


def id_to_movie_name(id_num):
    """
    Takes in an movie's ID number and returns the 
    name associated with it. 
    """
    new_movies = {value: key for key, value in moviesdb.items()}
    return new_movies[id_num]

def actor_to_id(actor_name):
    """
    Takes in an actors's name and returns the 
    id associated with it. 
    """
    return namesdb[actor_name]

def movie_to_id(movie_name):
    """
    Takes in an movie's name and returns the 
    id associated with it. 
    """
    return moviesdb[movie_name]

def acted_together(data, actor_id_1, actor_id_2):
    """
    Takes in the data and two actor names, checking to see 
    it they've acted together before.
    """
   
    if actor_id_1 == actor_id_2:
        return True
    #if the actor ids are the same, return true 
    
    if actor_id_1 in data['dict1'][actor_id_2]:
        return True
    #if the actor is in the dictionary value list, also return tru

    if actor_id_2 in data['dict1'][actor_id_1]:
        return True
    #reverse of top case 
    
    return False
    
    #else, return false 
    

def actors_with_bacon_number(data, n):
    """
    Takes in an the data and the desired bacon number. 
    
    Returns actors with the bacon number inputed. 
    """
    actors_seen = {4724}
    actors_before = {4724}
    
    
    #store kevin's ID in actors seen and actors before 
    
    for i in range(n):
        if actors_before == set():
            return set()
        #return empty set if no neighbors
        result = set()
        for actor in actors_before: 
        #loop through actors
            for neighbor in data['dict1'][actor]:
                #loop through neighbors
                if neighbor not in actors_seen:
                    #if we have not seen them, add to neighbors
                    result.add(neighbor)
        actors_before = result
        actors_seen.update(result)
        #return result
        
    return result
    

def bacon_path(data, actor_id):
    """
    Takes in the data and takes in an actor ID. 
    
    Using the actor_to_actor_path, this will return the 
    shortest path to kevin bacon via other actor paths.
    """
    
    
    return actor_to_actor_path(data, 4724, actor_id)
    


def actor_to_actor_path(data, actor_id_1, actor_id_2):
    """
    Takes in the data and takes in an actor ID. 
    
    Using the actor_to_actor_path, this will return the 
    shortest path to kevin bacon via other actor paths.
    """
    #function that gets to actor_id_2
    return actor_path(data, actor_id_1, lambda x: x == actor_id_2)
#    #making a path from actor 1 to actor 2 
#    actors_seen = {actor_id_1}
#    actors_before = {actor_id_1}
#     #store starting ID in actors seen and actors before 
#    levels = []
#    #levels is a list of sets
#    if actor_id_1 == actor_id_2:
#        return [actor_id_1]
#    while True: 
#        levels.append(actors_before)
#        if actors_before == set():
#            return None 
#        result = set()
#        #return empty set if no chain
#        for actor in actors_before: 
#            for neighbor in data['dict1'][actor]:
#                if neighbor not in actors_seen:
#                    #if we have not seen neighbor, add to result 
#                    result.add(neighbor) #if go test function(neighbor) = true, then return path 
#        actors_before = result
#        actors_seen.update(result)
#        #update result
#        
#        if actor_id_2 in actors_before:
#            break 
#        #break out of loop if we see it again
#        
#     #check if neighbors of actor have bacon number n-
#    n = len(levels)
#    path = [actor_id_2]
#    #check if neighbors of actor have bacon number n-
#    #store length of levels 
#    for i in range(n):
#        for neighbor in levels[n-i-1]:
#            if neighbor in data['dict1'][path[-1]]:
#                #check here as well 
#                #if neighbor is in the dictionary, append to path 
#                path.append(neighbor)
#                break 
#    path.reverse()
#    return path
#    #reverse at the end 
    
def movie_path(data, actor_id_1, actor_id_2):
    """
    Takes in the data and takes in an actor ID. 
    
    Find the movies that the actors have acted in together. 
    """
    actor_path = actor_to_actor_path(data, actor_id_1, actor_id_2)
    movies = []
    
    #go through path once, data multiple times
    for i in range(len(actor_path)-1): 
        for tup in data['dict2']:
            if (actor_path[i], actor_path[i+1]) == (tup[0], tup[1]) or (actor_path[i+1], actor_path[i]) == (tup[0], tup[1]):
                movies.append(tup[2])         
                break 
                   
    return movies 

#goal test function 
def actor_path(data, actor_id_1, goal_test_function):
    """
    Takes in the data and takes in an actor ID. 
    
    Using the actor_to_actor_path, this will return the 
    shortest path to kevin bacon via other actor paths.
    """
    actors_seen = {actor_id_1}
    actors_before = {actor_id_1}
    #store starting ID in actors seen and actors before 
    levels = []
    #levels is a list of sets
    flag = False 
    #include flag to create a check in while loop 
    while True: 
        levels.append(actors_before)
        if actors_before == set():
            return None 
        result = set()
        #return empty set if no chain
        for actor in actors_before: 
            if goal_test_function(actor) == True: 
                flag = True
                result.add(actor)
                actor2 = actor
                #change flag value and add to result if condition is true
            else: 
                for neighbor in data['dict1'][actor]:
                    if neighbor not in actors_seen:
                        result.add(neighbor)
                        if goal_test_function(neighbor) == True: 
                            actor2 = neighbor
                            flag = True
                            #else, keep adding until the neighbor yields a true value 
                        
        actors_before = result
        actors_seen.update(result)
        #update result 
                        
        if flag == True:             
            break 
        #break out of loop if flag is true 
                        
       
     #check if neighbors of actor have bacon number n-
    print("hello")
    n = len(levels)
    path = [actor2]
    for i in range(n):
        for neighbor in levels[n-i-1]:
            if neighbor in data['dict1'][path[-1]]:
                #check here as well 
                path.append(neighbor)
                break 
        #return an reverse path as before 
    path.reverse()
    return path
    #reverse at the end 
    


def actors_connecting_films(data, film1, film2):
    return None

if __name__ == '__main__':
    with open('resources/small.pickle', 'rb') as f:
        smalldb = pickle.load(f)

    with open('resources/names.pickle', 'rb') as f:
        namesdb = pickle.load(f)
    
    with open('resources/tiny.pickle', 'rb') as f:
        tinydb = pickle.load(f)
        
    with open('resources/large.pickle', 'rb') as f:
        largedb = pickle.load(f)
        
    with open('resources/movies.pickle', 'rb') as f:
        moviesdb = pickle.load(f)
    
    key_list = list(namesdb.keys())
    val_list = list(namesdb.values())
    position = val_list.index(54189)
    #print(key_list[position])
    #print(namesdb)
    #print(smalldb)
    #print(namesdb['Julie Silver'])
    #print(namesdb['Jean-Marc Roulot'])
    #print(acted_together(transform_data(smalldb), 20853, 931399))
    #print(transform_data(tinydb))
    #print(transform_data(tinydb))
    #print(tinydb)
    #print(actors_with_bacon_number(transform_data(largedb), 6))
    
    print(namesdb['Robert Duvall'])
    #print(namesdb['Iva Ilakovac'])
    #print(actor_to_actor_path(transform_data(largedb), 1284576, 17244))
    new_names = {value: key for key, value in namesdb.items()}
    new_movies = {value: key for key, value in moviesdb.items()}
    #print([new_names[1284576], new_names[105288], new_names[98132], new_names[12797],
          # new_names[32], new_names[17244]])
    #print(largedb)
    #print(movie_path(transform_data(largedb), 3087, 1345462))
    #print([new_movies[8452], new_movies[197919], new_movies[121071], new_movies[256690],
          #new_movies[283406]])
   
    #print(acted_together(transform_data(smalldb), 4724, 9210))
    with open('resources/tiny.pickle', 'rb') as f:
        tiny = pickle.load(f)    
    #print(acted_together(transform_data(tiny), 4724, 2876))
    #print(acted_together(transform_data(tiny), 4724, 1640))
    #print(actor_to_actor_path(transform_data(largedb), 1345462, 89614))
    print(transform_data(tinydb)['dict3'])
    print(tinydb)
 
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    
