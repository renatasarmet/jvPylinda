import linda
from time import sleep

linda.connect()

blog = linda.universe._rd(("MicroBlog",linda.TupleSpace))[1]

t1 = blog._rd(("bob","distsys",str))


print(t1)
