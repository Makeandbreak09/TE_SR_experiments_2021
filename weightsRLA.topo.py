#!/usr/bin/env python3
from node import *

class weightsRLA(Topo):
    def build(self):
        self.add_node("0")
        self.add_node("1")
        self.add_node("2")
        self.add_node("3")
        self.add_node("4")
        self.add_node("5")
        self.add_node("6")
        self.add_node("7")
        self.add_node("8")
        self.add_node("9")
        self.add_link_name("0", "1", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("1", "0", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("0", "2", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("2", "0", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("1", "3", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("3", "1", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("2", "4", cost=1000, delay=0.2, bw=50000.0, directed=True)
        self.add_link_name("4", "2", cost=1000, delay=0.2, bw=50000.0, directed=True)
        self.add_link_name("2", "5", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("5", "2", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("3", "4", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("4", "3", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("3", "6", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("6", "3", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("4", "7", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("7", "4", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("5", "7", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("7", "5", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("6", "0", cost=1000, delay=0.2, bw=50000.0, directed=True)
        self.add_link_name("0", "6", cost=1000, delay=0.2, bw=50000.0, directed=True)
        self.add_link_name("6", "8", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("8", "6", cost=1000, delay=0.2, bw=20000.0, directed=True)
        self.add_link_name("7", "9", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("9", "7", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("8", "1", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("1", "8", cost=1000, delay=0.2, bw=30000.0, directed=True)
        self.add_link_name("8", "9", cost=1000, delay=0.2, bw=40000.0, directed=True)
        self.add_link_name("9", "8", cost=1000, delay=0.2, bw=40000.0, directed=True)
    
    def dijkstra_computed(self):
        # Demand from 0 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","2")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {2} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{4}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 1 to 3
        build_str = ""
        self.add_command("1", f"ip -6 route add {{3}} metric 1 table 1 src {{1}}  {build_str}")
        # Demand from 2 to 5
        build_str = ""
        self.add_command("2", f"ip -6 route add {{5}} metric 1 table 1 src {{2}}  {build_str}")
        # Demand from 3 to 0
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("3","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {1} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("3", f"ip -6 route add {{0}} metric 1 table 1 src {{3}}  {build_str}")
        # Demand from 4 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("4","2")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {2} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("4","0")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {0} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("4", f"ip -6 route add {{1}} metric 1 table 1 src {{4}}  {build_str}")
        self.add_command("0", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("1", "ip -6 rule add to {3/} iif lo table 1")
        self.add_command("2", "ip -6 rule add to {5/} iif lo table 1")
        self.add_command("3", "ip -6 rule add to {0/} iif lo table 1")
        self.add_command("4", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("0", "nuttcp -6 -S")
        self.add_command("1", "nuttcp -6 -S")
        self.add_command("3", "nuttcp -6 -S")
        self.add_command("4", "nuttcp -6 -S")
        self.add_command("5", "nuttcp -6 -S")
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T150 -i1 -R10000 -N32 {4} \>\>flow_0-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-4.txt\; done\\\" | at now+2min')
        self.add_command("1", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 1 nuttcp -T150 -i1 -R10000 -N32 {3} \>\>flow_1-3.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_1-3.txt\; done\\\" | at now+2min')
        self.add_command("2", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 2 nuttcp -T150 -i1 -R10000 -N32 {5} \>\>flow_2-5.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_2-5.txt\; done\\\" | at now+2min')
        self.add_command("3", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 3 nuttcp -T150 -i1 -R10000 -N32 {0} \>\>flow_3-0.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_3-0.txt\; done\\\" | at now+2min')
        self.add_command("4", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 4 nuttcp -T150 -i1 -R10000 -N32 {1} \>\>flow_4-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_4-1.txt\; done\\\" | at now+2min')

        self.enable_throughput()
        self.add_command("0", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("1", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("2", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("3", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("4", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("5", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("6", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("7", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("8", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("9", "sysctl net.ipv6.fib_multipath_hash_policy=1")

topos = {'weightsRLA': (lambda: weightsRLA())}
