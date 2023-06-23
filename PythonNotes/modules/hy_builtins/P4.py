# yyh hash表
# 将第二列和第三列比较， 第二列的值相同或第三列的值相同则意味着两行相同，统计并分组其数据

hash_dict = {}


class HashKey(object):

    def __init__(self, *args):
        self.args = args
        self.container_args = [args]

    def __hash__(self):
        return 1

    def __eq__(self, other):
        for args in self.container_args:
            if len(other.args) != len(args):
                continue
            result_list = []
            for ci, arg in enumerate(args):
                result_list.append(other.args[ci] == arg)
            # 与
            rl = all(result_list)
            # 或
            rl = any(result_list)
            if rl:
                self.container_args.append(other.args) if other.args not in self.container_args else ...
                return rl


class HashKey2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hash_list = [(x, y)]

    def __hash__(self):
        return 1

    def __eq__(self, other):
        """self指的是容器， other指的是容器外的元素"""
        for t in self.hash_list:
            if t[0] == other.x or t[1] == other.y:
                self.hash_list.append((other.x, other.y)) if other.args not in self.hash_list else ...
                return True
        # return self.x == other.x or self.y == other.y

    def __repr__(self):
        return "<HashKey(%s)>" % id(self)


if __name__ == '__main__':
    data_list = [
        ["A0", "1", "2"],
        ["A1", "3", "2"],
        ["A2", "3", "4"],
        ["A3", "5", "4"],
        ["A4", "6", "7"],
        ["A5", "8", "7"],
        ["A6", "1", "0"],
        ["A7", "10", "9"],
    ]
    print([["A0", "A1", "A2", "A3", "A6"], ["A4", "A5"], ["A7"]])
    for row_list in data_list:
        hash_key = HashKey(row_list[1], row_list[2])
        if hash_key in hash_dict:
            hash_dict[hash_key].append(row_list)
        else:
            hash_dict[hash_key] = [row_list]
    print(hash_dict)

