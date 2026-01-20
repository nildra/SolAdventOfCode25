import operator

def compute_operation(doc):
    ops_dict = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    with open(doc, 'r') as f:
        total = f.read().splitlines()
        init = [int(x) for x in total[0].split()]
        operators_last_line = total[-1].split()
        for line in total[1:-1]:
            for index, col in enumerate(line.split()):
                ope = ops_dict.get(operators_last_line[index])
                init[index] = ope(init[index],int(col))
    print(sum(init))

compute_operation("input.txt")
