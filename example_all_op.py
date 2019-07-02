import linda
linda.connect()

# Exemplo de arquivo que escreve e le do tuplespace

blog = linda.TupleSpace()
linda.universe._out(("MicroBlog",blog))

blog = linda.universe._rd(("MicroBlog",linda.TupleSpace))[1]

blog._out(("bob","distsys","I am studying chap 2"))
blog._out(("bob","distsys","The linda example's pretty simple"))
blog._out(("bob","distsys","A new message!"))
blog._out(("bob","gtcn","Cool book!"))

t1 = blog._rd(("bob","distsys",str))
# t2 = blog._rd(("alice","gtcn",str))
# t3 = blog._rd(("bob","gtcn",str))
print(t1)

blog._in(("bob","distsys","I am studying chap 2"))
t1 = blog._rd(("bob","distsys",str))


print(t1)
# print(t2)
# print(t3)

