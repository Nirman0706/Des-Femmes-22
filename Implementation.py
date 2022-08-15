# example_test.py implements a setup_network() that connects all nodes
# We just have to connect nodes 1 and 2 so it is useless for us. So we delete this part
# 
# 
# Now inside run_test(),

def run_test(self):
    self.nodes[1].generate(1)
    self.sync_blocks()

# First line of the function generate a block through node 1.
# Sending the mined block from node 1 to node 2 can be done with self.sync_blocks()
#
#
# Now to check if node 2 has indeed recieved the block:

assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())


# since the block is trasferred from 1 to 2, getblockhash() should give same value for both nodes.