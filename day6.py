def calculateMinGroup(n, levels):
    G = {}
    is_root = {i: True for i in range(n)}
    for i in range(n):
        G[i] = []
    for u,v in levels:
        G[u-1].append(v-1)
        is_root[v-1] = False

    maxHeight = 0

    for i in range(n):
        if not is_root[i]:
            continue
        stack = []
        height = 0
        visited = [False] * n


        stack.append({'v': i, 'depth' : 0})


        while stack:
            s = stack.pop()
            if not visited[s['v']]:
                height = max(height, s['depth'])
                visited[s['v']] = True
            for v in G[s['v']]:
                if not visited[v]:
                    stack.append({
                        'v' : v,
                        'depth' : s['depth'] + 1
                    })
                            #print(f'Now from the root, we traverse to {n} node')
                            # Because visited is a set, this lookup is O(1).
                            #if depths[n] == math.inf:

        maxHeight = max(maxHeight, height)


    return maxHeight + 1
def main():
    #print(calculateMinGroup(n = 5 ,levels = [[1,2], [2,3], [1,4]]))
    #print(calculateMinGroup(n=22,levels = [[4,1],[12,13],[2,22],[22,16],[20,15],[7,14],[17,9],[15,17],[1,10],[14,20],[9,18],[22,12],[16,5]]))
    print(calculateMinGroup(n=45,levels = [[1,12],[11,7],[40,19],[2,17],[10,21],[5,11],[25,14],[30,5],[30,43],[6,8],[24,41],[32,31],[11,37],[28,42],[16,39],[39,27],[35,20],[1,38],[18,44],[33,3],[34,18],[22,36],[41,32],[3,16],[33,26],[7,2],[23,45],[17,33],[36,34],[4,28],[38,10],[44,24],[8,40],[19,35],[16,6],[27,23],[6,1],[16,22],[11,9],[44,25],[23,15],[35,29]]))
    print(calculateMinGroup(22,[[2,11],[8,5],[5,20],[4,7],[5,15],[21,13],[17,8],[12,19]]))
if __name__ == '__main__':
    main()
