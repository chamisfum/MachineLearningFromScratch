class JumSearch:
    def JumpSearch(data, find):
        data.sort()
        length = len(data)
        jump = int(length**(1/2))

        