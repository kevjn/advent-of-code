import re

raw_seeds, *raw_maps = open("input").read().split("\n\n")

seeds = list(map(int,re.findall("(\d+)", raw_seeds)))

maps = []
for line in raw_maps:
    d = {}
    for m in line.strip().split('\n')[1:]:
        dst, src, n = map(int,m.split())
        d[(src,src+n)] = (dst,dst+n)
    maps.append(d)

ans = 1e9
for seed in seeds:
    s = seed
    for m in maps:
        for src,dst in m.items():
            start,stop = src
            dstart,dstop = dst
            if s in range(start,stop):
                s = dstart + s-start
                break
    ans = min(ans, s)
print(ans)

seeds = [(a,a+b-1) for a,b in zip(seeds[::2], seeds[1::2])]

ans = 1e9
for seed_range in seeds:
    s = [seed_range]
    for m in maps:
        for seed in s.copy():
            for src,dst in m.items():
                r_seed = range(*seed)
                r_src = range(*src)
                r_dst = range(*dst)

                if r_seed.start in r_src or r_seed.stop in r_src:
                    if seed in s:
                        s.remove(seed)
                    overlap_start,overlap_end = max(r_seed.start, r_src.start), min(r_seed.stop, r_src.stop)
                    dx = r_dst.start-r_src.start
                    x = (overlap_start+dx,overlap_end+dx)
                    left = (r_seed.start, overlap_start) if overlap_start > r_seed.start else None
                    right = (overlap_end, r_seed.stop) if overlap_end < r_seed.stop else None

                    total_len = sum(len(range(*r)) if r else 0 for r in (x,left,right))
                    assert len(r_seed) == total_len

                    s.append(x)
                    if left:
                        s.append(left)
                    if right:
                        s.append(right)

    ans = min(ans, min(a for (a,b) in s))

print(ans)