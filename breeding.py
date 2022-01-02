import numpy as np

def get_primes(n):
    return [x for x in range(2, n)
               if all(x % y != 0 for y in range(2, x))
            ]
            


def breed(max_val,primes):
    """"purpose: simulate breeding until there are atleast max_val numbers minted
    
    Returns: list of lists, each element is #'s that are minted on that day
    """
    all_minted = primes

    # start with the primes
    active = primes
    
    while len(active) < max_val-3:
        if i%100==0:
            print(i)
            print(len(active)/max_val)
        active = propagate(active, primes, max_val=max_val)
        all_minted.append(active)
    return all_minted


def find_partner(n, breedable, max_val):
    """helper function for propogate to escape double loop"""
    if n not in breedable:
        return None
    
    for m in breedable:
        # since breedable is sorted, dont need to look anymore
        if n*m > max_val:
            return None
        
        if n*m  < max_val and (n*m not in breedable) :
            return m
        
        # automatically continues under condition n*m<max_val and nothing found so far
    
    return None
    
def find_partner(n, breedable, max_val):
    """helper function for propogate to escape double loop"""
    if n not in breedable:
        return None
    
    for m in breedable:
        # since breedable is sorted, dont need to look anymore
        if n*m > max_val:
            return None
        
        if max_val is None and (n*m not in breedable):
            return m
        if n*m  < max_val and (n*m not in breedable) :
            return m 
        
        # automatically continues under condition n*m<max_val and nothing found so far
    
    return None
    

def propogate(active, primes, max_val=2**14):
    """Purpose: Reproduce active (minted) numbers in one day.
    If two numbers a,b breed/multiply then they are put in deadish list and are not available for more breeding 
        for this round. 
    Propagated holds all numbers that breed

    If n is prime then it will be put back in active before returning.
    A number reproduces with the smallest available number. 
    """
    
    new_nums = []
    deadish = []
    unbreed = []
    propagated = []
    for i in range(len(active)):
        n = active[i]
        
        # don't need to look for smaller memebers of active, its already been done
        # cant reuse dead/already-been-used 
        breedable = [j for j in active[i:] if (j not in deadish) and (j not in new_nums)] # active is sorted so so is breedable
        
        if len(breedable)>0:
            m = find_partner(n, breedable, max_val=max_val)

            # couldnt find a match, move on to next m, keep n for next round
            if m is None:
                unbreed.append(n)
            else:
                new_nums.append(n*m)

                # kill all 3 for the round, bring back the primes before returning
                deadish.append(m)
                deadish.append(n)
                deadish.append(n*m)
                
                propagated.append(n)
                propagated.append(m)
        
        # nothing to breed, dont need to check the rest
        else:
            unbreed += active[i:]
            break
    
    active = list(set(unbreed + new_nums + primes))
    active = sorted(active)
    
    return active, propagated
            
     