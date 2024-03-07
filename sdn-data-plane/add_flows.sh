#!/usr/bin/bash
# utilize priority field to define proper match actions

# A->B->D
sudo ovs-ofctl add-flow s1 priority=1000,in_port=1,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:2
sudo ovs-ofctl add-flow s2 priority=1000,in_port=1,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:3
sudo ovs-ofctl add-flow s4 priority=1000,in_port=1,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:4

# A->C->E->D
sudo ovs-ofctl add-flow s1 priority=500,in_port=1,actions=output:3
sudo ovs-ofctl add-flow s3 priority=500,in_port=1,actions=output:2
sudo ovs-ofctl add-flow s5 priority=500,in_port=2,actions=output:3
sudo ovs-ofctl add-flow s4 priority=500,in_port=3,actions=output:4

# D->C->A
sudo ovs-ofctl add-flow s4 priority=1000,in_port=4,dl_type=0x0800,nw_proto=6,tcp_src=80,actions=output:2
sudo ovs-ofctl add-flow s3 priority=1000,in_port=3,dl_type=0x0800,nw_proto=6,tcp_src=80,actions=output:1
sudo ovs-ofctl add-flow s1 priority=1000,in_port=3,dl_type=0x0800,nw_proto=6,tcp_src=80,actions=output:1

# D->B->E->C->A
sudo ovs-ofctl add-flow s4 priority=500,in_port=4,actions=output:1
sudo ovs-ofctl add-flow s2 priority=500,in_port=3,actions=output:2
sudo ovs-ofctl add-flow s5 priority=500,in_port=1,actions=output:2
sudo ovs-ofctl add-flow s3 priority=500,in_port=2,actions=output:1
sudo ovs-ofctl add-flow s1 priority=500,in_port=3,actions=output:1
