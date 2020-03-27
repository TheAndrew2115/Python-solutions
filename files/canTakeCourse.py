import collections

'''
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?
'''

def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # construct hashmap
        courseMap = collections.defaultdict(lambda:[])

        for n in prerequisites:
            courseMap[n[0]].append(n[1])

        for key in courseMap.keys():
            keyNum = 0
            for newKey in courseMap[key]:
                
                while newKey in courseMap.keys():
                    if key in courseMap[newKey]:
                        return False
                    newKey = courseMap[newKey][keyNum]
                keyNum+=1

        return True
                
