
class Solution:
    """"""
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return strs
        strs_ordered_with_index = []
        for i in range(len(strs)):
            s_ordered = ''.join(sorted(strs[i]))
            strs_ordered_with_index.append([s_ordered,i])
        strs_ordered_with_index = sorted(strs_ordered_with_index,key=lambda x: x[0])
        ret_list = []
        cur_s = strs_ordered_with_index[0][0]
        cur_list = [strs[strs_ordered_with_index[0][1]]]
        for j in range(1, len(strs)):
            if strs_ordered_with_index[j][0] != cur_s:
                ret_list.append(cur_list)
                cur_s = strs_ordered_with_index[j][0]
                cur_list = [strs[strs_ordered_with_index[j][1]]]
            else:
                cur_list.append(strs[strs_ordered_with_index[j][1]])
        if cur_list:
            ret_list.append(cur_list)
        return ret_list

    def groupAnagramsNice(strs):
        """Great resolution using dictionary"""
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
