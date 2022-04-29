from celery import group, chain, chord

from proj.tasks import add, average


# groups run same tasks together
print('Group:')
g = group(add.s(i, i) for i in range(10))
print(g().get())


partial_g = group(add.s(i) for i in range(10))
print(partial_g(10).get())


# chains link tasks together, result of first task is a argument of second task
print('\nChain:')
ch = chain(add.s(2, 8) | add.s(2))
print(ch().get())


ch = (add.s(2, 8) | add.s(2))
print(ch().get())


partial_ch = chain(add.s(2) | add.s(2))
print(partial_ch(8).get())


# chords link tasks together, result of first group task is argument of second task
print('\nChord:')
cho = chord((add.s(i, i) for i in range(10)), average.s())
print(cho().get())


cho = (group(add.s(i, i) for i in range(10)) | average.s())
print(cho().get())



# use group, chain, chord with together
print('\nAll:')
g_ch_cho = (group(add.s(i, i) for i in range(10)) | average.s() | add.s(2))
print(g_ch_cho().get())
