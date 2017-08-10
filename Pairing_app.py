import random
import itertools
import time


# def dfs(graph, start, end):



def build_blacklist(blk_lst):
    """ Builds a dictionary/map for the blacklisted pairs of students. i.e if 1 cannot pair with 2 then the value
     for key 1 is the set {1, 2} as no student can pair with themselves. """
    bad_pair_dict = {}
    for stu in blk_lst:
        if stu[0] in bad_pair_dict:  # Appends additional student to stu[0]'s blacklist
            bad_pair_dict[stu[0]].add(stu[1])
        else:  # Adds stu[0] to the blacklist dict with the set of themself and their banned partner
            bad_pair_dict[stu[0]] = {stu[0], stu[1]}
        if stu[1] in bad_pair_dict:  # Mirrors the actions taken above now for stu[1]
            bad_pair_dict[stu[1]].add(stu[0])
        else:  # Mirrors the actions taken above now for stu[1]
            bad_pair_dict[stu[1]] = {stu[0], stu[1]}
    return bad_pair_dict


def find_rand_pairs(stu_lst, blk_lst):
    """ Finds the valid pairings of students using a set of all students and removing bad elements for each student's
    personal blacklist. """
    bad_pair_dict = build_blacklist(blk_lst)
    stu_set = set(stu_lst)
    rand_pairs = []
    try:
        for stu, invalid_pairings in bad_pair_dict.items():
            if len(stu_set) == 0:
                return rand_pairs
            if len(stu_set) == 1:
                loner = stu_set.pop()
                print(loner, " is loner :(")
                rand_pairs.append(loner)
                return rand_pairs
            valid_stu_set = stu_set - invalid_pairings
            valid_partner = random.sample(valid_stu_set, 1)[0]
            rand_pairs.append((stu, valid_partner))
            stu_set -= {stu, valid_partner}
    except ValueError:
        print("No valid pairings. Too many blacklisted.")
        return None


# stu_list = [x for x in range(0, 100000)]
# blk_list = [(1, x) for x in range(0, 1000, 3)]
# blk_list.extend([(2, x) for x in range(0, 1000, 2)])
stu_list = [1, 2, 3, 4]
blk_list = [(1, 2), (2, 3)]
start = time.time()
print(find_rand_pairs(stu_list, blk_list))
print(time.time()-start)
