from typing import List

class SubdomainVisitCount:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # create a counter dictionary
        res = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split() # split the domain into two by the space
            count = int(count)
            frags = domain.split('.') # cplit each domain by the dot
            for i in range(len(frags)):
                res['.'.join(frags[i:])] += count # join the frags back by [i:], and save the count

        return ["%d %s" % (res[k], k) for k in res] # res[k] is the count, k is the domain