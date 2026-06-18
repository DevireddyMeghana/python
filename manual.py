import gc

a=["hello","hi",6000]
print(gc.get_referents(a))
print(gc.get_referrers("hello"))
print(gc.get_referents(10))
print(gc.collect())
print(gc.get_count())
print(gc.get_threshold())
print(gc.set_threshold(5000,20,20))
print(gc.set_threshold(5))
print(gc.disable())
print(gc.enable())