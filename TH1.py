danhsach1 = [1.0, 3.0]
danhsach2 = [5.0, 7.0]
danhsach = danhsach1 + danhsach2
print(danhsach)
danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)
print(danhsach * 2)
print([x/2 for x in danhsach])
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu  = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print(anh_xa)
tap_hop = set(anh_xa)
print(tap_hop)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
print(lay_monhoc)
import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print(tap_sinh)
kq = list(zip(range(4), range(7, 12), reversed(range(11))))
print(kq)