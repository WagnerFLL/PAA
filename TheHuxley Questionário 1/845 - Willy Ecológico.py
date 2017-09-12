def find_h_min(tree,qttd,begin,end,n):

    x = pos_mid = int((end-begin)/2) + begin
    mid = tree[pos_mid]
    sum = 0

    if(begin == pos_mid):
        return tree[pos_mid]

    x += 1
    while( x < n ):
        sum += tree[x] - mid
        x += 1

    if( sum > qtdd ):
        return find_h_min(tree,qtdd,pos_mid,end,n)

    elif( sum < qtdd ):
        return find_h_min(tree, qtdd, begin, pos_mid, n)

    else:
        return tree[pos_mid]

enter = input().split(' ')
n_tree = int(enter[0])
qtdd = int(enter[1])

trees = []
trees = sorted( [int(x) for x in input().split(' ')] )

print( find_h_min(trees,qtdd,0,n_tree,n_tree) )